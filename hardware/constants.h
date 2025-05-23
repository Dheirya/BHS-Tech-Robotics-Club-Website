#if defined(__SAM3X8E__)
    #undef __FlashStringHelper::F(string_literal)
    #define F(string_literal) string_literal
#endif

#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0
#define LCD_RESET A4
#define YP A3
#define XM A2
#define YM 9
#define XP 8
#define TS_MINX 120
#define TS_MAXX 900
#define TS_MINY 70
#define TS_MAXY 920
#define BLACK 0x0000
#define WHITE 0xFFFF
#define SKYBLUE 0x265f
#define DARKTHEME 0x65ba
#define THEME 0x0436
#define GREEN 0x1e4c
#define BACKGROUND 0xdfbf
#define YELLOW 0xfe8b
#define DARKYELLOW 0xfe47
#define MINPRESSURE 10
#define MAXPRESSURE 1000

MCUFRIEND_kbv tft;
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

int state = 1;
int homeState = 1;
int happiness = 60;
int health = 80;
int money = 200;
bool blink = false;
unsigned long previousMillis = 0;
unsigned long blinkStartTime = 0;
unsigned long nextBlinkTime = 0;
const long blinkDuration = 200;
const long minBlinkInterval = 5000;
const long maxBlinkInterval = 10000;
unsigned long lastButtonPressTime = 0;
const long buttonCooldown = 500;
