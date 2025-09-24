# StepSense – ML-Integrated Foot-Traffic Energy Harvesting System

## 📌 Overview

StepSense is a hardware–software integrated project that harvests energy from footsteps using piezoelectric sensors and an ESP32 microcontroller. The system measures and visualizes energy generation in real-time, and uses Machine Learning to classify steps (light/normal/heavy), predict energy output, and forecast footfall trends.

---

## 🔧 Features

- **Energy Harvesting:** Piezoelectric sensors capture foot pressure and convert it into electrical energy.
- **Data Logging & Visualization:** Python scripts for real-time plotting and analysis of voltage and energy.
- **ML Integration:**
  - Step classification (light, normal, heavy)
  - Energy prediction per step
  - Time-series forecasting of footfall
- **IoT Ready:** ESP32 ensures easy data transfer and system scalability.

---

## 🛠️ Tech Stack

- **Hardware:** Piezoelectric sensors, ESP32 microcontroller, rectifier, capacitor
- **Software:** Python, NumPy, Matplotlib, Scikit-learn
- **ML Models:** Classification, Regression, Time-Series Forecasting

---

## 🚀 How It Works

1. **Footstep applies pressure** on piezoelectric sensors.
2. **Generated voltage** is rectified, stored, and logged via ESP32.
3. **Python scripts** process incoming data for visualization.
4. **ML models** analyze patterns for step classification, energy prediction, and footfall forecasting.

---

## 📊 Sample Output

- Voltage vs. Time graph (real-time energy visualization)
- Step type classification report
- Forecast plots for predicted footfall trends

---

## 📂 Project Structure

```
StepSense/
│
├── data/                     # Raw and processed datasets
│   ├── raw/                   # Directly from Arduino logs or manual entry
│   └── processed/             # Cleaned/ready for ML
│
├── models/                    # Trained ML models (.pkl files)
│
├── src/                       # All Python code
│   ├── __init__.py
│   ├── data_preprocessing.py  # Cleaning, feature extraction
│   ├── step_classifier.py     # Classification (light/normal/heavy)
│   ├── energy_prediction.py   # Energy prediction per step
│   ├── footfall_forecast.py   # Time series forecasting
│   └── visualize_data.py      # Your existing Python graph code
│
├── arduino/                   # Arduino sketches
│   └── stepsense.ino
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project description + usage
└── .gitignore                 # Ignore large/unnecessary files
```

---

## 🎯 Applications

- Smart floors in public spaces for renewable energy generation
- Footfall analytics for malls, stations, and campuses
- Green IoT solutions

---

