# importing required modules
import os
import csv
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.views import login
from django.conf import settings
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import io
import csv
import ast
from .userform import DataForm,DocumentForm
from .p2 import mlp,mlp_csv
from django.views.generic import View
from .models import parameter
from django.template.loader import get_template
from .graph import graph
f1=io.BytesIO()

class UserHome(TemplateView):
	template_name = 'input.html'

	def get(self, request):
		form1=DataForm()
		return render(request, self.template_name, {'form1' : form1})

	def post(self, request):
		form1 = DataForm(request.POST)
		if form1.is_valid():
			form1.save()
			radius_mean=form1.cleaned_data['radius_mean']
			texture_mean=form1.cleaned_data['texture_mean']
			perimeter_mean=form1.cleaned_data['perimeter_mean']
			area_mean=form1.cleaned_data['area_mean']
			smoothness_mean=form1.cleaned_data['smoothness_mean']
			compactness_mean=form1.cleaned_data['compactness_mean']
			concavity_mean=form1.cleaned_data['concavity_mean']
			concave_points_mean=form1.cleaned_data['concave_points_mean']
			symmetry_mean=form1.cleaned_data['symmetry_mean']
			fractal_dimension_mean=form1.cleaned_data['fractal_dimension_mean']
			radius_se=form1.cleaned_data['radius_se']
			texture_se=form1.cleaned_data['texture_se']
			perimeter_se=form1.cleaned_data['perimeter_se']
			area_se=form1.cleaned_data['area_se']
			smoothness_se=form1.cleaned_data['smoothness_se']
			compactness_se=form1.cleaned_data['compactness_se']
			concavity_se=form1.cleaned_data['concavity_se']
			concave_points_se=form1.cleaned_data['concave_points_se']
			symmetry_se=form1.cleaned_data['symmetry_se']
			fractal_dimension_se=form1.cleaned_data['fractal_dimension_se']
			radius_worst=form1.cleaned_data['radius_worst']
			texture_worst=form1.cleaned_data['texture_worst']
			perimeter_worst=form1.cleaned_data['perimeter_worst']
			area_worst=form1.cleaned_data['area_worst']
			smoothness_worst=form1.cleaned_data['smoothness_worst']
			compactness_worst=form1.cleaned_data['compactness_worst']
			concavity_worst=form1.cleaned_data['concavity_worst']
			concave_points_worst=form1.cleaned_data['concave_points_worst']
			symmetry_worst=form1.cleaned_data['symmetry_worst']
			fractal_dimension_worst=form1.cleaned_data['fractal_dimension_worst']	
			
			pred = mlp(radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst)
			args = {'form1' : form1, 'pred' : pred}
			form1=DataForm()
			
		return render(request,self.template_name,args)		

#for training:
def model_form_train(request):
	if request.method == 'POST':
		form2=DocumentForm(request.POST, request.FILES)
		if form2.is_valid():
			form2.save()
			csv_file=request.FILES['document']
			if not csv_file.name.endswith('.csv'):
				messages.error(request,'File is not csv type')
				return render(request, "training.html" ,{'form2' : form2})
			file=csv_file.name
			
			accuracy = mlp_csv(file)
			accuracy = accuracy*100
			return render(request, "training.html" ,{'form2' : form2, 'accuracy' : accuracy})
	else:
		form2=DocumentForm(request.POST, request.FILES)
		return render(request, "training.html" ,{'form2' : form2})

def get_image_rfc(request):
	f=open('finalized_model_mlp.sav', 'rb')
	cl_mlp=pickle.load(f)
	accuracy_mlp=pickle.load(f)
	a=pickle.load(f)

	labels = 'Right Prediction', 'Wrong Prediction'
	plt.rcParams['font.size'] = 7.0
	sizes = [a[0][0],a[0][1]]
	colors = ['blue', 'red']
	explode = (0, 0)  # explode 1st slice
	ax=plt.subplot(131)
	ax.set_title('MLP:          Good Fistulae')
	ttl=ax.title
	ttl.set_position([.2,0.9])
	plt.axis('equal')
	plt.rcParams['font.size'] = 5.0
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	        autopct='%1.0f%%', shadow=False, startangle=150)

	labels = 'Right Prediction', 'Wrong Prediction'
	plt.rcParams['font.size'] = 7.0
	sizes = [a[1][1],a[1][0]]
	colors = ['blue', 'red']
	explode = (0, 0)  # explode 1st slice
	ax=plt.subplot(132)
	ax.set_title('Bad Fistulae')
	ttl=ax.title
	ttl.set_position([.4,0.9])
	plt.axis('equal')
	plt.rcParams['font.size'] = 5.0
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	        autopct='%1.0f%%', shadow=False, startangle=180)

	labels = 'Accuracy', ''
	plt.rcParams['font.size'] = 7.0
	sizes = [accuracy_mlp,1-accuracy_mlp]
	colors = ['blue', 'red']
	explode = (0, 0)  # explode 1st slice
	ax=plt.subplot(133)
	plt.axis('equal')
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	        autopct='%1.0f%%', shadow=False, startangle=150)
	plt.savefig(f1, format='png')
	
    	#plt.show()
	return HttpResponse(f1.getvalue(), content_type='image/png')
    
def get_image(request):
	r=graph('finalized_model_mlp.sav')
	return r    
    
    