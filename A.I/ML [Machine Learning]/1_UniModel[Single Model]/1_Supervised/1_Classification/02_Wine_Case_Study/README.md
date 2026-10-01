# Wine Classification – KNN

## 📁 Project Location

This project is part of the **Python Data Science and Generative AI Programs** repository.

```text
Python(Data_Science_and_Gen_AI)-programs
│
└── A.I
    │
    └── ML [Machine Learning]
        │
        └── 1_UniModel [Single Model]
            │
            └── 1_Supervised
                │
                └── 1_Classification
                    │
                    └── 02_Wine_Case_Study
```

### Complete Local Path

```text
D:\Desktop\marvellous\GitHub_Codes\Python(Data_Science_and_Gen_AI)-programs\A.I\ML [Machine Learning]\1_UniModel[Single Model]\1_Supervised\1_Classification\02_Wine_Case_Study
```

---

## 📌 Project Description

This project implements **Wine Classification using the K-Nearest Neighbors (KNN)** machine learning algorithm.

The model uses the chemical properties of wine to predict its corresponding class.

The project also demonstrates **feature scaling** and **hyperparameter tuning** by testing different values of `K`.

---

## 🧠 Machine Learning Algorithm

### K-Nearest Neighbors (KNN)

KNN is a supervised machine learning algorithm used for classification and regression.

For classification, KNN determines the class of a new data point based on the classes of its nearest neighboring data points.

The number of neighbors is controlled using the **K value**.

In this project:

```text
K = 1 to 20
```

are tested to observe how the value of K affects model accuracy.

---

## 🔄 Machine Learning Workflow

```text
Wine Dataset
     ↓
Load Dataset
     ↓
Clean Dataset
     ↓
Separate Features and Labels
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
Compare K Values
     ↓
Plot K vs Accuracy
```

---

## 📊 Dataset

The input dataset is:

```text
WinePredictor.csv
```

The target/output column is:

```text
Class
```

All remaining columns are used as independent variables/features.

The program separates them using:

```text
X = Independent Variables
Y = Class
```

---

## 🧹 Data Cleaning

The project removes missing values using:

```text
DataFrame.dropna()
```

After cleaning, the program displays:

- Dataset shape
- Total records
- Total columns

---

## ✂️ Train-Test Split

The dataset is divided into training and testing data.

Current configuration:

```text
Training Data : 50%
Testing Data  : 50%
Random State  : 42
```

Stratified splitting is used to maintain the class distribution between training and testing datasets.

---

## 📏 Feature Scaling

KNN is distance-based, so feature scaling is important.

The project uses:

**StandardScaler**

The scaler calculates the mean and standard deviation from the training data and transforms the features accordingly.

The correct workflow is:

```text
X_Train
   ↓
fit_transform()
   ↓
X_Train_Scaled

X_Test
   ↓
transform()
   ↓
X_Test_Scaled
```

The test data should not be used to fit the scaler.

---

## ⚙️ Hyperparameter Tuning

The project tests different K values:

```text
K = 1, 2, 3, ... 20
```

For every K value:

1. Create a KNN model.
2. Train the model.
3. Predict the test data.
4. Calculate accuracy.
5. Store the accuracy.

This allows the relationship between **K value and model accuracy** to be visualized.

---

## 📈 Visualization

A line graph is generated showing:

```text
X-axis → K Value
Y-axis → Accuracy
```

This helps visualize how changing the number of neighbors affects the model's performance.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

### Python Libraries

```text
pandas
matplotlib
scikit-learn
```

Scikit-learn components used:

```text
KNeighborsClassifier
train_test_split
StandardScaler
accuracy_score
confusion_matrix
```

---

## 📂 Project Structure

```text
02_Wine_Case_Study/
│
├── WinePredictor.csv
├── WinePredictor.py
└── README.md
```

---

## 🎯 Learning Objectives

This case study demonstrates:

- Loading CSV data using Pandas
- Cleaning a dataset
- Handling missing values
- Separating independent and dependent variables
- Splitting data into training and testing sets
- Feature scaling
- Understanding KNN classification
- Hyperparameter tuning
- Testing multiple K values
- Calculating classification accuracy
- Visualizing model performance

---

## 🔑 Important Concepts

### K

The number of neighboring data points considered by KNN.

### Feature Scaling

Normalization of features so that features with larger numerical ranges do not dominate distance calculations.

### Training Data

Data used to train the KNN model.

### Testing Data

Previously unseen data used to evaluate the trained model.

### Accuracy

The percentage of correctly classified samples.

---

## ▶️ How to Run

### 1. Install Required Libraries

```text
pip install pandas matplotlib scikit-learn
```

### 2. Keep the Dataset in the Project Directory

```text
WinePredictor.csv
```

### 3. Run the Python Program

```text
python WinePredictor.py
```

The program will display the dataset information, accuracy for each K value, and a graph showing **K Value vs Accuracy**.

---

## 👨‍💻 Author

**Tanay Dherange**