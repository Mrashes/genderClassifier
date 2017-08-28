from sklearn import tree
    
#[height, weight, shoe size]
X = [[181, 80, 44], [177,70,43], [160,60,38], 
    [154,45,37], [166,65,40], [190,90,47], 
    [175,64,39], [177,70,40], [159, 59,37], 
    [171,75,42], [158, 62,38], [181,85,43]]

#gender
Y = ['male', 'female', 'female', 
    'female', 'male', 'male', 
    'female', 'male', 'female',
    'male', 'female', 'male']

#getting classifier
clf = tree.DecisionTreeClassifier()

#fitting to model
clf = clf.fit(X,Y)

#predict based on data given
prediction = clf.predict([ [190,73,40]])

print (prediction)