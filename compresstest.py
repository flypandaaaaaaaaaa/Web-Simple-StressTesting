import os
def test(num):
	for i in range(num):
		os.system('curl 127.0.0.1:10112/cmpfile')
