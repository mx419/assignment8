"""This module contains the unit tests of the hw8 program"""

import numpy as np 
from unittest import TestCase
import unittest
import user_input_class
from user_defined_exceptions import *
#author: Muhe Xie
#netID: mx419
#date: 11/05/2015


class Test_HW8(TestCase):
    '''this class will test the functions and methods of classes in homework8'''
    def setUp(self):
        pass

    def test_User_Input_String1(self):
        '''the method will test the validation function of User_Input_String class '''
        with self.assertRaises(Input_Format_Error):
            user_input_class.User_Input_String('[2]]')

        with self.assertRaises(Input_Format_Error):
            user_input_class.User_Input_String('[10,,10]')

    def test_User_Input_String2(self):
        with self.assertRaises(Invalid_Input_Error):
            user_input_class.User_Input_String('[2,10]')

        with self.assertRaises(Repeated_Number_Error):
            user_input_class.User_Input_String('[10,10]')

        

    def test_User_Input_String3(self):
        '''the method will test the assignment function of User_Input_String class'''
        instance1 = user_input_class.User_Input_String('[1,10,100,1000]')

        self.assertEqual(10,instance1.position_list[1])

        self.assertEqual(100,instance1.get_position_values()[1])

        self.assertEqual(1,instance1.get_position_values()[3])

        self.assertEqual(1000,instance1.position_list[3])


        


if __name__ == '__main__':
    unittest.main()


        

