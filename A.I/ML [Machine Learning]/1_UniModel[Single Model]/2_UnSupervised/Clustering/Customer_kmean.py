import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    # step 1- load data
    Banner(1,"Load DataSet")
    df = pd.read_csv(r"D:\Desktop\marvellous\Python Batch\DataSet\Mall_Customers.csv")

    print("\nData from csv :- ")
    print(df.head())
    print("\nMissing Values")
    print(df.isnull().sum())

   # Step 2- Feature selection
    Banner(2,"Feature selection")
    X = df[["AnnualIncome","SpendingScore"]]

    print("\nSelected Features :- ")
    print(X.head())


    # Step 3- Scale the Data
    Banner(3,"Scale the Data")

    Scaler = StandardScaler()

    X_Scale = Scaler.fit_transform(X)

    print("\nScaled Data")
    print(X_Scale[:5])
 

    # Step 4- Elbow Method
    Banner(4,"Elbow Method Graph")

    WCSS = []
    for k in range (1,11,1):

        Model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )
        Model.fit(X_Scale)
        WCSS.append(Model.inertia_)

    print("\nValues of wcss : ")
    for i in range(len(WCSS)) :
        print(f"{i+1} : {WCSS[i]}")


    # Step 5- Visualization 
    Banner(5,"Visualization of Elbow Method")

    plt.plot(range(1,11),WCSS,marker="o")
    plt.xlabel("No of Cluster (k)")
    plt.ylabel("Within Cluster Sum of Square")
    plt.title("Elbow Method")

    plt.grid(True)
    plt.show()

    print(" - Graph Plotted Successfully....\n")

    # Step 6- Final Model
    Banner(6,"Final Model Creation")

    Model = KMeans(
        4,
        random_state=42,
        n_init=10
    )

    Clusters = Model.fit_predict(X_Scale)

    df["Cluster"] = Clusters
    print("\nData Set eith cluster")
    print(df.head(20))

    # Step 7 - visualize the final clusters
    Banner(7,"visualize the final clusters")

    plt.scatter(
        X["AnnualIncome"],
        X["SpendingScore"],
        c=Clusters,
        cmap="viridis"
    )

    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation using K-Means")
    plt.show()

    print(" - End of Case Study.\n")
    

def Banner (Step , Content):

    print("="*60)
    print("\tStep:",Step," - ",Content)
    print("="*60)

if __name__ == "__main__":
    main()