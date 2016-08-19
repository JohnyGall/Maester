# John James Gallagher & Joseph Thomas Campbell
# August 2016
# maester - A platform for running tests on multiple Android devices in series.
# _init.py
#
# This module will initialize an appium server for a given connected device
# It starts the appium server in the background using the process manager, pm2.
# It also sets all the required capabilites for appium so that it can run the
# specfic apk on the connected device

import os
import sys
import shlex
import subprocess
from time import sleep

from appium import webdriver

def init_server(self, device):
    apk_path = os.path.expanduser(self._apk_path)
    aapt_path = self._aapt_path
    adb_path = self._adb_path

    start_appium_server()
    sleep(20) # allow time for the pm2 process to start
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = get_platform_version(self, device)
    desired_caps['deviceName'] = 'DeviceName'
    desired_caps['app'] = apk_path
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

#gets either the appPackage and appActivity for the apk.  Both
#capabilities are required by appium
def get_capability(apk_path, aapt_path, capability):
    cap = ""
    curr_dir = os.getcwd()
    os.chdir(os.path.expanduser(aapt_path))
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
