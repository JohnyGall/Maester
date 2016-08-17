'''
The Xpaths and IDs of all the UI elements we refer to in unit tests.
They are all here so when the UI changes we don't have to update a huge number of
files
'''

#NUMBERS

def one_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_1")
    
def two_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_2")
    
def three_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_3")
    
def four_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_4")
    
def five_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_5")
    
def six_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_6")
    
def seven_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_7")
    
def eight_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_8")
    
def nine_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_9")
   
def zero_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/digit_0")

def decimal_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/dec_point")

#OPERATORS

def mult_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/op_mul")

def div_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/op_div")

def add_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/op_add")

def subtract_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/op_sub")

def delete_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/del")

def clear_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/clr")

def equals_button(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/eq")

#SCREEN

def display_screen(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/formula")

def sub_result(self):
    return self.driver.find_element_by_id("com.dalviksoft.calculator:id/result")




