import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, accuracy_score, mean_squared_error, r2_score

# 1. Load Dataset (Replace 'your_dataset.csv' with your file path or URL)
# df = pd.read_csv('your_dataset.csv')

# Placeholder synthetic dataset for demonstration
df = pd.DataFrame({
    'feature_num': [25, 30, np.nan, 45, 35, 50, 23, 40],
    'feature_cat': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
    'target_class': [0, 1, 0, 1, 0, 1, 0, 1],       # For Classification
    'target_reg': [100, 150, 110, 200, 140, 210, 95, 180] # For Regression
})

# Define features and targets
X = df.drop(columns=['target_class', 'target_reg'])
y_class = df['target_class']
y_reg = df['target_reg']

# Identify numerical and categorical columns
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object', 'category']).columns

# 2. Define Preprocessing Pipeline
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, num_cols),
    ('cat', cat_transformer, cat_cols)
])

# ---------------------------------------------------------
# TASK 1: CLASSIFICATION PIPELINE
# ---------------------------------------------------------
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X, y_class, test_size=0.2, random_state=42
)

clf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

clf_pipeline.fit(X_train_c, y_train_c)
y_pred_c = clf_pipeline.predict(X_test_c)

print("--- Classification Results ---")
print("Accuracy:", accuracy_score(y_test_c, y_pred_c))
print(classification_report(y_test_c, y_pred_c))

# ---------------------------------------------------------
# TASK 2: REGRESSION PIPELINE
# ---------------------------------------------------------
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

reg_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42))
])

reg_pipeline.fit(X_train_r, y_train_r)
y_pred_r = reg_pipeline.predict(X_test_r)

print("--- Regression Results ---")
print("RMSE:", np.sqrt(mean_squared_error(y_test_r, y_pred_r)))
print("R2 Score:", r2_score(y_test_r, y_pred_r))