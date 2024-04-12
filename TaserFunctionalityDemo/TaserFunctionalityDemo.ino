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

void correct(){
   digitalWrite(light_pin, green);
}

void wrong(){
   digitalWrite(light_pin, red);
}

void loop() {
  if(digitalRead(A0) == 1){
    pressed = true; 
  }

  if(pressed && digitalRead(A0) == 0){
    pressed = false; 
    back_n_forth(); 
    int num = random(0,2);
    Serial.print(num);
    digitalWrite(light_pin, num);  
    if(num == red){
      digitalWrite(taser_pin, HIGH); 
      delay(200); 
      digitalWrite(taser_pin, LOW); 
    }
  }
  
}
