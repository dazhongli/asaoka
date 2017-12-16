# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm
import matplotlib.markers as mks

def read_xl_file(filename):
    df = pd.read_excel(filename,sheetname=0,
                   skiprows=13)
    column_name = ['ID','date','tube_top','tube_heigth','plate_level','difference',
               'settlement','ground_level','remarks']
    df.columns = column_name[0:len(df.columns)]
    df.set_index(df['date'],inplace = True)
    df.dropna(axis=0,how='all', inplace=True, subset=['date'])
    return df
#below function read the sm files
#noc sets the number of color used for plotting curves
def plot_raw_data(dfs,df_names,fig_name,ground_level=False, offset=False):
    #let's get the earlest data of the data frame
    noc = len(dfs)
    dates = []
    #get the starting dates for all curves
    for df in dfs:
        dates.append(np.datetime64(min(df.date.tolist())))
    if offset == True :
        pass #we will handle this later
    date_orgin =min(dates)
    fig = plt.figure(figsize=(11.69,8.27),dpi=100)# A4 size paper
    fig.suptitle(fig_name)
    if ground_level:
        ax_settlement = fig.add_subplot(2,1,2)
        ax_groundlevel = fig.add_subplot(2,1,1)
    else:
        ax_settlement = fig.add_subplot(1,1,1)
    ax_settlement2 = ax_settlement.twiny()
    color=iter(plt.cm.rainbow(np.linspace(0,1,noc)))
    for index,df in enumerate(dfs):
        c=next(color)
        if isinstance(dfs,list)==False:
            df = dfs
        try:
            df_settlement = np.array(df.settlement)
            df_date = np.array(df['date'])
            if ground_level:
                df_groundlevel = np.array(df.ground_level)
        except:
            print('Error happened in the programm')
        time_incr = (df_date - date_orgin)/np.timedelta64(1,'D')
        df_settlement = np.array(df.settlement)
        if ground_level and 'ground_level' in df.columns:
            df_groundlevel = np.array(df.ground_level)
        lowess = sm.nonparametric.lowess(df_settlement, time_incr,frac=0.1)
        marker_list = list(mks.MarkerStyle.markers.keys())
        ax_settlement.scatter(df_date, df_settlement,
                           marker=(marker_list[index]),c=c)
        #plot at the day-axis
        #ax_settlement2.scatter(time_incr,df_settlement,marker=(marker_list[index]),
         #                      c=c,label =df_names[index])
        ax_settlement2.plot(lowess[:,0],lowess[:,1], '-',c=c,label =df_names[index])
        if ground_level and 'ground_level' in df.columns:
            ax_groundlevel.plot(df_date,df_groundlevel,c=c)
            ax_groundlevel.set_ylabel('Ground Level(mpD)')
        if isinstance(dfs,list)==False:
            break
    ax_settlement.set_xlabel('Date')
    ax_settlement.set_ylabel('Settlement(mm)')
    ax_settlement2.legend()
    #Set the axis of the plot
    ax_settlement.set_ylim(ax_settlement.get_ylim()[::-1])
    ax_settlement.grid()
    plt.savefig(fig_name+'- settlement vs time'+'.pdf',format='pdf')
    plt.show()
def read_SMM_data_settlement(filename,sheetname=0,index_id=0):
    if os.path.isfile(filename):
        df = pd.read_excel(filename,skiprows=70,sheetname =sheetname, parse_cols=index_id)
        df.dropna(axis=0,how='any',inplace=True)
        df.columns=['date','reference_level','difference','settlement','Northing']
        df.set_index(df['date'],inplace = True)
        df.date = pd.to_datetime(df.date)
        return df
    else:
        pass
def read_settlement_data(filename,sheet_index,date_column,settlement_column,skiprows=0):
    df = pd.read_excel(filename,skiprows=skiprows,sheetname=sheet_index,
                       parse_cols=[date_column,settlement_column])
    df.dropna(axis=0,how='any',inplace=True)
    df.columns=['date','settlement']
    df.set_index(df['date'],inplace=True)
    df.date=pd.to_datetime(df.date)
    return df
