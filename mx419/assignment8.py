"""
This module is the main program of hw8. It mainly deal with the user input and call
other modules to generate the results 

"""
import numpy as np 
import math
import matplotlib.pyplot as plt
from user_defined_exceptions import *
from user_input_class import *
import make_investment_class


#author: Muhe Xie
#netID: mx419
#date: 11/01/2015

def start_investment():
    '''This function will read the input of user and call related modules to calculate and output the investment result'''
    
    while True:
        try:
            print "Please Enter a list of positions (input should like [1,10,100,1000] or any subset of the list, do not input repeated number), enter \'quit\' to exit:"
            str_list_input = raw_input()
            if str_list_input == "quit": #quit the program
                print "Goodbye"
                return
            if str_list_input == "": #test empty input 
                raise Empty_Input_Error
            position_list_object = User_Input_String(str_list_input) #use user input class to deal with the user input
            #list of positions
            positions_list = position_list_object.get_positions()
            #list of position values
            positions_value_list = position_list_object.get_position_values()
            break
            
        except Empty_Input_Error:
            print "The input is empty, please re-enter the list"

        except Input_Format_Error:
            print "The input format is wrong, please re-enter the list"
            
        except Repeated_Number_Error:
            print "Repeated numbers, please re-enter the list"
       
        except Invalid_Input_Error:
            print "The input number is not valid, please re-enter the list"
            
    while True:
        try:
            print "Please Enter the number of trials, i.e. 10000(recommended) enter \'quit\' to exit:"
            num_trial_input = raw_input()
            if num_trial_input == "quit": #quit the program
                print "Goodbye"
                return
            if not re.match(r"\s*[0-9]+\s*",num_trial_input):
                raise Input_Format_Error
            if num_trial_input == "": #test empty input 
                raise Empty_Input_Error
            if int(num_trial_input) == 0:
                raise Zero_Input_Error
            num_trial = int(num_trial_input)
            break 
        except Empty_Input_Error:
            print "The input is empty, please re-enter the list"

        except Input_Format_Error:
            print "The input format is wrong, please re-enter the list"
            
        except Zero_Input_Error:
            print "The input is 0, please re-enter the list"

    #create an instance of make_single_day_investment to do the experiment
    execute_investment = make_investment_class.make_single_day_inverstment(positions_list, positions_value_list, num_trial)
    print "please wait..."
    #this function will generate the final results, include the pdfs and the results.txt
    execute_investment.generate_result_of_n_trials()
    print "Congratulations! the results are saved succeffully, thanks for trying ,bye"

if __name__ == "__main__":
    try:
        start_investment()    

    except KeyboardInterrupt:
        print "the program has been interrupted by KeyboardInterrupt, thanks for trying,Goodbye"

    except EOFError:
        print "the program has been interrupted by EOFERROR, thanks for trying, Goodbye"

    except TypeError:
        print "the program has been interrupted by TypeError, thanks for trying, Goodbye"

    except OverflowError:
        print "the program has been interrupted by OverflowError, thanks for trying, Goodbye"

