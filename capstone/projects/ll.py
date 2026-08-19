from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from .tree import DecisionTreeClassifier

# 1. Load sample dataset (Iris flower classification)
data = load_iris()
X = data.data  # Features (measurements)
y = data.target  # Labels (flower species)

# 2. Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Choose and train a Machine Learning model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Make predictions on unseen test data
predictions = model.predict(X_test)

# 5. Evaluate the model's accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")