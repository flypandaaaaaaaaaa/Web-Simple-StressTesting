from time import sleep,time
from compresstest import test
import os
x1=time()
test(10000)
x2=time()
with open('/tmp/testresult.txt','w') as f:
	f.write(str(x2-x1))
