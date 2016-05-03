
# coding: utf-8

# ## knn algo using the digit recognition dataset

# ### (using the digits dataset from sklearn)

# In[14]:

# load the digits data
from sklearn import datasets

digits = datasets.load_digits()


# In[15]:

# show image pixels as an array
print "Each image is an 8x8 array of pixels:"
print digits.images[0]


# In[8]:

# plot an image
import pylab as pl

pl.imshow(digits.images[0], cmap=pl.cm.gray_r, interpolation='nearest')


# In[12]:

# display the label (as a scalar) and features (as a vector)
print "This image has been labeled as a:" , digits.target[0]
print "Its 64 features (pixel values) are:"
print digits.data[0]


# In[13]:

pl.imshow(digits.images[1], cmap=pl.cm.gray_r, interpolation='nearest')

print "This image has been labeled as a:" , digits.target[1]
print "Its 64 features (pixel values) are:"
print digits.data[1]


# In[18]:

# evaluate a k-nearest neighbor model with different number of neighbors
from sklearn import neighbors
import numpy as np

# split the data into 80% for training and 20% for testing
num_train = int(digits.target.size * 0.8)

print num_train
print digits.target.size


# In[20]:

train_data, train_target = digits.data[:num_train], digits.target[:num_train]
test_data, test_target = digits.data[num_train:], digits.target[num_train:]

# fit for k=1 to k=10
num_neighbors = range(1,11)

accuracyTrain = []
accuracyTest = []

for k in num_neighbors:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_data, train_target)

    accTrain = knn.score(train_data, train_target)
    accTest = knn.score(test_data, test_target)

    print "With k = %d neighbors, our train accuracy is %.2f%%" % (k, accTrain*100)
    print "With k = %d neighbors, our test accuracy is %.2f%%" % (k, accTest*100)

    accuracyTrain.append(accTrain)
    accuracyTest.append(accTest)


# In[21]:

# plot the generalization error with increasing number of neighbors
import matplotlib.pyplot as plt

plt.plot(num_neighbors, accuracyTrain, label='Train.')
plt.plot(num_neighbors, accuracyTest, label='Test.')
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


# In[24]:

print accuracyTest
print num_neighbors

print np.argmax(accuracyTest)


# In[26]:

# evaluate the model with best generalization error
from sklearn.metrics import confusion_matrix, classification_report

# find the best value of k
k = num_neighbors[np.argmax(accuracyTest)]


# In[25]:

# refit the model
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(digits.data[:num_train], digits.target[:num_train])

predicted = knn.predict(digits.data[num_train:])

print classification_report(digits.target[num_train:], predicted)

confmat = confusion_matrix(digits.target[num_train:], predicted)
print confmat


# In[ ]:



