#coding=utf-8

import os, sys, platform

os.system('rm -rf sunilamjad.so sunilamjad32.so')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf sunilamjad.so sunilamjad32.so')

except:

    pass

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('sunil.so'):

        os.system('curl -L https://github.com/kameenax-143/executables/blob/main/sunilamjad.cpython-311.so?raw=true -o sunilamjad.so') 

        import sunilamjad

    else:

        import sunilamjad

elif bit == '32bit':

    if not os.path.isfile('sunilamjad32.so'):

        os.system('curl -L https://github.com/kameenax-143/executables/blob/main/sunilamjad32.cpython-311.so?raw=true -o sunilamjad32.so') 

        import sunilamjad32

    else:

        import sunilamjad32

