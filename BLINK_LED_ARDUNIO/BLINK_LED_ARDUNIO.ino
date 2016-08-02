/*
Adopted code from https://www.arduino.cc/en/Tutorial/Melody

Song is "Jingle Bells"

The Arduino speaker does not need a resistor.
Use as many lights as you can to simulate Christmas lights! (while the song plays at the same time)
Here's a hint: https://www.arduino.cc/en/Tutorial/BlinkWithoutDelay
*/


int speakerPin = 9;

int length = 50; // the number of notes
char notes[] = "eeeeeeegcdefffffeeeeddedgeeeeeeegcdefffffeeeggfdc ";// a space represents a rest
int beats[] = { 4, 4, 8, 4, 4, 8, 4, 4, 4, 4, 16, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 4, 4, 8, 4, 4, 8, 4, 4, 4, 4, 16, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 16, 16};
int tempo = 60;

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note, int duration) {
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

  // play the tone corresponding to the note name
  for (int i = 0; i < 8; i++) {
    if (names[i] == note) {
      playTone(tones[i], duration);
    }
  }
}

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  for (int i = 0; i < length; i++) {
    if (notes[i] == ' ') {
      delay(beats[i] * tempo); // rest
    } else {
      playNote(notes[i], beats[i] * tempo);
    }

    // pause between notes
    delay(tempo / 2); 
  }
}

