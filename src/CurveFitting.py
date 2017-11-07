# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime
from scipy.interpolate import interp1d
from scipy import polyfit
import matplotlib.pyplot as plt

# df - data_frame holding entire piece of data
# interval - delta_t
# data_range 

#The exponential function for Barron's Methods

def exponential_settlement(t):
    return s_inf*(1-a*exp(b*t))
#T0 - date array - numpy array
#S0 - settlement array, numpy array
def Asaoka_fit(T0,S0,interval,start_date=0, end_date=0):
    if end_date ==0:
        end_date = T0.max()
    if start_date==0:
        start_date =T0.min()
    #now convert T0 to days starting from the origin
    T0 =(T0-T0[0])/np.timedelta64(1,'D')
    #user does not specify the end date for fitting, take the maximum
    start_date = np.datetime64(start_date)
    end_date = np.datetime64(end_date)
    n = int(np.floor((end_date-start_date)/np.timedelta64(1,'D')/interval))
    T_bar = np.zeros(n)
    origin = T0[0]
    for i in np.arange(n):
        T_bar[i] = origin + i*interval
    interpolate_1d = interp1d(T0,S0)
    S1=interpolate_1d(T_bar)
    #fit the linear curve
    beta1, beta0 = polyfit(S1[0:-1], S1[1:],1)
    return beta0, beta1
    #we do the interpolation here
#    fig = plt.figure(figsize=(11.69,8.27),dpi=100)
#    ax = fig.add_subplot(2,1,1)
#    ax_Asaoka = fig.add_subplot(2,1,2)
#    ax_Asaoka.plot(S1[0:-1],S1[1:],'ko',label=r'$s_i$ vs $s_{i-1}$',markersize=3)
#    ax_Asaoka.set_xlabel(r'$S_{i-1}$')
    ax_Asaoka.set_ylabel(r'$S_i$')
#    step_of_S1 = len(S1)
#    step_of_S_fitted = int(np.floor(step_of_S1*2.0)) #we will extend the data by 50%
#    fitted_S = np.zeros(step_of_S_fitted)
#    fitted_T = np.zeros(step_of_S_fitted)
#    for index, step in enumerate(np.arange(step_of_S_fitted)):
#        if index ==0:
#            fitted_S[0] = S1[0]
#            fitted_T[0] = T_bar[0]
#        else:
#            fitted_S[index] = beta0 + beta1*fitted_S[index-1]
#            fitted_T[index] = step*interval
#    ax.plot(T0,S0,'bx',label='original data')
#    ax.plot(T_bar,S1,'ro',label='sampled point',markersize=3)
#    ax.plot(fitted_T,fitted_S,label='Asaoka')
#    ax.set_ylim(ax.get_ylim()[::-1])
#    plt.legend()
#    plt.savefig('Asaoka Plot'+'.pdf',format='pdf')
#    plt.show()

#by default we set the data_range = 3 (i.e. we use the first 3 month as data)    
def exponetial_fit(df:pd.DataFrame,data_range, start_date,end_date =0):
    pass

# this function do the predictive analysis using a hyperbolic method
def hyperbolic_fitting(df:pd.DataFrame,interval,start_date,end_date =0):
    pass
# - interval is only required for the asaoka's method, by default is set to zero,
# - i.e., not used in the algorithm
def fit_data(df:pd.DataFrame, start_date, end_date=0, option = 'Asaoka',interval = 0):
    if end_date ==0:
        end_date = df.date.max()
    print(end_date)
    print(start_date)
    print(((end_date-start_date)/np.timedelta64(1,'D'))/30.5)
    if option =='Asaoka':
        pass
    elif option =='general':
        pass
    elif option == 'hyperbolic':
        pass
    total_days = end_date - start_date
