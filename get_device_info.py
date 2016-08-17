'''
This module returns information about the connected phones such as the udids,
model, and name
'''

import init
import string

#returns the udids for all connected phones/emulators
def get_info():
    devices = []

    lines = set_up_list()

    for i in range (0, len(lines)):
        devices.append(get_phone(lines[i]))

    return devices

#get udid
def get_phone(id_line):
    device = ""
    i = 0

    while id_line[i] != ' ':
        device += id_line[i]
        i += 1

    return device

def get_model(device):
    lines = set_up_list()
    model = ""

    for i in range (0, len(lines)):
        if device == get_phone(lines[i]):
            j = find_colon(lines[i], 2) + 1 #find 2nd colon from the right, go to the space right after
            while lines[i][j] != ' ':
                model += lines[i][j]
                j += 1
            break

    return model

def get_name(device):
    lines = set_up_list()
    name = ""

    for i in range (0, len(lines)):
        if device == get_phone(lines[i]):
            j = find_colon(lines[i], 1) + 1 #find 1st colon from the right, go to the space right after
            while j != len(lines[i]) - 1:
                name += lines[i][j]
                j += 1
            break

    return name


def set_up_list():
    output = init.run_cmd_with_output("adb devices -l")
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



