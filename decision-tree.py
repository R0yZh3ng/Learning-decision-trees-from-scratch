# decison trees are a flow chart based ml algorithm that are used for both classification and regression tasks.

# to first understand how decision trees work, we must first understand the baseconcepts

#impurity: the disorder or randomness of the data within a certain node of the decision tree, indicating how mixed the different classes of data are at that node

# --> there are a few different ways of measuring impurity, two common ways are with *entropy* and *Gini Index/Gini Impurity*

# Entropy, in this case, represents how much information is needed to accurately describe the sample.
# thus is a data sample is homogenous/contains all similar elements, the entropy is 0, if there is an equal ratio representation of different data classes then the entropy is 1, the maximum.
# to put this mathematically, Entropy = - /sum_{i = 1}^{n} P.i * log(P.i)
#P.i in this scenario means the portion of the sample that belongs to the class n for a particular node.

# The Gini-index, is a measurment of inequality in a data sample, again with a value of 0 being that the sample is homogenous and all elements are simialr, and the value of 1 means maximum inequaity between the elements of the sample.
# to put this mathematically, Gini-index = 1 - /sum_{i = 1}^{n} (P.i)^2
#P.1 in this case remains the portion of the sample that belongs to the class n for a particular node.



#### decision tree algorithms are tree structs where the nodes are attributes, the branches are the decisions(rules), and the leaf nodes representing results (discrete and continous)

## The CART(classification And Regression Tree) is a decision tree model that 
## -----> generate both classification and regression trees
## -----> uses the Gini-index as a metric/cost function to evalute split in feature selection in the case of classification trees - used commonly in binary classifications
## -----> uses the least-square as a metric to select features in the case of a regression tree

# lets start with calculating the Gini-index for all the nominal features of the data sample (features with no particular order or ranking). The lowest of the Gini-index of the nominal features is set as the root node. 
# Then, compute the Gini-index of the remaining nominal features for all the different classes of the current node. the lowest of the Gini-index out of the remaining nominal features gets set as a node.
# the process repeats until all nominal features have been assigned to a node, then, generate the leaf nodes for that specific sequence of path down the tree.
#another way to generate a leaf node is when the Gini-index of all nominal features evaluate to zero.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


training_data = pd.read_csv('datasets/drug200.csv')
features = training_data.iloc[1, :].values # takes the different nominal features that are going to be used to calculate the gini-index and puts them in a numpy array
decisions = training_data.iloc[:, -1].values # takes the last column of the dataset for all the different results
decision_classes = np.unique(decisions) # grabs the unique classes in the results


print(training_data) #test if the training_data is correctly loaded in

print(decision_classes) #test if the decision classes are correctly identified


def gini_index(nominal_feature):
    unique_elements = np.unique(training_data[training_data[feature] == nominal_feature])

    for elements in unique_elements: 
        feature_subset = training_data[training_data[feature] == elements]
         
        
