"""this module define some user-defined exceptions"""

#author: Muhe Xie
#netID: mx419
#date: 11/05/2015

class Input_Format_Error(Exception):
    # raised when user's input's format is wrong
    def __str__(self):
        return 'The input format is wrong\n'

class Repeated_Number_Error(Exception):
    # raised when there are repeated number in the list
    def __str__(self):
        return 'There are repeated number in the list\n'

class Empty_Input_Error(Exception):
    # raised when user input is empty
    def __str__(self):
        return 'The input is empty\n'
    
class Zero_Input_Error(Exception):
    # raised when user input is 0
    def __str__(self):
        return 'The input is 0\n'

class Invalid_Input_Error(Exception):
    # raised when user input number is not valid
    def __str__(self):
        return 'The input number is not valid'