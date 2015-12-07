#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###


print features_train.shape

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(min_samples_split=40)


t_training = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t_training, 3), "s"


t_testing = time()
pred = clf.predict(features_test)
print "testing time:", round(time()-t_testing, 3), "s"






from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print "accuracy_score",acc

#########################################################


