from sklearn import tree
# [weight,texture( 1=>bumpy, 2=>smooth)]
feature = [[140, 1], [130, 1], [150, 0], [170, 0]]
label = ['orange', 'orange', 'apple', 'apple']
clf = tree.DecisionTreeClassifier()
clf.fit(feature, label)
print(clf.predict([130, 1]))

