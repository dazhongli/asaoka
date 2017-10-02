# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import os 

def read_xl_file(filename):
    
    df = pd.read_excel(filename,sheetname=0,
                   skiprows=13)
    
    column_name = ['ID','date','tube_top','tube_heigth','plate_level','difference',
               'settlement','ground_level','remarks']
    df.columns = column_name
    df.dropna(axis=0,how='all', inplace=True, subset=['date'])
    return df
def plot_raw_data(df,filename = ''):
    fig = plt.figure(figsize=(11.69,8.27),dpi=100)
    fig.suptitle(filename)
    ax_settlement = fig.add_subplot(2,1,2)
    ax_groundlevel = fig.add_subplot(2,1,1)
    df_date = np.array(df['date'])
    df_settlement = np.array(df.settlement)
    df_groundlevel = np.array(df.ground_level)
    ax_settlement.plot(df_date, df_settlement,'bx',markersize=4)
    ax_groundlevel.plot(df_date,df_groundlevel,'k')
    ax_settlement.set_xlabel('Date')
    ax_settlement.set_ylabel('Settlement(mm)')
    ax_groundlevel.set_xlabel('Date')
    ax_groundlevel.set_ylabel('Ground_level(mpD)')
    
    #Set the axis of the plot
    ax_settlement.set_ylim(ax_settlement.get_ylim()[::-1])
    
    
    plt.savefig('settlement vs time'+'.pdf',format='pdf')
    plt.show()
    