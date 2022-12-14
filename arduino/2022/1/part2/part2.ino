#include <SPI.h>
#include <SD.h>

const int chipSelect = 10;
char character;
String currentLine = "";
uint64_t currentCalories = 0;
uint64_t topThreeCalories [3] = {0,0,0};

void setup() {
  Serial.begin(115200);

  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    while (1);
  }

  File dataFile = SD.open("input.txt");

  if (dataFile) {
    while (dataFile.available()) {
      character = dataFile.read();
      if (character != '\n') {
        currentLine += character;
      }
      else {
        if (currentLine.length() > 0) {
          currentCalories += currentLine.toInt();
        }
        else {
          processResult(currentCalories);
          currentCalories = 0;
        }
        currentLine = "";
      }
    }
    dataFile.close();
  }
  else {
    Serial.println("Error opening file!");
  }

  print_uint64_t(topThreeCalories[0]+topThreeCalories[1]+topThreeCalories[2]);
  Serial.println();
}

void processResult(uint64_t result){
  if (result > topThreeCalories[0]){
    topThreeCalories[2] = topThreeCalories[1];
    topThreeCalories[1] = topThreeCalories[0];
    topThreeCalories[0] = result;
    return;
  }
  if (result > topThreeCalories[1]){
    topThreeCalories[2] = topThreeCalories[1];
    topThreeCalories[1] = result;
    return;
  }
  if (result > topThreeCalories[2]){
    topThreeCalories[2] = result;
    return;
  }
  
}

void print_uint64_t(uint64_t num) {
  char rev[128];
  char *p = rev + 1;

  while (num > 0) {
    *p++ = '0' + ( num % 10);
    num /= 10;
  }
  p--;
  /*Print the number which is now in reverse*/
  while (p > rev) {
    Serial.print(*p--);
  }
}

void loop() {
}
