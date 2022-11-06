#define MAX_ITEMS 100
#define BTN_PIN 7
#define IR_PIN A0
#define echoPin 2 
#define trigPin 3

int irArray[MAX_ITEMS];
double usArray[MAX_ITEMS];
int tsArray[MAX_ITEMS];


int count=0;
int time=0;

double duration; 
double distance;

void setup() {
  pinMode(IR_PIN, INPUT);
  pinMode(2, OUTPUT);  
  pinMode(3, INPUT);
  pinMode(BTN_PIN, INPUT);  
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);  
  Serial.begin(9600);
}

void loop() {
  while (digitalRead(BTN_PIN) == LOW){
    
    time = millis();
    tsArray[count] = time;
    IR(count);
    US(count);
    delay(100); 

    //Serial.print("TimeStamp: ");
    Serial.print(tsArray[count]);
    Serial.print(",");
    

    //Serial.print("IR Distance : ");
    Serial.print(irArray[count]);
    Serial.print(",");
  

    //Serial.print("US Distance : ");
    Serial.println(usArray[count]);
    delay(500);

    count = (count+1) % MAX_ITEMS;

  }
  count = 0;
}

void IR(int c){
  int val = analogRead(A0);
  irArray[c] = val;
}

void US(int c){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration  * 0.0343 / 2.0;
  usArray[c] = distance;
  
}
