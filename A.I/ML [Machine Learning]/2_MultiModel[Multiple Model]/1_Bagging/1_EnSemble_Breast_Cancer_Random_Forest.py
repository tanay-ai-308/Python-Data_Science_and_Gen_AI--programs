import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------------------------
# step 1- Load the Data Set
# -----------------------------------------------
df = pd.read_csv(r"D:\Desktop\marvellous\Python Batch\DataSet\breast_cancer.csv")
print("\nShape of Data set - ",df.shape)
print("\nRecords :- ")
print(df.head())


# -----------------------------------------------
# step 2- Separte Features and labels
# -----------------------------------------------
X = df.drop("target",axis=1)
Y = df["target"]

print("\nX Shape - ",X.shape)
print("\nY Shape - ",Y.shape)

# -----------------------------------------------
# step 3- Split Data Set for training and testing
# -----------------------------------------------

X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2,random_state=42)

# -----------------------------------------------
# step 4- Scale the feature
# -----------------------------------------------
Scaler = StandardScaler()
X_Train = Scaler.fit_transform(X_Train)
X_Test = Scaler.fit_transform(X_Test)


# -----------------------------------------------
# step 5- Create the model
# -----------------------------------------------
Model = RandomForestClassifier(n_estimators=10,random_state=42)

# -----------------------------------------------
# step 6- Train the model
# -----------------------------------------------
Model = Model.fit(X_Train,Y_Train)

# -----------------------------------------------
# step 7- Test the Model
# -----------------------------------------------
Y_Pred = Model.predict(X_Test)

# -----------------------------------------------
# step 8- Evaluate the Model
# -----------------------------------------------
print("\nAcurracy - ",accuracy_score(Y_Test,Y_Pred)*100)
print("\nConfustion Matrix - ",confusion_matrix(Y_Test,Y_Pred))