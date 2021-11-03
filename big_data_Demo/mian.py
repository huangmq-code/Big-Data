import os
import pandas as pd
import numpy as np
import csv
import matplotlib.pylab as mpy
import scipy as sc
import sys
file_dir='E:/big_data_Demo/CN-Reanalysis201301/201301/'
files=os.listdir(file_dir)
def1=pd.read_csv(os.path.join(file_dir,files[0]))
for e in files[1:]:
    def2=pd.read_csv(os.path.join(file_dir,e))
    def1=pd.concat((def1,def2),axis=0,join='inner')
print(def1)
x=def1['PM2.5(微克每立方米)']
mpy.hist(x,bins=[0,2.5,5,7.5,10,12.5,15,17.5,20,22.5,25,27.5,30,32.5,35,37.5,40,42.5,45,47.5,50,52.5,55,57.5,60,62.5,65,
                 67.5,80,82.5,85,87.5,90,92.5,95,97.5,100,102.5,105,107.5,110,112.5,115,117.5,120,122.5])
mpy.show()
