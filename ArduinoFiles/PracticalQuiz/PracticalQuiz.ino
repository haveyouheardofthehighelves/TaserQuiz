int light_pin = 4;
int toggle = 12;
int button_pin = A0;
int green = LOW; // Assign HIGH to represent green
int red = HIGH;    // Assign LOW to represent red
int taser_pin = 13;
bool pressed = false;

void setup() {
  pinMode(taser_pin, OUTPUT);
  pinMode(light_pin, OUTPUT);
  pinMode(toggle, OUTPUT); // Use toggle pin 12
  pinMode(button_pin, INPUT);
  digitalWrite(toggle, HIGH); // Ensure toggle pin is high
  digitalWrite(taser_pin, LOW);
  Serial.begin(9600);
}

void back_n_forth(){

  for (int i = 10; i <= 50; i += 10) { // Corrected loop conditions
      digitalWrite(light_pin, green);
      delay(50);
      digitalWrite(light_pin, red);
      delay(50); // Add delay to keep each color on for a while
  }
    for (int i = 50; i <= 700; i += 45) { // Corrected loop conditions
      digitalWrite(light_pin, green);
      delay(i);
      digitalWrite(light_pin, red);
      delay(i); // Add delay to keep each color on for a while
  }


}


void loop() {
  Serial.println(digitalRead(A0));
  if(Serial.available()){
    char incomingByte = Serial.read();
    if(incomingByte == 'g'){
      back_n_forth();
      digitalWrite(light_pin, green);
    }

    if(incomingByte == 'r'){
       back_n_forth();
       digitalWrite(light_pin, red);
       digitalWrite(taser_pin, HIGH);
       delay(200);
       digitalWrite(taser_pin, LOW);
    }

    if(incomingByte == 'g' || incomingByte == 'r'){
       Serial.println('d');
    }
  }
  // put your main code here, to run repeatedly:
}