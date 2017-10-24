 -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import os
import datetime
import statsmodels.api as sm


def read_xl_file(filename):
    df = pd.read_excel(,sheetname=0,
                   skiprows=13)
    column_name = ['ID','date','tube_top','tube_heigth','plate_level','difference',
               'settlement','ground_level','remarks']
    df.columns = column_name[0:len(df.columns)]
    df.set_index(df['date'],inplace = True)
    df.dropna(axis=0,how='all', inplace=True, subset=['date'])
    return df
#below function read the sm files
def plot_raw_data(df,filename = ''):
    fig = plt.figure(figsize=(11.69,8.27),dpi=100)
    fig.suptitle(filename.split('.')[0])
    ax_settlement = fig.add_subplot(2,1,2)
    ax_groundlevel = fig.add_subplot(2,1,1)
    df_date = np.array(df['date'])
    time_incr = (df_date - df_date[0])/np.timedelta64(1,'D')
    df_settlement = np.array(df.settlement)
    df_groundlevel = np.array(df.ground_level)
    #calculate the relative distance
#    for index, rows in df.iterrows():
#        for row in rows:
#            #calculate the timedelta between two dates
#            df.loc[index,'relative_time']=(df.loc[index,'date']-
#                  df.loc[0,'date'])/np.timedelta64(1,'D')
    lowess = sm.nonparametric.lowess(df_settlement, time_incr,frac=0.1)
    ax_settlement.plot(df_date, df_settlement,'bx',markersize=4)
    ax_settlement2 = ax_settlement.twiny()
    settlement = df['settlement']
    ax_groundlevel.plot(df_date,df_groundlevel,'k')
    ax_settlement.set_xlabel('Date')
    ax_settlement.set_ylabel('Settlement(mm)')
    ax_groundlevel.set_ylabel('Grpassound_level(mpD)')
    ax_settlement2.plot(time_incr,df_settlement,'bx',markersize=4,label ='orignal data')
    ax_settlement2.plot(lowess[:,0],lowess[:,1], 'k-',label='smoothed curve',)
    ax_settlement2.legend()
    #Set the axis of the plot
    ax_settlement.set_ylim(ax_settlement.get_ylim()[::-1])
    ax_settlement.grid()
    plt.savefig(filename.split('.')[0]+'- settlement vs time'+'.pdf',format='pdf')
    plt.show()
def read_SMM_data_settlement(filename,sheetname=0,index_id=0):
    if os.path.isfile(filename):
        df = pd.read_excel(filename,skiprows=70,sheetname =sheetname, parse_cols=index_id)
        df.dropna(axis=0,how='any',inplace=True)
        df.columns=['date','reference_level','difference','settlement','Northing']
        df.set_index(df['date'],inplace = True)
        return df
    else:
        pass
    