# Need to install the package pm2
# npm install -g pm2
import os
import sys
import shlex
import subprocess
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

def set_up(self, device):
    apk_reinstall_flag = [line.rstrip('\n') for line in open('../app/apk_reinstall_flag')]

    start_appium_server()
    sleep(20) # allow time for the pm2 process to start
    desired_caps = {}


    if(apk_reinstall_flag[0] == "false"): # reinstall the APK after every test - disabled by default
        #print "apk_reinstall is false, setting desired caps"
        desired_caps["noReset"] = 'true'

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = run_cmd_with_output("adb -s " + device + " shell getprop ro.build.version.release") #TODO meaningful error handling if this fails
    desired_caps['deviceName'] = 'DeviceName'
    # Returns abs path relative to this file and not cwd
    #./aapt dump badging path_to_apk_file
    desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'../app/' + get_apk_name())) #TODO: Don't hard code thi
    desired_caps['appPackage'] = 'com.dalviksoft.calculator' # Parse from selected apk?
    desired_caps['appActivity'] = 'com.android2.calculator3.Calculator' # parse from selected APK
    desired_caps['udid'] = device
    self.desired_caps = desired_caps
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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

def get_apk_name():
    files = run_cmd_with_output("ls -1 " + "../app")
    files = files.splitlines()

    for item in files:
        if item[-4:] == ".apk":
            return item
