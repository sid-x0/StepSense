const int piezoPin = A0;  // Piezo connected to analog pin A0
int sensorValue = 0;
float voltage = 0.0;

void setup() {
  Serial.begin(9600);
  Serial.println("Time(ms),Voltage(V),RawValue");  // Optional header
}

void loop() {
  sensorValue = analogRead(piezoPin);
  voltage = sensorValue * (5.0 / 1023.0);  // Convert to voltage

  Serial.print(millis());
  Serial.print(",");
  Serial.print(voltage, 3);  // Print voltage with 3 decimal places
  Serial.print(",");
  Serial.println(sensorValue);

  delay(50);  // Adjust as needed
}
