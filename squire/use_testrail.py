'''
This module defines functions to connect unit test results to the 
TestRail platform (a Test Case Management & Test Management Software Tool).
To connect any given test you only need to call post_to_testrail() which takes
as arguments the case_id of that unit test in TestRail, the device name, and 
the result flag.  The result flag can either be True or False (if the test passed 
or not).  

If TestRail is not used, this module should not matter.  It is not used by default. 
To use it, include the -testrail flag when running the program.
'''



import testrail

project_name = '' # Your project name here

def get_testrail_client():
    client = testrail.APIClient('') # Your TestRail server here
    client.user = '' # your TestRial login detals here
    client.password = ''
    return client

def update_testrail(case_id,run_id,result_flag):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    #Get the TestRail client account details
    client = get_testrail_client()

    #Update the result in TestRail using send_post function.
    #Parameters for add_result_for_case is the combination of runid and case id.
    #status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5

    if result_flag:
        msg = "Successfully updated the example form"
    else:
        msg = "Failed to update the example form"

    if run_id is not None:
        try:
            result = client.send_post(
                'add_result_for_case/%s/%s'%(run_id,case_id),
                {'status_id': status_id, 'comment': msg })
        except Exception,e:
            print 'Exception in update_testrail() updating TestRail.'
            print 'PYTHON SAYS: '
            print e
        else:
            print 'Updated test result for case: %s in test run: %s with msg:%s'%(case_id,run_id,msg)

    return update_flag

def get_project_id(project_name):
        "Get the project ID using project name"
        client = get_testrail_client()
        project_id=None
        projects = client.send_get('get_projects')
        for project in projects:
            if project['name'] == project_name:
                project_id = project['id']
                #project_found_flag=True
                break
        return project_id

def get_run_id(test_run_name,project_name):
    "Get the run ID using test name and project name"
    run_id=None
    client = get_testrail_client()
    project_id = get_project_id(project_name)
    try:
        test_runs = client.send_get('get_runs/%s'%(project_id))
    except Exception,e:
        print 'Exception in update_testrail() updating TestRail.'
        print 'PYTHON SAYS: '
        print e
        return None
    else:
        for test_run in test_runs:
             if test_run['name'] == test_run_name:
                 run_id = test_run['id']
                 break
        return run_id


def create_test_run(project_name, run_name):
    client = get_testrail_client()
    project_id = get_project_id(project_name)

    try:
        client.send_post('add_run/%s'%(project_id),
            {'name':run_name, "inclue_all":True})
    except Exception,e:
        print 'Exception in update_testrail() updating TestRail.'
        print 'PYTHON SAYS: '
        print e
        return None

def post_to_testrail(case_id,device,result_flag):
    use_testrail = [line.rstrip('\n') for line in open('../app/testrail_flag')]
    should_run = use_testrail[0]
    run_name = use_testrail[1]

    client = get_testrail_client()
    project_id = get_project_id(project_name)
    test_runs = client.send_get('get_runs/%s'%(project_id))

    if should_run == "true":
        name = run_name + "_" + device
        if name not in test_runs:
            create_test_run(project_name, name)

        run_id = get_run_id(name, project_name)

        update_testrail(case_id,run_id,result_flag)
