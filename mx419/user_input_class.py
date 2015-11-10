"""This module contain a class to validate the input of user of the position list"""

import re
from user_defined_exceptions import *

#author: Muhe Xie
#netID: mx419
#date: 11/01/2015
class User_Input_String:
    '''this class will validate the user input of user of the position list'''
    def __init__(self,str_list):
        '''the constructor will check the user input'''
        self.position_list_str = str_list
        self.standard_list = [1,10,100,1000]
        #use regular expression to check the input
        if  not re.match(r"\s*[\s*[0-9]+(,\s*[0-9]+\s*){0,}]$", self.position_list_str): 
            raise Input_Format_Error
        else:
            number_str_list = re.findall(r'[0-9]+', self.position_list_str) 
            number_list = []
            for i in range(len(number_str_list)):
                int_tmp = int(number_str_list[i])
                if int_tmp not in self.standard_list:
                    raise Invalid_Input_Error
                    
                elif int_tmp in number_list:
                    raise Repeated_Number_Error
                else:
                    number_list.append(int_tmp)
            self.position_list = number_list
    def get_positions(self):
        '''the method will return the position list'''
        return self.position_list
    
    def get_position_values(self):
        '''the method will return the position value list'''
        value_list = []
        for i in range(len(self.position_list)):
            int_tmp = 1000/self.position_list[i]
            value_list.append(int_tmp)
        return value_list