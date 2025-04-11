import numpy as np
import time

py_list=[2,4,3,5,2,4,5]
np_arr=[4,2,4,2,4,2,4]
start=time.time()
py_list=[i*2 for i in range(100000)]
print("\n Time for eqecution: ",time.time()-start)
start=time.time()
np_arr=np.arange(100000)*2
print("\n Time for eqecution: ",time.time()-start)
