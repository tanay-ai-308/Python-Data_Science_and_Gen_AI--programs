import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)

Border = "-="*40

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 1 - Load Data set
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 1 - Load Data set")
print(Border)
print()

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print()
print("Dataset Loaded Successfully.\n")
print("Initial entries in dataset are :- ")
print(df.head())

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 2 - Data Analysis (EDA)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 2 - Data Analysis (EDA)")
print(Border)
print()

print("Shape of Dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("\nMissing Values per column : ")
print(df.isnull().sum())

print("\nClass Distribution(species count) :- ")
print(df["species"].value_counts())

print("\nStatistical report of data set :")
print(df.describe())

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 3 - Decided Independent and dependent variable
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 3 - Decided Independent and dependent variable")
print(Border)
print()

# X : Independent Variable/ Features
# Y : Dependent Variable/ Lables

Feature_Columns = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]

X = df[Feature_Columns]
Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 4 - Visualization of Dataset
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 4 - Visualization of Dataset")
print(Border)
print()

# Scatter Plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris Case Study")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 5 - Splite the data set for training and testing
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 5 - Splite the data set for training and testing")
print(Border)
print()

X_Train,X_test, Y_Train,Y_test = train_test_split(X,Y,test_size=0.5, random_state=42)

print("Dataset spliting activity done.")

print("\nX = ",X.shape)                 #150,4
print("Y = ",Y.shape)                   #150,0

print("\nX_Train = ",X_Train.shape)     #75,4
print("X_test = ",X_test.shape)         #75,4

print("\nY_Train = ",Y_Train.shape)     #75,0
print("Y_test = ",Y_test.shape)         #75,0

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 6 - Build the Model
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 6 - Build the Model")
print(Border)
print()

Model = DecisionTreeClassifier(max_depth=5)

print("Model gets created Sccessfully")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 7 - Train Model
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 7 - Train Model")
print(Border)
print()

Model = Model.fit(X_Train,Y_Train)

print("Model train successfully")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 8 - Test Model
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print(" - Step 8 - Test Model")
print(Border)
print()

Y_Pred = Model.predict(X_test)

print("Model testing done.")

print("Expected answer : ")
print(Y_test)
print("Predicted answer : ")
print(Y_Pred)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Step 9 - Evaluate the model performance
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print()
print(Border)
print("- Step 9 - Evaluate the model performance")
print(Border)
print()

Accurracy = accuracy_score(Y_test,Y_Pred)
print("Accuracy of model is :- ",Accurracy*100)

print("Confusion matrix")
cm = confusion_matrix(Y_test,Y_Pred)
print(cm)

print("Classification report :- ")
print(classification_report(Y_test,Y_Pred))