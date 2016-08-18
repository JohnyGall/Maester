# Need to install the package pm2
# npm install -g pm2
import os
import sys
import shlex
import subprocess
from time import sleep

from appium import webdriver

def init_server(self, device):
    apk_path = os.path.expanduser(self._apk_path)
    print apk_path
    aapt_path = self._aapt_path
    print aapt_path
    adb_path = self._adb_path
    print adb_path
    # apk_reinstall_flag = [line.rstrip('\n') for line in open('../app/apk_reinstall_flag')]

    start_appium_server()
    sleep(20) # allow time for the pm2 process to start
    desired_caps = {}

    '''
    if(apk_reinstall_flag[0] == "false"): # reinstall the APK after every test - disabled by default
        #print "apk_reinstall is false, setting desired caps"
        desired_caps["noReset"] = 'true'
    '''
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = get_platform_version(self, device)
    desired_caps['deviceName'] = 'DeviceName'
    # Returns abs path relative to this file and not cwd
    #./aapt dump badging path_to_apk_file
    desired_caps['app'] = apk_path
    # os.path.abspath(os.path.join(os.path.dirname(__file__), apk_path)) #TODO: Don't hard code thi
    desired_caps['appPackage'] = get_capability(apk_path, aapt_path, "package:")
    desired_caps['appActivity'] = get_capability(apk_path, aapt_path, "launchable-activity:")
    desired_caps['udid'] = device
    self._desired_caps = desired_caps
    self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def start_appium_server():
    start_appium_cmd = "pm2 start appium"
    run_cmd_with_output(start_appium_cmd)

def kill_appium_server():
    kill_appium_cmd = "pm2 stop appium"
    run_cmd_with_output(kill_appium_cmd)

def run_cmd_with_output(cmd):
    cmd = shlex.split(cmd)
    out = subprocess.check_output(cmd)
    out = str(out).rstrip()
    return out

def get_platform_version(self, device):
    curr_dir = os.getcwd()
    os.chdir(os.path.expanduser(self._adb_path))
    value = run_cmd_with_output("./adb -s " + device + " shell getprop ro.build.version.release")
    os.chdir(curr_dir)
    return value


def get_capability(apk_path, aapt_path, capability):
    cap = ""
    curr_dir = os.getcwd()
    os.chdir(os.path.expanduser(aapt_path))
    print os.getcwd()
    print apk_path
    output = run_cmd_with_output("./aapt dump badging " + apk_path + ' -l')
    output = output.splitlines()

    for line in output:
        if capability in line:
            cap = get_capability_from_line(line)
            break

    os.chdir(curr_dir)
    return cap


def get_capability_from_line(line):
    cap = ""
    parenths = list()

    for char in line:
        if char == "'":
            parenths.append(char)
        if len(parenths) == 1 and char != "'":
            cap += char

    return cap
