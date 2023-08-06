#import all library files from lib.py
from lib import *
# Reading data from train.csv
# the data is freely available on kaggle

data=pd.read_csv("data/emnist-balanced-train.csv")
label=data.iloc[:,0]
def all_same(items):
  return len(set(items)) == 1

# Extract feature columns
feature_cols = list(data.columns[1:])

# Separate the data into feature data and target data (X and y, respectively)
#X = data[feature_cols]
X=data.iloc[:,1:]
y = label

# Apply PCA by fitting the data with only 60 dimensions
pca = PCA(n_components=60).fit(X)
# Transform the data using the PCA fit above
X = pca.transform(X)
y = y.values
variance=pca.explained_variance_ratio_
print(sum(variance))

# Shuffle and split the dataset into the number of training and testing points above
sss = model_selection.StratifiedShuffleSplit(n_splits=10, test_size=0.4, random_state=42)
for train_index, test_index in sss.split(X,y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]


#Prediction can de done using this function
def predict_output(X_test=X_test,y_test=y_test,X_train=X_train,y_train=y_train):
    # Fit a KNN classifier on the training set
    knn_clf = KNeighborsClassifier(n_neighbors=3, p=2)
    knn_clf.fit(X_train, y_train)
    # X_test=pca.transform(X_test)
    # Initialize the array of predicted labels
    y_pred = np.empty(len(y_test), dtype=np.int)
    start = time()

    # Find the nearest neighbors indices for each sample in the test set
    kneighbors = knn_clf.kneighbors(X_test, return_distance=False)

    # For each set of neighbors indices
    for idx, indices in enumerate(kneighbors):
        # Find the actual training samples & their labels
        neighbors = [X_train[i] for i in indices]
        neighbors_labels = [y_train[i] for i in indices]

        # if all labels are the same, use it as the prediction
        if all_same(neighbors_labels):
            y_pred[idx] = neighbors_labels[0]
        else:
            # else fit a SVM classifier using the neighbors, and label the test samples
            svm_clf = svm.SVC(C=0.5, kernel='rbf', decision_function_shape='ovo', random_state=42)
            svm_clf.fit(neighbors, neighbors_labels)
            label = svm_clf.predict(X_test[idx].reshape(1, -1))

            y_pred[idx] = label
    end = time()

    print("Actual output:{}".format(y_test))
    print("Predicted output:{}".format(y_pred))
    print(accuracy_score(y_test, y_pred))
    print("Made predictions in {:.4f} seconds.".format(end - start))
    return y_pred
predict_output(X_test,y_test,X_train,y_train)

