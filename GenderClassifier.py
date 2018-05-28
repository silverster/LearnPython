#Gender Classifier

from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

#[height,weight,shoe size]

X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
	[166,65,40],[190,90,47],[175,64,39],[177,70,40],
	[159,55,36],[171,75,42],[181,85,43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male',
 'female', 'female',
     'female', 'male', 'male']

tree_clf = tree.DecisionTreeClassifier()
tree_clf.fit(X,Y)
tree_prediction = tree_clf.predict([[190,70,43]])
print('Prediction using DecisionTreeClassifier ',
	tree_prediction)

lr_clf = LogisticRegression()
lr_clf.fit(X,Y)
lr_prediction = lr_clf.predict([[190,70,43]])
print('Prediction using LogisticRegression ',
	lr_prediction)


knn_clf = KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X,Y)
knn_prediction = knn_clf.predict([[190,70,43]])
print('Prediction using KNeighborsClassifier ', 
	knn_prediction)