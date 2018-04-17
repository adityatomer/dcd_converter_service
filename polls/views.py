#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import logging as logger
# import mdtraj as md
import mdtraj as md
import numpy as np





# # def getLogging(filePath):
logger.basicConfig(
	format="%(asctime)s [%(threadName)-12.12s %(lineno)d] [%(levelname)-5.5s]  %(message)s",
	handlers=[
	logger.FileHandler("{0}/{1}.log".format("./", "app.log")),
	logger.StreamHandler()
	],
	level=logger.INFO)



def convert(infile,topologyFile):
    t=md.load_dcd(infile, top=topologyFile)
    nparray=t.xyz
    xyz=np.squeeze(np.multiply(nparray,10))
    
    return xyz


def index(request):
	# ans=convert.convert()
	t=convert("/Users/adityatomer/Desktop/django_test/dcd_convertor_service/polls/sample_dcd.dcd","/Users/adityatomer/Desktop/django_test/dcd_convertor_service/polls/sample_dcd_new.pdb");
	content=str(t)
	logger.info(content)


	response = HttpResponse(content, content_type='text/plain')
	response['Content-Length'] = len(content)


	return response
