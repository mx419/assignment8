"""This module contain a class to finish the invest procedure and save the results"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

#author: Muhe Xie
#netID: mx419
#date: 11/01/2015

class make_single_day_inverstment(object):
    """This class will finish the invest procedure and save the results, the total money invest in a single day is 1000"""

    def __init__(self,positions_list, positions_value_list, num_trial):
        '''the constructor will accept the paramters of investment'''
        self.positions_list = positions_list
        self.positions_value_list = positions_value_list
        self.num_trial = num_trial

    def generate_one_day_investment_result(self,value,num_invest_per_day):
        '''the method will accept the paramters of investment'''
        cumu_ret = 0
        for i in range(num_invest_per_day):
            random_value = np.random.uniform(0,1,1)
            #the result that people win with 51% probability
            if random_value <=0.51:
                cumu_ret =cumu_ret+value*2
        return cumu_ret

    def generate_result_of_n_trials(self):
        '''the method will generate the result of n trials'''
        positions_list = self.positions_list 
        positions_value_list = self.positions_value_list
        num_trials = self.num_trial
        #numeric results saved in this file
        output_target = open('results.txt', 'w')

        for position_i in range(len(positions_list)):
            cumu_ret = np.zeros(num_trials)
            daily_ret = np.zeros(num_trials)
            for trial in range(num_trials):
                cumu_ret[trial] = self.generate_one_day_investment_result(positions_value_list[position_i],positions_list[position_i])
                daily_ret[trial] = (cumu_ret[trial]/1000.0) - 1
            fig = plt.figure()
            plt.hist(daily_ret,100,range=[-1,1])
            plt.xlim(-1,1)
            plt.title('histogram of '+str(positions_list[position_i]) + ' position')
            plt.xlabel('daily return for unit investment')
            plt.ylabel('frequency')
            string_output = "Position = %d, mean = %f, std = %f" %(positions_list[position_i],np.mean(daily_ret),np.std(daily_ret))
            output_target.write(string_output)
            output_target.write('\n')
            save_file_name = 'histogram_'+str(positions_list[position_i]).zfill(4)+'_pos.pdf'
            fig.savefig(save_file_name)
            plt.clf()
        output_target.close()



