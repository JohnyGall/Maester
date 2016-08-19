# John James Gallagher & Joseph Thomas Campbell
# August 2016
# maester - A platform for running tests on multiple Android devices in series.
# _get_devices.py
#
# This module returns information about the connected phones such as the udids,
# model, and name.  

import _init
import string
import os

#returns a dictionary of relevant information about all
#connected devices.  Each device will have information 
#about its udid, model, and name returned
def get_info(self):
    devices = []

    lines = set_up_list(self)

    for i in range (0, len(lines)):
        info = {"udid": get_phone(lines[i]), 
                "model": get_model(lines[i]), 
                "name": get_name(lines[i])}

        devices.append(info)

    return devices

#get udid
def get_phone(id_line):
    device = ""
    i = 0

    while id_line[i] != ' ':
        device += id_line[i]
        i += 1

    return device

def get_model(id_line):
    model = ""
    i = find_colon(id_line, 2) + 1 #find 2nd colon from the right, go to the space right after

    while id_line[i] != ' ':
        model += id_line[i]
        i += 1
            
    return model

def get_name(id_line):
    name = ""
    i = find_colon(id_line, 1) + 1 #find 1st colon from the right, go to the space right after

    while i != len(id_line) - 1:
        name += id_line[i]
        i += 1

    return name


def set_up_list(self):
    curr_dir = os.getcwd()
    os.chdir(os.path.expanduser(self._adb_path))
    output = _init.run_cmd_with_output("./adb devices -l")
    os.chdir(curr_dir)
    lines = output.splitlines() #make each line an element of the array lines
    lines.pop(0) #get rid of the info line returned
    return lines

#find the indexed number colon from the right and return the index 
def find_colon(line, index):
    colons = list()
    i = len(line) - 1

    while i >= 0:
        if line[i] == ':':
            colons.append(line[i])
        if len(colons) == index:
            return i
        i = i - 1





