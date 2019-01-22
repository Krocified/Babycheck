# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:01:20 2019

@author: OWNER
"""

# Length avg is 50 cm
# Head Circ avg is half the length +10, so 35 cm
# Weight avg is 2.5-3.5 kg

# index for baby
# 0 = low weight baby
# 1 = average baby
# 2 = super baby

# Baby Length, Head Circumference, Weight 
from sklearn import tree
measurements = [
        [50, 35, 3], 
        [45, 32.5, 2.8], 
        [49.1, 34, 2.9], 
        [43, 32, 2.7], 
        [44.4, 33, 2.5],
        [53, 37, 3.5],
        [41, 30, 2.6],
        [54.1, 37, 4],
        [48, 34, 3.1],
        [42, 31, 2.7],
        [35.3, 28, 2.4],
        [31, 24, 2.2],
        [20, 20, 1.9],
        [29.5, 25, 2.5],
        [30, 25, 2],
        [40.1, 30, 2.6],
        [31, 25, 2.1],
        [38, 29, 1.8],
        [37, 28, 2.5],
        [25, 22, 1.6],
        [55, 38, 4],
        [53, 36, 3.8],
        [56, 38, 4.1],
        [60, 40, 4.8],
        [57, 39, 4.7],
        [55, 36, 3.8],
        [64, 42, 5],
        [59, 40, 4.7],
        [55, 37, 3.9],
        [62, 41, 4.9]
        ]

values = [1,1,1,1,1,1,1,1,1,1,
          0,0,0,0,0,0,0,0,0,0,
          2,2,2,2,2,2,2,2,2,2]

clf = tree.DecisionTreeClassifier()
clf.fit(measurements, values)

length = input("Please enter baby's length (in cm): ")
type(length)

head = input("Please enter baby's head circumference (in cm): ")
type(head)

weight = input("Please enter baby's weight (in kg): ")
type(weight)

baby = clf.predict([[length, head, weight]])

if baby == 0:
    print("Baby health is lower than average")
    
if baby == 1:
    print("Baby is healthy")
        
if baby == 2:
    print("Baby is a super baby")


#To Generate Tree with GraphViz
"""
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())
"""



