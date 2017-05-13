#!/usr/bin/env python3

"""This script prompts a user to enter a message to encode or decode
   using a classic Caeser shift substitution (3 letter shift)"""
 

import sys
import os
import time
#import Adafruit_MCP3008
#from MCP3008 import MCP3008
from BCMMCP3008 import MCP3008
import numpy as np
import pandas as pd


times=3000

SPI_PORT= 0
SPI_DEVICE = 0
chnum = 0
chnum = int(input("chanel_num:"))


if 1<= int(chnum) <= 8:
    pass
else:
    chnum=1


mcp = MCP3008()
#startTime=time.time()
#cu=range(times)
#ch=range(0,chnum)
#for count in cu:
#    for i in ch:
#        data[count,i]= mcp.read_adc(i)
    
result=mcp.read_adc_loop(chnum,times)
column = ["ch1", "ch2", "ch3","ch4","ch5","ch6","ch7","ch8"]
cvs=pd.DataFrame(columns=column[0:chnum],data=result["data"])

#cvs.loc[count]=data[:]
filename=time.strftime("%Y%m%d_%H%M%S",time.localtime())
dirPath=os.path.dirname(os.path.abspath(sys.argv[0]))
filePath=os.path.join(dirPath,filename+".csv")
cvs.to_csv(filePath,index_label=result["samplerate"])

