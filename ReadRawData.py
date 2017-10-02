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
def plot_raw_data(df):
    