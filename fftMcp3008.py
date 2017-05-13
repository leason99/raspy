
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import os
import sys
import readline
import glob

dirPath=os.path.dirname(os.path.abspath(sys.argv[0]))

#autocomplete
def pathCompleter(text,state):
    line   = readline.get_line_buffer().split()
    return [x for x in glob.glob(text+'*')][state]
readline.set_completer_delims('\t')
readline.parse_and_bind("tab: complete")
readline.set_completer(pathCompleter)

#show dir filename
print("dir's csv file: \n")
for x in glob.glob(dirPath+'/*.csv'):
    print(os.path.basename(x))
filename=input("\nPlease input cvs filename :")
print (filename)


filePath=os.path.join(dirPath,filename)
csv=pd.read_csv(filePath)
data=np.array(csv)
time=data[:,0]
plt.plot(time, data[:,2])
plt.ylabel('voltage(V)')
plt.xlabel('time(n)')
plt.show()






import numpy as np
#import pylab as pl
rate = 30
time=1
n=rate*time
t = np.arange(0, time, 1/rate)
data = np.sin(2*np.pi*t) #+ 2*np.sin(2*np.pi*7*t)
p = np.abs(np.fft.rfft(data))/n*2
f = np.linspace(0, rate/2, len(p))
#pl.plot(f, np.abs(np.fft.rfft(x)))
plt.bar(f,p,width=0.1,)
plt.xticks(f)
plt.yticks(np.arange(0,int(max(p))+1,0.5))
plt.show()

