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


fig, (ax0, ax1) = plt.subplots(nrows=2 ,figsize=(12,8 ))

ax0.plot(time, data[:,1]*5/1024)
ax0.set_ylabel('voltage(V)')
ax0.set_xlabel('time(n)')
n=data.shape[0]

rate=float(csv.columns[0])
p = np.abs(np.fft.fft(data[:,1]))/n


f = np.linspace(0, rate/2, len(p))


freqs = np.fft.fftfreq(data[:,1].size, 1/rate)
idx = np.argsort(freqs)
idx2=idx[int(idx.shape[0]/2):int(idx.shape[0]/2)+20]
ax1.set_xlabel("Frequence(Hz)")
ax1.set_ylabel("Amplitude")
ax1.set_title('Samplerate: {}   N: {}  '.format(rate,n), fontsize=16)
ax1.bar(freqs[idx2], p[idx2])


plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

plt.show()