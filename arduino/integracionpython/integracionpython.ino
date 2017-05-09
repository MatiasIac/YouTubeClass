const int SWITCH = 2;
const int X = 0;
const int Y = 1;

void setup() {
  pinMode(SWITCH, INPUT);
  digitalWrite(SWITCH, HIGH);
  Serial.begin(115200);
}

void loop() {
  Serial.println("{\"x\":" + (String)analogRead(X) + ", \"y\":" + (String)analogRead(Y) + "}");
  delay(100);
}
