# Wine Predictor using K-Nearest Neighbors

## 📌 Project Overview

**Wine Predictor** is a Machine Learning classification project developed using **Python** and **K-Nearest Neighbors (KNN)**.

The project reads wine-related data from a CSV file, cleans the dataset, separates input and output variables, performs training and testing data splitting, applies feature scaling, and evaluates different K values to determine how the value of `K` affects classification accuracy.

The project also provides a graphical representation of **K Value vs Accuracy** using Matplotlib.

---

## 🎯 Objective

The main objectives of this project are:

- Load a wine dataset from a CSV file.
- Clean the dataset by handling missing values.
- Separate independent and dependent variables.
- Divide the dataset into training and testing data.
- Apply feature scaling using `StandardScaler`.
- Implement the K-Nearest Neighbors classification algorithm.
- Test multiple values of `K`.
- Calculate classification accuracy.
- Visualize the relationship between `K` and accuracy.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Scikit-learn**
- **K-Nearest Neighbors (KNN)**
- **StandardScaler**
- **Train-Test Split**

---

## 📂 Project Structure

```text
Wine-Predictor/
│
├── WinePredictor.py
├── WinePredictor.csv
└── README.md
```

---

## 📊 Dataset

The program expects a CSV file named:

```text
WinePredictor.csv
```

The dataset should contain:

- Multiple numerical feature columns
- One target column named `Class`

Example structure:

```text
Feature1, Feature2, Feature3, ..., Class
value,    value,    value,    ..., 1
value,    value,    value,    ..., 2
value,    value,    value,    ..., 3
```

The `Class` column represents the output that the model has to predict.

---

# 🔄 Machine Learning Workflow

The project follows the following workflow:

```text
Load Dataset
      ↓
Data Cleaning
      ↓
Separate X and Y
      ↓
Train-Test Split
      ↓
Feature Scaling
      ↓
KNN Model
      ↓
Test Different K Values
      ↓
Calculate Accuracy
      ↓
Visualize Results
```

---

## Step 1 — Load Dataset

The dataset is loaded using Pandas.

```python
DataFrame = pd.read_csv(DataPath)
```

The first few records are displayed using:

```python
DataFrame.head()
```

This helps verify that the dataset has been loaded correctly.

---

## Step 2 — Data Cleaning

Missing values are removed using:

```python
DataFrame.dropna(inplace=True)
```

The program also displays:

- Number of records
- Number of columns
- Dataset shape

This provides basic information about the dataset before training the model.

---

## Step 3 — Separate Independent and Dependent Variables

The input features are stored in `X`:

```python
X = DataFrame.drop(columns=["Class"])
```

The target/output variable is stored in `Y`:

```python
Y = DataFrame["Class"]
```

### Independent Variables

The independent variables are the features used by the model to make predictions.

### Dependent Variable

The dependent variable is the `Class` column that the model attempts to predict.

---

## Step 4 — Train-Test Split

The dataset is divided into training and testing data using:

```python
train_test_split()
```

The project currently uses:

- **50% training data**
- **50% testing data**
- `random_state=42`
- `stratify=Y`

`stratify=Y` helps maintain a similar distribution of classes in both training and testing datasets.

---

## Step 5 — Feature Scaling

KNN uses distances between data points. Therefore, features with larger numerical ranges can have a greater influence on the distance calculation.

To avoid this problem, `StandardScaler` is used.

```python
Scaler = StandardScaler()
```

Training data:

```python
X_Train_Scaled = Scaler.fit_transform(X_Train)
```

Testing data:

```python
X_Test_Scaled = Scaler.transform(X_Test)
```

The scaler learns the parameters from the training data and applies the same transformation to the testing data.

---

# 🤖 Step 6 — K-Nearest Neighbors

The project uses:

```python
KNeighborsClassifier
```

KNN classifies a new data point based on its nearest neighboring data points.

The value of `K` determines how many neighboring points are considered.

For example:

```text
K = 3
```

means the model considers the **3 nearest neighbors**.

---

# ⚙️ Step 7 — Hyperparameter Testing

The project tests K values from:

```text
K = 1 to 20
```

For each K value:

1. A KNN model is created.
2. The model is trained.
3. Predictions are generated.
4. Accuracy is calculated.
5. The accuracy is stored.

The results are then displayed graphically.

---

# 📈 Visualization

Matplotlib is used to create a graph:

K Value vs Accuracy

The graph helps visualize how changing the K value affects model accuracy.

Example:

Accuracy
   │
100│           ●
 90│      ●         ●
 80│   ●
 70│
   └────────────────────
      1  2  3  4 ... 20
             K Value


The actual graph depends on the dataset and train-test split.

---

# ▶️ How to Run

## 1. Install Python

Make sure Python is installed on your system.

Check the Python version:

```bash
python --version
```

---

## 2. Install Required Libraries

Install the required packages:

```bash
pip install pandas matplotlib scikit-learn
```

---

## 3. Place the Dataset

Keep `WinePredictor.csv` in the same directory as the Python program.

Example:

```text
Wine-Predictor/
│
├── WinePredictor.py
├── WinePredictor.csv
└── README.md
```

---

## 4. Run the Program

Execute:

```bash
python WinePredictor.py
```

The program will:

- Display dataset information.
- Clean the data.
- Split the dataset.
- Scale the features.
- Test K values from 1 to 20.
- Display accuracy values.
- Generate an accuracy graph.

---

# 📋 Example Output

```text
==============================
 - Step1 Load the dataset from csv file
------------------------------

Some Entries from dataset is :-

       Feature1    Feature2    Feature3    Class
0       ...
1       ...
2       ...
3       ...
4       ...

==============================
 - Step2 Clean the Data sets.
------------------------------

Shape of dataset :-  (178, 14)
Total Records :-  178
Total Columns :-  14
```

The exact output depends on the dataset being used.

---

# 🧠 Concepts Demonstrated

This project demonstrates several important Machine Learning concepts:

- Data loading
- Data cleaning
- Pandas DataFrame
- Independent and dependent variables
- Training and testing datasets
- Feature scaling
- K-Nearest Neighbors
- Hyperparameter `K`
- Model prediction
- Accuracy calculation
- Data visualization
- Classification

---

# 📌 Important Note

The current implementation evaluates each K value using the test dataset. For a production-quality Machine Learning workflow, K should ideally be selected using a **validation set or cross-validation**, and the test set should be reserved for the final evaluation.

A future version can include:

- Cross-validation
- Automatic selection of the best K
- Final model training
- Confusion matrix
- Precision
- Recall
- F1-score
- Classification report

---

# 🚀 Future Enhancements

Possible improvements include:

1. Add cross-validation for K selection.
2. Automatically select the best K value.
3. Generate a confusion matrix.
4. Display precision, recall and F1-score.
5. Add a classification report.
6. Add user input for predicting a new wine.
7. Compare KNN with other classification algorithms.
8. Add a GUI for wine prediction.
9. Save the trained model using `joblib` or `pickle`.

---

# 👨‍💻 Author

**Tanay Dherange**

BSc Computer Science

Interested in:

- C / C++
- Python
- Data Structures
- Machine Learning
- Software Development

---

## 📄 License

This project is created for **educational and learning purposes**.