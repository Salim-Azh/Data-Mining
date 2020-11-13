import numpy as np
import pandas as pd
import sklearn.datasets as skd
import sklearn.metrics as skme
import sklearn.model_selection as skmd
import sklearn.tree as skt
import graphviz
import matplotlib as mp
import apyori as apy
import sklearn.neighbors as skne

def sep():
    print('*'*50)

def load_iris():
    #Loading
    print("Loading iris dataset ...")
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    return pd.read_csv(url, names=names)

def load_store_data():
    print("Loading store dataset ...")
    return pd.read_csv("./store_data.csv")

def features_visualization(df, grouby_arg="", head=5, groupby = False):
    print(df.shape)
    print(df.head(head))
    print(df.describe())
    if(groupby):
        print(df.groupby(grouby_arg).size())

def decision_tree_classification(feat_train,lbl_train,feat_validation,\
    lbl_validation):
    # Decision tree classifier creation
    clf = skt.DecisionTreeClassifier()
    clf.fit(feat_train,lbl_train) # find pattern in the training data
    clf_predictions = clf.predict(feat_validation) # predictions

    # Evaluate predictions
    print("**Decision tree prediction's evaluation**")
    print("Decision tree classifier prediction accuracy:",\
        skme.accuracy_score(lbl_validation, clf_predictions))
    # Confusion matrix
    print("Iris confusion matrix with decision tree predictions:")
    print(skme.confusion_matrix(lbl_validation, clf_predictions))
    print("Classification report:")
    print(skme.classification_report(lbl_validation, clf_predictions))
    
    # Visualization : Decision tree
    skt.plot_tree(clf) 
    mp.pyplot.show()

def knn_classification(feat_train,lbl_train,feat_validation,\
    lbl_validation):
    # Knn classifier creation with k = 10 
    knn = skne.KNeighborsClassifier(n_neighbors=10)
    # Train the model using the training sets
    knn.fit(feat_train, lbl_train)
    # Predict the response for test dataset
    knn_predictions = knn.predict(feat_validation)

    #Evaluate predictions
    print("**KNN prediction's evaluation for k=10**")
    print("Accuracy:",skme.accuracy_score(lbl_validation,\
        knn_predictions))

def main():
    sep()
    df = load_iris()
    features_visualization(df = df,grouby_arg="class", groupby=True)
    sep()

    ### Splitting data #################################################
    test_proportion = 0.2
    data = df.to_numpy() # convert the dataframe into a numpy array
    #slice the table to dissociate features and labels
    features, labels = data[:, :-1], data[:, -1]
    
    #training data in feat_train and lbl_train
    #validation data in feat_validation and lbl_validation
    feat_train, feat_validation, lbl_train, lbl_validation = \
        skmd.train_test_split(features, 
                            labels, 
                            test_size=test_proportion, # 80% training and 20% test
                            random_state=1)
    
    print(f"Data splitted with {(1-test_proportion)*100}% training and {test_proportion*100}% test\n")
    ### End Splitting data #############################################

    decision_tree_classification(feat_train,lbl_train,feat_validation,\
        lbl_validation)

    knn_classification(feat_train,lbl_train,feat_validation,lbl_validation)
   
    ### Association rules with store dataset ###########################
    sep()
    df2 = load_store_data()
    features_visualization(df2)
    sep()

    # apriori takes the data set as a two dimension list
    # each row is the list containing the data for one row
    data_list = []   
    for row in range(0, 1000): # store data contains 7500 rows 
                               # but we take only the first 1000 
                               # to make the processing faster
        data_list.append([str(df2.values[row,column]) for column in range(0, 20)])

    algo = apy.apriori(data_list, 
                    min_support=0.03,
                    min_confidence=0.2,
                    min_lift=2,
                    min_length=2)
    results = list(algo)
    print(len(results), "association rules founded")
    if(len(results)>5):
        for i in range(0,5):
            print(f"Association rule No. {i+1} is: {results[i]}")
            print('-'*25)
    else:
        for i in range(0,len(results)):
            print(f"Association rule No. {i+1} is: {results[i]}")
            print('-'*25)
    ### End Association rules with store dataset #######################
if __name__ == "__main__":
    main()
