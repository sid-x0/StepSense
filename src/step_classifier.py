import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Paths
PROCESSED_PATH = os.path.join("data", "processed", "step_data_processed.csv")
MODEL_PATH = os.path.join("models", "step_classifier.pkl")

def train_step_classifier():
    # Load processed dataset
    df = pd.read_csv(PROCESSED_PATH)

    # Features and target
    X = df.drop(columns=["label"])  
    y = df["label"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate
    y_pred = clf.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved at: {MODEL_PATH}")

if __name__ == "__main__":
    train_step_classifier()
