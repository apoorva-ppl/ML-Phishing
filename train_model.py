# In train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

print("Loading pre-featured data...")
# Load the dataset with all its features
df = pd.read_csv('Phishing_Legitimate_full.csv')

# --- This is the new, simpler logic ---

# The 'CLASS_LABEL' column is our target (y)
y = df['CLASS_LABEL']

# All other columns are our features (X). We drop the label column to get them.
X = df.drop('CLASS_LABEL', axis=1)

# --- The rest of the script is the same ---

print(f"Data loaded. Found {X.shape[1]} features.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training XGBoost model...")
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb.fit(X_train, y_train)

accuracy = xgb.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

print("Saving model as phishing_detector.pkl...")
joblib.dump(xgb, 'phishing_detector.pkl')
print("Done!")
