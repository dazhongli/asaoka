# -*- coding: utf-8 -*-
import pandas as pd

# df - data_frame holding entire piece of data
# interval - delta_t
# data_range 
def Asaoka_fit(df:pd.dataframe,interval,start_date, end_date=0):
    pass
def exponetial_fit(df:pd.dataframe,interval,start_date,end_date =0):
    pass
def fit_data(df:pd.dataframe,interval,start_date, end_date=0, option = 'Asaoka'):
    if end_date ==0:
        end_date = df.date.max
    if option =='Asaoka':
        Asaoka_fit()
    total_days = end_date - start_date
    
    t = np.array(df.relative_time) #holds the time relative to the first 
    s = np.array(df.settlement)    #hodels the settlement
    
    n = total_days/interval
    