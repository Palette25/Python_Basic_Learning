#--------------------------------------------My  first classifier-----------------------------------------------#
from scipy.spatial import distance

def enu(a, b):
    return distance.euclidean(a, b)

class My_Palette():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        pre = []
        for row in x_test:
            label = self.closest(row)
            pre.append(label)
        return pre

    def closest(self, row):
        best_dist = enu(row, self.x_train[0])
        best_index = 0
        for i in range(1, len(self.x_train)):
            dist = enu(row, self.x_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i

        return self.y_train[best_index]

from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)

my_classifier = My_Palette()

my_classifier.fit(x_train, y_train)

pre = my_classifier.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pre))
