// -----------------------------------------
// Demonstrate Particle and IFTTT
/* -----------------------------------------
This program subscribes to a a particle event.
An IFTTT app monitors inbox activity of a Gmail account and publishes events to the Particle Cloud.
------------------------------------------*/

int led = D0;
int boardLed = D7;

// setup() is run only once, it's where we set up GPIO and initialise peripherals
void setup() {
    
  // Setup GPIO
  pinMode(led,OUTPUT); // Our LED pin is output (lighting up the LED)
  pinMode(boardLed,OUTPUT); // Our on-board LED is output as well
  digitalWrite(led,LOW);
  digitalWrite(boardLed,LOW);
  
  // Subscribe to an event published by IFTTT using Particle.subscribe
  Particle.subscribe("turn_my_led_on_alexa_234423", myHandler);
  // TODO:
  // Subscribe will listen for the event unique_event_name and, when it finds it, will run the function myHandler()
  // (Remember to replace unique_event_name with an event name of your own choosing. Make it somewhat complicated to make sure it's unique.)
  // myHandler() is declared later in this app.
}

// loop() runs continuously, it's our infinite loop. In this program we only want to repsond to events, so loop can be empty.
void loop() {

}

// Now for the myHandler function, which is called when the Particle cloud tells us that our email event is published.
void myHandler(const char *event, const char *data)
{
  /* Particle.subscribe handlers are void functions, which means they don't return anything.
  They take two variables-- the name of your event, and any data that goes along with your event.
  In this case, the event will be "buddy_unique_event_name" and the data will be "on" or "off"
  */

  if (strcmp(data,"led off")==0) {
    // if subject line of email is "off"
    digitalWrite(led,LOW);
    digitalWrite(boardLed,LOW);
  }
  else if (strcmp(data,"led on")==0) {
    // if subject line of email is "on"
    digitalWrite(led,HIGH);
    digitalWrite(boardLed,HIGH);
  }

}