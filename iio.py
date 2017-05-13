import time
import os


start=time.time()
os.system("bash iio.sh")
print("samplaterate:{}".format(1/(time.time()-start)*1000))