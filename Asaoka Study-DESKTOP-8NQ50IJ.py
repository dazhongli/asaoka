# -*- coding: utf-8 -*-

import os
import numpy as np
import seaborn as sns
import ReadRawData
from CurveFitting import Asaoka_fit
import CurveFitting 



cwd = os.getcwd()
print(cwd)

for root, dirs,files in os.walk(r'.\RawData'):
        for file in files:
            print(file)

df = ReadRawData.read_xl_file(r'.\RawData\RB-170-SM1-1A.xlsx')
date = df.date


#ReadRawData.plot_raw_data(df,'RawData\RB-170-SM1-1A')

CurveFitting.fit_data(df,date.min(),interval = 15)
    

    