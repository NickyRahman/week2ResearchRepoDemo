import os
from subprocess import *

#run secondary script 1
p = Popen([r'D:\Python\PatternCircle.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print output[0]

#run secondary script 2
p = Popen([r'D:\Python\PatternHexagon.py', "ArcEditor"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print output[0]