# -*- coding: utf-8 -*-

import os
import numpy as np
import seaborn as sns
import ReadRawData
from CurveFitting import Asaoka_fit



cwd = os.getcwd()
print(cwd)

for root, dirs,files in os.walk(r'.\RawData'):
        for file in files:
            print(file)
folder = r'C:\Users\dz.li\OneDrive\02 - Projects\Professional\HKBCF\00 - Monitoring Data\Reclamation Settlement Assessment\SM1'
filename = r'DS(0)11-SM1-2R (Adjusted).xls'
df_settlement = ReadRawData.read_xl_file(os.path.join(folder,filename))

#ReadRawData.plot_raw_data(df,filename)
SMM_path = r'C:\Users\dz.li\OneDrive\02 - Projects\Professional\HKBCF\00 - Monitoring Data\SMM\SMM3B\DS(O)'
SMM_filename = 'Graphical Plot for DS(O)11-SMM3B.xlsx'
df_SMM = ReadRawData.read_SMM_data_settlement(os.path.join(SMM_path,SMM_filename),sheetname = 1,index_id= [2,3,4,5,6])