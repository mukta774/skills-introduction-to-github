# Skin Type Classification

A machine learning project to classify skin types based on physiological and environmental factors using multiple classification algorithms.

## Overview

This project builds and compares various machine learning models to predict skin type (Dry, Oily, Normal, or Combination) from a dataset of 1,300+ samples with features including:
- **Age**: User age in years
- **Gender**: Male/Female
- **Hydration Level**: Low/Medium/High
- **Oil Level**: Low/Medium/High
- **Sensitivity**: Low/Medium/High
- **Humidity**: Environmental humidity percentage
- **Temperature**: Environmental temperature

## Dataset

- **File**: `Skin_Type_OG.csv`
- **Size**: 1,300+ records
- **Target Variable**: Skin_Type (4 classes: Dry, Oily, Normal, Combination)
- **Features**: 7 input features

## Models

This project implements and compares the following classification algorithms:

1. **Decision Tree** (`decisiontree.py`)
   - Hyperparameter tuning with GridSearchCV
   - Feature importance analysis
   - Tree visualization

2. **Logistic Regression** (`logistics_regression.py`)
   - Classification with probability estimates
   - Feature coefficients analysis

3. **Random Forest** (`random_forest.py`)
   - Ensemble method with multiple decision trees
   - Feature importance ranking

4. **XGBoost** (`xgboost.py`)
   - Gradient boosting approach
   - Advanced hyperparameter tuning

## Project Structure

```
├── Skin_Type_OG.csv              # Main dataset
├── decisiontree.py               # Decision Tree implementation
├── logistics_regression.py        # Logistic Regression implementation
├── random_forest.py              # Random Forest implementation
├── xgboost.py                    # XGBoost implementation
└── README.md                     # This file
```

## Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
xgboost
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mukta774/skin_care.git
cd skin_care
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run any of the model files to train and evaluate:

```bash
python decisiontree.py
python logistics_regression.py
python random_forest.py
python xgboost.py
```

## Model Evaluation

Each model includes:
- Accuracy score
- Precision, Recall, and F1-Score (weighted average)
- Confusion matrix visualization
- Feature importance analysis
- Classification report with per-class metrics

## Features

- Data preprocessing with categorical encoding (One-Hot Encoding)
- Train-test split with stratification (80-20 split)
- Hyperparameter tuning using GridSearchCV
- Cross-validation (5-fold)
- Class imbalance handling capabilities
- Comprehensive performance metrics and visualizations

## Results

Each model outputs:
- Classification metrics
- Confusion matrix heatmap
- Top 20 feature importances bar chart
- Decision tree visualization (for tree-based models)

## Key Insights

- Compare performance across different algorithms
- Identify which features are most important for skin type classification
- Understand how environmental factors (humidity, temperature) influence skin type
- Evaluate the trade-offs between model complexity and accuracy

## Author

mukta774

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests.

---

**Last Updated**: March 26, 2026