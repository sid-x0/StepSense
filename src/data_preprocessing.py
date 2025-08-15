import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import os

RAW_PATH = r"C:\SID\project\StepSense\data\raw\step_data.csv"
PROCESSED_PATH = r"C:\SID\project\StepSense\data\processed\step_data_processed.csv"

# Make sure processed folder exists
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)

# Read raw CSV
df = pd.read_csv(RAW_PATH)

df.dropna(inplace=True)

# Scale numeric columns
scaler = MinMaxScaler()
numeric_cols = ['peak_voltage', 'duration', 'rise_time', 'energy']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Encode labels
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])

# Save processed CSV
df.to_csv(PROCESSED_PATH, index=False)

print(f"Processed data saved to {PROCESSED_PATH}")
