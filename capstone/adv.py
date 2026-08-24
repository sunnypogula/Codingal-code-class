from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
from matplotlib import pyplot
X,Y = make_blobs(n_samples=1000,centers=2,random_state=1)
print(X.shape,Y.shape)
counter = Counter(Y)
print(counter)
for i in range(10):
    print(X[i],Y[i])
for label, _ in counter.items():
    row_ix = where(Y == label)[0]
    pyplot.scatter(X[row_ix,0],X[row_ix,1],label=str)
pyplot.legend()
pyplot.show()