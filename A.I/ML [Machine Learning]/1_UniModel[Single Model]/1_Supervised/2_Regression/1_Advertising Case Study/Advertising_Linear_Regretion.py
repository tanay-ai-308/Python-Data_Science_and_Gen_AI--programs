import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    MarvellousRegretion("Advertising.csv")

def MarvellousRegretion(DataPath):

    # - Load the Data
    Border = "-"*40
    print(Border)
    print(" - Load the Data")
    print(Border)

    df = pd.read_csv(DataPath)
    print(df.head())

    print()
    # - Remove unwanted columns(EDA)
    print(Border)
    print(" - Step2 - Remove unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    print()
# - step3 - Check Missing Values
    print(Border)
    print("- Step3 - Check Missing Values")
    print(Border)

    print("Total missing values = ")
    print(df.isnull().sum())

    print()
# - step4 - Statistical Summary
    print(Border)
    print("- step4 - Statistical Summary")
    print(Border)

    print(df.describe())

    print()
# - step5 - Correlation
    print(Border)
    print("- step5 - Correlation")
    print(Border)

    print(df.corr())

    print()
# - step6 - Separate Independent and Dependent Variables
    print(Border)
    print("- step6 - Separate Independent and Dependent Variables")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent Variable")
    print(X.head())

    print("Dependent Variable")
    print(Y.head())

    print()
# - step7 - Splite the DataSet
    print(Border)
    print("- step7 - Splite the DataSet")
    print(Border)

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data : ",X_Train.shape)
    print("Testing Data : ",X_Test.shape)

    print()
# - step8 - Create and train the model
    print(Border)
    print("- step8 - Create and train the model")
    print(Border)

    Model = LinearRegression()

    Model = Model.fit(X_Train,Y_Train)
    print("Model Train successfully")

    print()
# - step9 - test the Model
    print(Border)
    print("- step9 - test the Model")
    print(Border)

    Y_Pred = Model.predict(X_Test)

    print("Expected Answer : ")
    print(Y_Test[:3])

    
    print("Predicted Answer : ")
    print(Y_Pred[:3])

    print()
# - step10 - Evaluate the Model
    print(Border)
    print("- step10 - Evaluate the Model")
    print(Border)

    Mse = mean_squared_error(Y_Test,Y_Pred)
    R_Mse = np.sqrt(Mse)

    R2 = r2_score(Y_Test,Y_Pred)

    print("Mse (Mean Square Error) : ",Mse)
    print("RMse (Root Mean Square Error) : ",R_Mse)
    print(" r2 : ",R2)

    print()
# - step11 - Display Coefficient (m)
    print(Border)
    print("- step11 - Display Coefficient (m)")
    print(Border)

    print("\nT.V Coefficient : ",Model.coef_[0])
    print("Radio Coefficient : ",Model.coef_[1])
    print("Newspaper Coefficient : ",Model.coef_[2])

    print("\nIntercept (c) : ",Model.intercept_)
if __name__ == "__main__" :
    main()