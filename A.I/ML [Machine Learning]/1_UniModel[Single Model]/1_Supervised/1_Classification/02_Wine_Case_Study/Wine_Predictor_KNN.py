import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler

def main():
    MarvellousClassifer("WinePredictor.csv")

def MarvellousClassifer(DataPath):
    Border1 = "=:="*30
    Border2 = "- -"*30

#=============================================
#   - Step1 Load the dataset from csv file
#=============================================
    
    print()
    print(Border1)
    print(" - Step1 Load the dataset from csv file")
    print(Border2)
    print()

    DataFrame = pd.read_csv(DataPath)

    print("Some Entries from dataset is :- ")
    print(DataFrame.head())
    print()

#=============================================
#   - Step2 Clean the Data sets.
#=============================================
    
    print()
    print(Border1)
    print(" - Step2 Clean the Data sets.")
    print(Border2)
    print()

    DataFrame.dropna(inplace=True)

    print("Shape of dataset :- ",DataFrame.shape)
    print("Total Records :- ",DataFrame.shape[0])
    print("Total Columns :- ",DataFrame.shape[1])
    print()

#=============================================
#   - Step3 Separate Independent and Dependent Variables.
#=============================================
    
    print()
    print(Border1)
    print("- Step3 Separate Independent and Dependent Variables.")
    print(Border2)
    print()

    X = DataFrame.drop(columns = ["Class"])
    Y = DataFrame["Class"]

    print("Shape of X :-",X.shape)
    print("Shape of Y :-",Y.shape)

    print(Border2)
    print("Input Columns : ",X.columns.tolist())
    print("Output Column : Class")
    print()

#=============================================
#    - Step4 Split the DataSet.
#=============================================
    
    print()
    print(Border1)
    print(" - Step4 Split the DataSet.")
    print(Border2)
    print()

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print(Border2)
    print("Details of training and testing data.")

    print("Shape of X_Train :- ",X_Train.shape)
    print("Shape of X_Test :- ",X_Test.shape)
    print("Shape of Y_Train :- ",Y_Train.shape)
    print("Shape of Y_Test :- ",Y_Test.shape)
    print(Border2)
    print()

#=============================================
#   - Step5 Feature Scaling.
#=============================================
    
    print()
    print(Border1)
    print(" - Step5 Feature Scaling.")
    print(Border2)
    print()

    Scaler = StandardScaler()

    X_Train_Scaled = Scaler.fit_transform(X_Train)
    X_Test_Scaled = Scaler.transform(X_Test)

    print("Feature Scaling Done.")
    print(Border2)
    print()

#=============================================
#   - Step6 Hyper parameter tuning.
#=============================================
    
    print()
    print(Border1)
    print(" - Step6 Hyper parameter tuning.")
    print(Border2)
    print()

    Accuracy = []
    K_Value = range(1,21)

    for k in K_Value:
        Model = KNeighborsClassifier(n_neighbors=k)
        Model = Model.fit(X_Train_Scaled,Y_Train)
        Y_Pred = Model.predict(X_Test_Scaled)
        acc = accuracy_score(Y_Test,Y_Pred)
        Accuracy.append(acc*100)

    print("Acuracy Report :- ")
    for i in Accuracy:
        print(i)

    print(Border2)
    print("Graphical Representation :- ")

    plt.figure(figsize=(8,5))
    plt.plot(K_Value,Accuracy,marker = 'o')
    plt.title("K_Values V.S Accuracy")
    plt.xlabel("K_Value")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_Value))
    plt.show()
    print()
    print(Border2)

if __name__ == "__main__" :
    main()