# Customer Segmentation Using K-Means Clustering

## 📌 Project Overview

This project implements **K-Means Clustering**, an unsupervised machine learning algorithm, to group mall customers based on their annual income and spending score.

The project uses the `Mall_Customers.csv` dataset and applies feature scaling and the Elbow Method to determine a suitable number of clusters. The final model assigns each customer to a cluster, helping identify different customer spending patterns.

## 🎯 Objectives

- Analyze customer data using Pandas.
- Select relevant features for clustering.
- Standardize numerical features using `StandardScaler`.
- Apply the Elbow Method to estimate the optimal number of clusters.
- Build a K-Means clustering model using Scikit-learn.
- Assign cluster labels to customers.
- Visualize the Elbow curve using Matplotlib.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data loading and manipulation
- **Matplotlib** – Data visualization
- **Scikit-learn** – Feature scaling and K-Means clustering

## 📂 Project Structure

```text
Customer-Segmentation/
│
├── Mall_Customers.csv
├── CustomerSegmentation.py
└── README.md
```

## 📊 Dataset Description

The project uses the `Mall_Customers.csv` dataset, which contains customer-related information.

The two selected features are:

| Feature | Description |
|---|---|
| AnnualIncome | Customer's annual income |
| SpendingScore | Score representing the customer's spending behavior |

These features are used to identify customer groups with similar income and spending patterns.

**Note:** Ensure that the column names in your CSV match those used in the Python program.

## ⚙️ Project Workflow

### 1. Load the Dataset

The dataset is loaded using Pandas' `read_csv()` function.

The program displays the first few records and checks for missing values.

### 2. Feature Selection

The `AnnualIncome` and `SpendingScore` columns are selected for clustering.

These features help identify relationships between customer income and spending behavior.

### 3. Feature Scaling

`StandardScaler` standardizes the selected features so that differences in their numerical scales do not disproportionately influence the clustering process.

### 4. Elbow Method

The Elbow Method evaluates different values of K, representing the number of clusters.

For each value of K from 1 to 10, the model calculates **WCSS (Within-Cluster Sum of Squares)**, which measures the sum of squared distances between data points and their assigned cluster centroids.

The WCSS values are plotted to help identify a suitable number of clusters.

### 5. K-Means Clustering

A K-Means model is initialized with four clusters, using `random_state=42` and `n_init=10` for reproducibility and multiple initializations.

The model assigns a cluster label to each customer.

### 6. Display Results

The generated cluster labels are added to the original DataFrame as a new column named `Cluster`.

The updated dataset is displayed to inspect customer assignments.

## 📈 Expected Output

When the program runs successfully, it displays:

1. The first five rows of the dataset.
2. Missing-value counts for each column.
3. The selected features.
4. The first five standardized records.
5. WCSS values for K = 1 through K = 10.
6. An Elbow Method graph.
7. Customer records with their assigned cluster labels.

The exact cluster assignments depend on the dataset and the selected features.

## 🚀 Installation and Execution

### Prerequisites

Install Python and the required libraries.

```bash
pip install pandas matplotlib scikit-learn
```

### Run the Project

1. Download or clone this repository.
2. Place `Mall_Customers.csv` in the appropriate location.
3. Update the CSV file path in the Python program.
4. Execute the program:

```bash
python CustomerSegmentation.py
```

## 💡 Applications

- Customer segmentation for marketing campaigns
- Identification of spending patterns
- Customer behavior analysis
- Targeted promotional strategies
- Retail business analytics
- Data-driven customer profiling

## 🔮 Future Enhancements

- Visualize the final clusters using a scatter plot.
- Display cluster centroids.
- Compare clustering results for different values of K.
- Evaluate clustering quality using the Silhouette Score.
- Export the clustered dataset to a new CSV file.
- Analyze the characteristics of each customer segment.

## 📚 Key Concepts Learned

- Unsupervised Machine Learning
- K-Means Clustering
- Feature Selection
- Data Standardization
- Elbow Method
- Within-Cluster Sum of Squares (WCSS)
- Data Visualization
- Customer Segmentation

## 👨‍💻 Author

**Tanay Dherange**

B.Sc. Computer Science Student | Aspiring Software Developer

## 📄 License

This project is available for educational and learning purposes. Add a `LICENSE` file if you intend to distribute it under a specific open-source license.