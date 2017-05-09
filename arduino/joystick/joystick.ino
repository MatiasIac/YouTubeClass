const int SWITCH = 2;
const int X = 0;
const int Y = 1;

void setup() {
  pinMode(SWITCH, INPUT);
  digitalWrite(SWITCH, HIGH);
  Serial.begin(115200);
}

void loop() {
  Serial.print("Switch: ");
  Serial.print(digitalRead(SWITCH));
  Serial.println("");

  Serial.print("X: ");
  Serial.print(analogRead(X));
  Serial.println("");

  Serial.print("Y: ");
  Serial.print(analogRead(Y));
  Serial.println("");
  Serial.println("");

  delay(100);
}
