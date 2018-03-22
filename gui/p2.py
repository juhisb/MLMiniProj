# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier
from django.conf import settings
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

import pickle
import os
#v1=
#v2=
BASE_DIR=getattr(settings,"MEDIA_ROOT",None)
def mlp(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30):
	clf1=pickle.load(open("finalized_model_mlp.sav", 'rb'))
	temp=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30]
	temp = np.array(temp).reshape((1, -1))
	pred = clf1.predict(temp)
	if pred=='B':
		pred = 'Benign Tumor'
	else:
		pred = 'Malignant Tumor'
	return pred

def mlp_csv(csv_file):
	
	df = pd.read_csv(os.path.join(BASE_DIR,"documents",csv_file), header = 0)

	X = np.array(df.drop(['diagnosis'],1))
	y = np.array(df['diagnosis'])

	X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

	# the classifier
	clf1 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(45,), random_state=1)

	# train
	clf1.fit(X_train, y_train)

	# predict
	pred = clf1.predict(X_test)
	# print(y_test)
	# print(pred)

	accuracy = accuracy_score(pred, y_test)

	# print ('\naccuracy = {0}'.format(accuracy))

	filename='finalized_model_mlp.sav'

	pickle.dump(clf1, open(filename, 'wb'))
	pickle.dump(accuracy, open(filename, 'wb'))
	for count in range(0,10):
		# print(count)
		X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

		# the classifier
		clf1 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(45,), random_state=1)

		# train
		clf1.fit(X_train, y_train)

		# predict
		pred = clf1.predict(X_test)
		# print(y_test)
		# print(pred)

		accuracy1 = accuracy_score(pred, y_test)
		f=open(filename, 'wb')
		if accuracy1>accuracy:
			accuracy=accuracy1
			clf2=clf1
			a = [[0,0], [0,0]] 
			a=confusion_matrix(y_test, pred, labels=None, sample_weight=None)
		
	# print ('\n Final accuracy = {0}'.format(accuracy))
	# print("Confusion matrix is:")
	# print(a)
	pickle.dump(clf2, f)
	pickle.dump(accuracy, f)
	pickle.dump(a, f)
	# print ("\nTotal time taken:", round(time()-t1, 3), "s")
	return(accuracy)   