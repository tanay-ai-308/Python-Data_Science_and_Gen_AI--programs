# Multiple Linear Regression – Advertising Sales Prediction

## 📌 Project Overview

This project implements a **Multiple Linear Regression** model using Python and Scikit-learn to predict product sales based on advertising budgets spent on TV, radio, and newspaper advertising.

The project demonstrates a complete machine learning workflow, including data loading, exploratory data analysis (EDA), data preprocessing, model training, prediction, and performance evaluation.

## 🎯 Objectives

- Load and analyze the advertising dataset using Pandas.
- Identify and remove unwanted columns.
- Check for missing values and generate statistical summaries.
- Analyze correlations between advertising budgets and sales.
- Split the dataset into training and testing sets.
- Train a Multiple Linear Regression model.
- Predict sales and evaluate model performance.
- Understand model coefficients and the intercept.

## 🛠️ Technologies Used

- **Python** – Programming language
- **NumPy** – Numerical calculations
- **Pandas** – Data loading and manipulation
- **Matplotlib** – Data visualization library
- **Scikit-learn** – Machine learning model and evaluation metrics

## 📂 Dataset Description

The project uses `Advertising.csv`, which contains advertising expenditure and corresponding sales data.

| Column | Description |
|---|---|
| `TV` | Advertising budget spent on TV |
| `radio` | Advertising budget spent on radio |
| `newspaper` | Advertising budget spent on newspapers |
| `sales` | Product sales (target variable) |

The `Unnamed: 0` column is removed if it exists because it is an unnecessary index column.

## ⚙️ Project Workflow

### Step 1: Load the Dataset
Load `Advertising.csv` using Pandas and display the first few records.

### Step 2: Remove Unwanted Columns
Remove the `Unnamed: 0` column if present.

### Step 3: Check Missing Values
Identify missing values in each column using `isnull().sum()`.

### Step 4: Statistical Summary
Use `describe()` to examine the count, mean, standard deviation, minimum, maximum, and quartiles of numerical columns.

### Step 5: Correlation Analysis
Use `corr()` to examine relationships between advertising expenditure and sales.

### Step 6: Separate Independent and Dependent Variables
- **Independent variables (X):** TV, radio, newspaper
- **Dependent variable (Y):** sales

### Step 7: Split the Dataset
Use `train_test_split()` to divide the dataset:

- Training data: 80%
- Testing data: 20%
- Random state: 42

### Step 8: Train the Model
Create a `LinearRegression` model and train it using the training dataset.

### Step 9: Predict Sales
Use the trained model to predict sales for the testing dataset.

### Step 10: Evaluate the Model
Evaluate prediction performance using Mean Squared Error, Root Mean Squared Error, and R² score.

### Step 11: Display Model Parameters
Display the coefficients for TV, radio, and newspaper advertising, along with the intercept.

## 🧮 Multiple Linear Regression Formula

The model estimates sales using the following equation:

**Sales = b₀ + b₁(TV) + b₂(Radio) + b₃(Newspaper)**

Where:

- `b₀` is the intercept.
- `b₁` is the TV advertising coefficient.
- `b₂` is the radio advertising coefficient.
- `b₃` is the newspaper advertising coefficient.

Each coefficient represents the estimated change in sales associated with a one-unit increase in that advertising variable, while holding the other variables constant.

## 📊 Model Evaluation Metrics

| Metric   | Description                                                                                                                |
|----------|----------------------------------------------------------------------------------------------------------------------------|
|  MSE     | Mean Squared Error measures the average squared prediction error. Lower is better.                                         |
|  RMSE    | Root Mean Squared Error expresses prediction error in the target variable's units. Lower is better.                        |
| R² Score | Measures how much variation in the target is explained by the model. A score closer to 1 generally indicates a better fit. |

The actual metric values are calculated and displayed when the program runs.

## 📦 Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## 🚀 Installation and Execution

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd <project-directory>
```

### 3. Install Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 4. Add the Dataset

Place `Advertising.csv` in the same directory as your Python script, or update the dataset path in the code.

### 5. Run the Program

```bash
python MultipleLinearRegression.py
```

Replace `MultipleLinearRegression.py` with your actual Python filename if it differs.

## 📁 Project Structure

```text
Multiple-Linear-Regression/
│
├── Advertising.csv
├── MultipleLinearRegression.py
└── README.md
```

## 💡 Learning Outcomes

By completing this project, you can learn how to:

- Perform basic exploratory data analysis.
- Prepare features and target variables.
- Split data for machine learning.
- Train a regression model using Scikit-learn.
- Generate predictions on unseen test data.
- Evaluate regression performance using standard metrics.
- Interpret regression coefficients and the intercept.

## 🔮 Future Improvements

- Add correlation heatmaps and scatter plots.
- Visualize actual sales versus predicted sales.
- Plot residuals to analyze prediction errors.
- Compare Linear Regression with other regression algorithms.
- Add improved handling for missing values and invalid data.
- Save the trained model for future predictions.

## 👨‍💻 Author

**Tanay Dherange**

Aspiring Software Developer | Python | Machine Learning | C/C++

## 📄 License

This project is intended for educational and learning purposes. Add a `LICENSE` file to specify the terms under which others may use or distribute your code.
