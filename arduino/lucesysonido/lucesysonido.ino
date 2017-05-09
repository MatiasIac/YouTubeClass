const int TRIG = 6;
const int ECHO = 7;
int distance;
int duration;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);
  distance = duration / 29 / 2;

  if (distance > 10 && distance < 15) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    tone(8, 1000, 500);
  } else if (distance > 5 && distance <= 10) {
      digitalWrite(13, HIGH);
      digitalWrite(12, HIGH);
      digitalWrite(11, LOW);
      tone(8, 3000, 500);
  } else if (distance <= 5) {
        digitalWrite(13, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
        tone(8, 5000, 500);
  } else {
          digitalWrite(13, LOW);
          digitalWrite(12, LOW);
          digitalWrite(11, LOW);
          noTone(8);
  }

  delay(500);
  Serial.println("Ciclo");
}
