import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

# Ensure CSV exists
if not os.path.exists("network_traffic.csv"):
    pd.DataFrame(columns=["Timestamp", "Source_IP", "Packet_Size", "Request_Count"]).to_csv("network_traffic.csv", index=False)

def train_model():
    df = pd.read_csv("network_traffic.csv")
    X = df[["Packet_Size", "Request_Count"]]
    y = [1 if count > 100 else 0 for count in df["Request_Count"]]  # Binary labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2f}")
    return model

if __name__ == "__main__":
    train_model()