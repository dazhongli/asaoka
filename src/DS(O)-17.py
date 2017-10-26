from ReadRawData import read_settlement_data,plot_raw_data,read_xl_file
import os
cwd = os.getcwd()
os.chdir(cwd)
print('hello')
filename = os.path.join(cwd,r'..\RawData\DS(O)-17-SMM3C_Rev1.xlsx')
df1 = read_settlement_data(filename,0,0,4,skiprows=14)
df2 = read_settlement_data(filename,0,0,7,skiprows=14)
plot_raw_data([df1,df2],['DS(O)-17-SMM3C1','DS(O)-17-SMM3C2'],'DS(O)-17-SMM3C',ground_level=False)
filename = os.path.join(cwd,r'..\RawData\DS(0)17-SM1-2R (Adjusted).xls')
df3 =read_xl_file(filename)
plot_raw_data([df3],['DS(0)17-SM1-2R'],'DS(0)17-SM1-2R',ground_level=True)