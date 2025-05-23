#include "Adafruit_GFX.h"
#include "MCUFRIEND_kbv.h"
#include "TouchScreen.h"
#include "graphics.h"
#include "constants.h"

void drawColorBitmap(int16_t x, int16_t y, const uint16_t *bitmap, int16_t w, int16_t h, float scale = 1.0) {
  for (int16_t origY = 0; origY < h; origY++) {
    int16_t yStart = round(y + origY * scale);
    int16_t yEnd = round(y + (origY + 1) * scale);
    int16_t height = max(1, yEnd - yStart);
    for (int16_t origX = 0; origX < w; origX++) {
      int16_t xStart = round(x + origX * scale);
      int16_t xEnd = round(x + (origX + 1) * scale);
      int16_t width = max(1, xEnd - xStart);
      uint16_t color = pgm_read_word(&bitmap[origY * w + origX]);
      tft.fillRect(xStart, yStart, width, height, color);
    }
  }
}

void blinkFunc() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= nextBlinkTime) {
    previousMillis = currentMillis;
    nextBlinkTime = random(minBlinkInterval, maxBlinkInterval);
    blinkStartTime = currentMillis;
    tft.fillRect(201, 59, 8, 4, DARKYELLOW);
    tft.fillRect(220, 55, 8, 4, DARKYELLOW);
  }
  if (blinkStartTime > 0 && currentMillis - blinkStartTime >= blinkDuration) {
    tft.fillRect(201, 59, 8, 4, BLACK);
    tft.fillRect(220, 55, 8, 4, BLACK);
    blinkStartTime = 0;
  }
}

void updateMoney() {
  tft.setCursor(27, 7);
  tft.setTextSize(2);
  drawColorBitmap(6, 5, coin, 20, 20, 0.9);
  tft.println(String(money));
}

void drawPercent() {
  tft.drawRoundRect(12, 37, 30, 120, 5, THEME);
  tft.drawRoundRect(56, 37, 30, 120, 5, THEME);
  tft.fillRoundRect(12, 37, 30, happiness * 1.2, 5, DARKTHEME);
  tft.fillRoundRect(56, 37, 30, health * 1.2, 5, DARKTHEME);
}

void drawTopBar() {
  tft.fillRect(0, 0, 320, 30, THEME);
  tft.fillRect(290, 0, 30, 30, DARKTHEME);
  tft.setCursor(100, 3);
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.println(F("Chirpie"));
  updateMoney();
}

void drawButtons() {
  tft.fillRoundRect(7, 195, 70, 40, 10, THEME);
  tft.fillRoundRect(86, 195, 70, 40, 10, THEME);
  tft.fillRoundRect(164, 195, 70, 40, 10, THEME);
  tft.fillRoundRect(243, 195, 70, 40, 10, THEME);
  drawColorBitmap(16, 160, smile, 15, 15, 1.5);
  drawColorBitmap(58, 158, health_symbol, 15, 15, 1.7);
  drawColorBitmap(32, 200, food, 13, 18, 1.7);
  drawColorBitmap(107, 200, pet, 14, 13, 2.1);
  drawColorBitmap(183, 198, broom, 29, 27, 1.2);
  drawColorBitmap(263, 200, sleep, 35, 35, 0.8);
  drawColorBitmap(100, 40, chirpie, 59, 38, 3.75);
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.setCursor(298, 5);
  tft.println(F("+"));
}

void setHome() {
  tft.drawRect(0, 29, 100, 162, THEME);
  tft.drawRect(0, 190, 320, 50, THEME);
  tft.fillRect(100, 30, 220, 160, SKYBLUE);
  drawPercent();
  drawButtons();
}

void drawHabits() {
  tft.fillRoundRect(7, 35, 150, 97, 5, DARKTHEME);
  tft.fillRoundRect(162, 35, 150, 97, 5, DARKTHEME);
  tft.fillRoundRect(7, 137, 150, 97, 5, DARKTHEME);
  tft.fillRoundRect(162, 137, 150, 97, 5, DARKTHEME);
  tft.setTextSize(3);
  tft.setTextColor(WHITE);
  tft.setCursor(39, 45);
  tft.print(F("HABIT"));
  tft.setCursor(194, 45);
  tft.print(F("HABIT"));
  tft.setCursor(39, 147);
  tft.print(F("HABIT"));
  tft.setCursor(194, 147);
  tft.print(F("HABIT"));
}

void setStore() {
  tft.fillRect(0, 30, 320, 240, BACKGROUND);
  drawHabits();
}

bool canPressButton() {
  unsigned long currentMillis = millis();
  if (currentMillis - lastButtonPressTime >= buttonCooldown) {
    lastButtonPressTime = currentMillis;
    return true;
  }
  return false;
}

void setup() {
  Serial.begin(9600);
  uint16_t ID = tft.readID();
  tft.begin(ID);
  tft.setRotation(-1);
  tft.fillScreen(BACKGROUND);
  drawTopBar();
  setHome();
}

void loop() {
  digitalWrite(13, HIGH);
  TSPoint p = ts.getPoint();
  digitalWrite(13, LOW);
  pinMode(XM, OUTPUT);
  pinMode(YP, OUTPUT);
  if (state == 1) {
    blinkFunc();
  }
  if (p.z > MINPRESSURE && p.z < MAXPRESSURE) {
    p.x = tft.height() - map(p.x, TS_MINX, TS_MAXX, 0, tft.height());
    p.y = tft.width() - map(p.y, TS_MINY, TS_MAXY, 0, tft.width());
    if (state == 1) {
      if (p.y > 289 && p.x < 31) {
        if (canPressButton()) {
          setStore();
          state = 2;
        }
      }
    }
    if (state == 2) {
      if (p.y > 289 && p.x < 31) {
        if (canPressButton()) {
          tft.fillRect(0, 30, 320, 240, BACKGROUND);
          setHome();
          state = 1;
        }
      }
    }
  }
}
