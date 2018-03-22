from django import forms
from .models import parameter,Document


class DataForm(forms.ModelForm):
	radius_mean=forms.FloatField(label='Mean Radius')
	texture_mean=forms.FloatField(label='Mean Texture')
	perimeter_mean=forms.FloatField(label='Mean Perimeter')
	area_mean=forms.FloatField(label='Mean Area')
	smoothness_mean=forms.FloatField(label='Smoothness')
	compactness_mean=forms.FloatField(label='Mean Compactness')
	concavity_mean=forms.FloatField(label='Mean Concavity')
	concave_points_mean=forms.FloatField(label='Mean Concave Points')
	symmetry_mean=forms.FloatField(label='Mean Symmetry')
	fractal_dimension_mean=forms.FloatField(label='Mean Fractal Dimension')
	radius_se=forms.FloatField(label='SE Radius')
	texture_se=forms.FloatField(label='SE Texture')
	perimeter_se=forms.FloatField(label='SE Perimeter')
	area_se=forms.FloatField(label='SE Area')
	smoothness_se=forms.FloatField(label='Smoothness')
	compactness_se=forms.FloatField(label='SE Compactness')
	concavity_se=forms.FloatField(label='SE Concavity')
	concave_points_se=forms.FloatField(label='SE Concave Points')
	symmetry_se=forms.FloatField(label='SE Symmetry')
	fractal_dimension_se=forms.FloatField(label='SE Fractal Dimension')
	radius_worst=forms.FloatField(label='Worst Radius')
	texture_worst=forms.FloatField(label='Worst Texture')
	perimeter_worst=forms.FloatField(label='Worst Perimeter')
	area_worst=forms.FloatField(label='Worst Area')
	smoothness_worst=forms.FloatField(label='Smoothness')
	compactness_worst=forms.FloatField(label='Worst Compactness')
	concavity_worst=forms.FloatField(label='Worst Concavity')
	concave_points_worst=forms.FloatField(label='Worst Concave Points')
	symmetry_worst=forms.FloatField(label='Worst Symmetry')
	fractal_dimension_worst=forms.FloatField(label='Worst Fractal Dimension')

	class Meta:
		model = parameter
		fields = ('radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','concave_points_mean','symmetry_mean','fractal_dimension_mean','radius_se','texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se','concave_points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst','concave_points_worst','symmetry_worst','fractal_dimension_worst')

class DocumentForm(forms.ModelForm):
	document=forms.FileField(label ='Choose file: ')
	class Meta:
		model=Document
		fields=('document',)