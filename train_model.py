import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib
from feature_extractor import extract_features

print("Loading data...")
# Make sure your CSV has 'url' and 'label' columns
df = pd.read_csv('phishing.csv')

# Convert labels: 'bad'/'phishing' -> 1, 'good'/'benign' -> 0
df['label'] = df['label'].apply(lambda x: 1 if x == 'bad' else 0)

print("Extracting features...")
feature_list = df['url'].apply(extract_features)
X = pd.DataFrame(feature_list)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training XGBoost model...")
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb.fit(X_train, y_train)

accuracy = xgb.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

print("Saving model as phishing_detector.pkl...")
joblib.dump(xgb, 'phishing_detector.pkl')
print("Done!")
