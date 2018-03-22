import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import io
from django.http import HttpResponse


def graph(file):
	f=open(file, 'rb')
	cl_mlp=pickle.load(f)
	accuracy_mlp=pickle.load(f)
	a=pickle.load(f)
	# Data to plot
	labels = 'Right', 'Wrong'
	sizes = [a[1][1],a[1][0]]
	colors = ['#ff0080', 'pink']
	explode = (0, 0)  # explode 1st slice
 
		# Plot
	
	ax=plt.subplot(131)
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.0f%%', shadow=False, startangle=40)
	plt.axis('equal')
	ax.set_title('Malignant Tumour')
	labels = 'Right', 'Wrong'
	sizes = [a[0][0],a[0][1]]
	colors = ['#ff0080', 'pink']
	explode = (0, 0)  # explode 1st slice
	# Plot
	ax1=plt.subplot(132)
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.0f%%', shadow=False, startangle=40)
	plt.axis('equal')
	ax1.set_title('Benign Tumour')
	labels = 'Right', 'Wrong'
	sizes = [accuracy_mlp,1-accuracy_mlp]
	colors = ['#ff0080', 'pink']
	explode = (0, 0)  # explode 1st slice
	# Plot
	ax2=plt.subplot(133)
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%0.4f%%', shadow=False, startangle=40)
	plt.axis('equal')
	ax2.set_title('Total Accuracy')
	f1 = io.BytesIO()
	plt.savefig(f1, format='png')
	
    	#plt.show()
	return HttpResponse(f1.getvalue(), content_type='image/png')