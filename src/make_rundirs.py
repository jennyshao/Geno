#!/usr/bin/python

#filename=make_rundirs.py

import numpy
import shutil
import os

from common import *
a=common()
target_directory=rootpath+"/run_home"

a.creatdir(target_directory)
a.threeround()

for key in a.comb_dir_localname:
	newkey=target_directory+"/"+key+"/"+"condor_out"
	a.creatdir(newkey)
