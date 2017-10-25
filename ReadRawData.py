import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm
import matplotlib.markers as mks
from scipy.interpolate import interp1d

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
def plot_raw_data(dfs,df_names,fig_name,ground_level=True, offset=False):
    #let's get the earlest data of the data frame
    dates = []
    #get the starting dates for all curves
    for df in dfs:
        dates.append(np.datetime64(min(df.date.tolist())))
    if offset == True :
        offset_date = max(dates)
        
    date_orgin =min(dates)
    fig = plt.figure(figsize=(11.69,8.27),dpi=100)# A4 size paper
    fig.suptitle(fig_name)
    if ground_level:
        ax_settlement = fig.add_subplot(2,1,2)
        ax_groundlevel = fig.add_subplot(2,1,1)   
    else:
        ax_settlement = fig.add_subplot(1,1,1)
    ax_settlement2 = ax_settlement.twiny()
    for index,df in enumerate(dfs):
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
                           marker=(marker_list[index]))
        #plot at the day-axis
        ax_settlement2.scatter(time_incr,df_settlement,marker=(marker_list[index]),
                            label =df_names[index])
        ax_settlement2.plot(lowess[:,0],lowess[:,1], 'k-')
        if ground_level and 'ground_level' in df.columns:
            ax_groundlevel.plot(df_date,df_groundlevel,'k')
            ax_groundlevel.set_ylabel('Grpassound_level(mpD)')
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
