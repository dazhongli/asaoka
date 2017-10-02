# -*- coding: utf-8 -*-


import ReadRawData

cwd = os.getcwd()
print(cwd)

for root, dirs,files in os.walk(r'.\RawData'):
        for file in files:
            print(file)

df = ReadRawData.read_xl_file(r'.\RawData\RA-11-SM1-1.xlsx')



def Asaoka(t,s,interval,starting_point):
    pass


    