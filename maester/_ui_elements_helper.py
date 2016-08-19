# John James Gallagher & Joseph Thomas Campbell
# August 2016
# maester - A platform for running tests on multiple Android devices in series.
# _ui_elements_helper.py
#
# Adds a new element to the ui_elements dictionary in the maester class.
# Allows the user to get back that element in the form required by appium
# to interact automatically with the app.


# The element passed in should either be the resource id of the element
# or the xpath AS A STRING.  The name is whatever the user wants to call
# that element's key in the dictionary
def add_element(self, element, name):
    self._ui_elements[name] = element


def get_element(self, name):
    elem = self._ui_elements[name]

    if elem[:2] == "//":
        ui_element = self.get_web_driver().find_element_by_xpath(elem)
    else:
        ui_element = self.get_web_driver().find_element_by_id(elem)
    return ui_element
