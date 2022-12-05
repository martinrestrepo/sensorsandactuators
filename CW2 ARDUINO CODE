#include <LiquidCrystal_I2C.h>

#define out A5
#define in1 2
#define in2 3
#define in3 4
#define vout 6
#define TIMER_HZ 1250
LiquidCrystal_I2C lcd(0x20, 20, 4);

int t = 5;
int values[8] = {5, 6, 4, 3, 8, 7, 1, 2};
int last_position = -1;
int last_val = -1;
int last_pulse = 0;
int vel_pc = 0;
int vel_pt = 0;
int pulse_ = 0;
int pulse_n = 0;
int pulse_iter = 0;
int timer1_counter;
int counts = 0;
int last_time = 0;
int direction = 0;

void setup() {
  pinMode(out, OUTPUT);  
  pinMode(vout, OUTPUT);    
  pinMode(in1, INPUT);
  pinMode(in2, INPUT);  
  pinMode(in3, INPUT);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(3, 1);
  Serial.begin(9600);
  analogWrite (out, 500);
  analogWrite (vout, 255);

  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;

  timer1_counter = 65486;
  Serial.println("timer");
  Serial.println(timer1_counter);
  TCNT1 = timer1_counter;
  TCCR1B |= (1 << CS12);    // 256 prescaler 
  TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
  interrupts();             // enable all interrupts
}

ISR(TIMER1_OVF_vect)        // interrupt service routine 
{
  TCNT1 = timer1_counter;   // preload timer
  pulse_n += pulse_;
  pulse_ = 0;
  pulse_iter += 1;
  if (pulse_iter % TIMER_HZ == 0) {
    vel_pc = 360.0/8 * pulse_n;
    pulse_n = 0;
    pulse_iter = 0;
  }
}

void loop() {
  int led1 = digitalRead(in1);
  int led2 = digitalRead(in2);
  int led3 = digitalRead(in3);

  int val= 4*led1+2*led2+1*led3;
  int position= (360/8*values[val]) % 360; 

  if (last_position != position)
  {    
    vel_pt = 360/8.0*TIMER_HZ / ( (pulse_iter - last_pulse + TIMER_HZ) % TIMER_HZ);
    //vel_pt = (pulse_iter - last_pulse + TIMER_HZ) % TIMER_HZ;
    direction = values[val] > last_val;
    if (values[val] == 1)
      direction = last_val == 8;
    if (values[val] == 8)
      direction = last_val != 1;
    direction = direction *2 -1;

    if (position == 0){
      counts += direction;
    }

    last_position = position;
    last_val = values[val];
    last_pulse = pulse_iter;
    pulse_ = 1;
    vel_pc = abs(vel_pc) * direction;
    vel_pt = vel_pt * direction;
    
    if (millis() - last_time > 1000 )
    {lcd.clear(); 
    lcd.setCursor(0, 0);
    lcd.print("Vel: ");
    lcd.print(vel_pc);
    lcd.print("/");
    lcd.print(vel_pt);
    lcd.setCursor(0, 1);
    lcd.print("Counts: ");
    lcd.print(counts);
    last_time = millis();
    }

    Serial.print(millis());
    Serial.print(",");
    Serial.print(position);
    Serial.print(",");
    Serial.print(vel_pc);
    Serial.print(",");
    Serial.print(vel_pt);
    Serial.print(",");
    Serial.print(counts);
    Serial.println();
    //delay(10);
  }
 
  //Serial.print(led1);
  //Serial.print(led2);
 // Serial.print(led3);


}
