# -*- coding: utf-8 -*-

import os
import ReadRawData


cwd = os.getcwd()
print(cwd)

for root, dirs,files in os.walk(r'.\RawData'):
        for file in files:
            print(file)

df = ReadRawData.read_xl_file(r'.\RawData\RA-11-SM1-1.xlsx')

ReadRawData.plot_raw_data(df,'RawData\RA-11-SM1-1')

def Asaoka(t,s,interval,starting_point):
    pass


    