#!/usr/bin/python
#Filename=common.py

import os
import numpy
import shutil

NaNs_freq=[2,4,6,8,10]
prop_MAF=[0.02,0.04,0.06,0.08,0.1]
reps= range(1,201)
folds = range (1,11)

rootpath=os.getcwd()
#comb_dir_localname=[]

#prepGmatrix_path="prepGmatrix"
#prepGmatrix_abs_path=rootpath+"/prepGmatrix"

#prepData_path="prepData"
#prepData_abs_path=rootpath+"/prepData"

#paramFiles_path="paramfiles111"
#paramFiles_abs_path= rootpath+"/paramfiles"


class common:
	comb_dir_localname=[]
	target_directory1=""
	#define variables belong to common class
	#rootpat=os.getcwd()
	prepGmatrix_path="prepGmatrix"
#	print "this is inside class common: "+prepGmatrix_path
	prepGmatrix_abs_path=rootpath+"/prepGmatrix"

	prepData_path="prepData"
	prepData_abs_path=rootpath+"/prepData"
	
	paramFiles_path="paramfiles"
	paramFiles_abs_path= rootpath+"/paramfiles"
	@staticmethod
	def abs_dir(x):
		nonlocal 	
		abs_x=rootpath+x
		print abs_x

        @classmethod	
	def creatdir(self,target_directory):
		self.target_directory=target_directory
#		print(self.target_directory)
		try:
			shutil.rmtree(self.target_directory)
		except Exception, exception:
			pass
   		#	print exception
		os.makedirs(self.target_directory)	

	@classmethod
	def tworound(self):
		#nonlocal comb_dir_localname
		for i in NaNs_freq:
			for j in prop_MAF:
	       			dirname = "NaN_%s_MAF_%s" % (str(i),str(j))
       				self.comb_dir_localname.append(dirname)
	#	print comb_dir_localname


	@classmethod
        def threeround(self):
                for i in NaNs_freq:
                        for j in prop_MAF:
				dirname="NaN_%s_MAF_%s" % (str(i),str(j))
				self.comb_dir_localname.append(dirname)
				for k in reps:
					rep_dir = "rep_%s" % (str(k))   
					parameters_filename="parameters_%s_%s_%03d.R" % (str(i),str(j),k)
					prepData_localname="Y_random.r_%s.csv" % (str(k))
					prepGmatrix_localname="G_G_NaNs_%s_prop.MAF_%s.rda" % (str(i),str(j))								
        #       print comb_dir_localname

