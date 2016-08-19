import os
import sys

from appium import webdriver
import _init
import _get_devices
import _ui_elements_helper

class new_squire:
    _apk_path = ""
    _appt_path = ""
    _adb_path = ""
    _ui_elements = {}
    _driver = None
    _desired_caps = None #do we actually need this?

    def set_apk_path(self, path):
        self._apk_path = path

    def set_aapt_path(self, path):
        self._aapt_path = path

    def set_adb_path(self, path):
        self._adb_path = path

    def get_adb_path(self):
        return self._adb_path

    def get_aapt_path(self):
        return self._aapt_path

    def get_adb_path(self):
        return self._adb_path

    def get_web_driver(self):
        return self._driver

    def kill_appium(self):
        _init.kill_appium_server()

    def init (self, device):
        _init.init_server(self, device)

    def add_element(self, element, name):
        _ui_elements_helper.add_element(self, element, name)

    def get_element(self, name):
        return _ui_elements_helper.get_element(self, name)

    def get_elements(self):
        return _ui_elements

    def get_devices(self):
        return _get_devices.get_info()
