from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
iris = load_iris()
#create test train
test_idx = [0, 50, 100]


## Training DATA ##
#remove test idx from the original train [target]
train_target = np.delete(iris.target, test_idx)
#remove test idx from the original train [data]
train_data = np.delete(iris.data, test_idx, axis=0)

## Testing Data ##

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print iris.feature_names
print iris.target_names
print test_data
print clf.predict(test_data)

from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True,
                     rounded=True,
                     impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")