#!/usr.bin/python
#filename=gen_master_input_list.py

import os
import numpy
from common import *
comb_dir_fullname=[]
dirname=""
parameters_filename=""

b=common()
b.tworound()
#for key in b.comb_dir_localname:
#	dirname=os.path.join(b.paramFiles_path,key)
#       comb_dir_fullname.append(dirname)
#	b.creatdir(dirname)

#fp=open("/home/jennyshao/Geno/src/abc.txt")

#os.mknod("/home/jennyshao/Geno/src/aaa/abc111.txt")

 
for i in NaNs_freq:
	for j in prop_MAF:
		comb_dir_localname = "NaN_%s_MAF_%s" % (str(i),str(j))
		dirname=os.path.join(b.paramFiles_path,comb_dir_localname)
		print "this is dirname: "+dirname
		prepGmatrix_localname="G_G_NaNs_%s_prop.MAF_%s.rda" % (str(i),str(j))
		for k in reps:
			parameters_filename="parameters_%s_%s_%03d.R" % (str(i),str(j),k)
			parameters_filename1=dirname+"/"+parameters_filename
	#		print parameters_filename
			os.mknod(parameters_filename1)	
			prepData_localname="Y_random.r_%s.csv" % (str(k))
			print "%s_%s %s %s %s" % (combination_dir_localname,rep_dir,parameters_filename, \
                                                prepData_localname,prepGmatrix_localname)

#print comb_dir_fullname
#print b.parameters_filename
#for key in comb_dir_fullname:
#	touch 


#print "%s_%s %s %s %s"%(b.comb_dir_localname,rep_dir)
