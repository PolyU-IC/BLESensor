
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <M5StickC.h>


float accX = 0.0F;
float accY = 0.0F;
float accZ = 0.0F;

float gyroX = 0.0F;
float gyroY = 0.0F;
float gyroZ = 0.0F;

float pitch = 0.0F;
float roll  = 0.0F;
float yaw   = 0.0F;




BLECharacteristic *pCharacteristic;
bool deviceConnected = false;
int txValue = 0;

#define SERVICE_UUID "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHARACTERISTIC_UUID_TX "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"

class ServerCallbacks: public BLEServerCallbacks
{
void onConnect(BLEServer* pServer)
{
deviceConnected = true;  
  };
void onDisconnect(BLEServer* pServer)
{

  deviceConnected = false;
  
  
  };
  };
  
void setup() {

M5.begin();
M5.Lcd.fillScreen(BLACK);
delay(500);

M5.Lcd.setCursor(0, 10);
M5.Lcd.setTextColor(WHITE);
M5.Lcd.setTextSize(1);
M5.Lcd.setRotation(3);

//Init IMU 
M5.IMU.Init();


Serial.begin(9600);
BLEDevice::init("sensor_node_server");


//Create BLE server
BLEServer *pServer = BLEDevice::createServer();
pServer->setCallbacks(new ServerCallbacks());

//Create the BLE Service
BLEService *pService = pServer->createService(SERVICE_UUID);

pCharacteristic = pService->createCharacteristic(
  CHARACTERISTIC_UUID_TX,
  BLECharacteristic::PROPERTY_NOTIFY
  
  ); //Characteristic UUID and property of notify parameter

 //BLE2902 needed to notify

pCharacteristic->addDescriptor(new BLE2902());


//Start the service
pService->start();

//Start advertising
pServer->getAdvertising()->start();

Serial.println("Waiting for a client connection to notify");



}

//Server->advertising
//Characteristic ->notifying
//Characteristic -> add descriptor


char str[20];



void loop() {
M5.IMU.getAccelData(&accX,&accY,&accZ);
if(deviceConnected)
{
txValue = random(-10,20);

//Conversion of txValue
char txString[8];
dtostrf(txValue,1,2,txString);

sprintf(str," %5.2f   %5.2f   %5.2f   ",accX,accY,accZ);

//Setting the value of characteristic
pCharacteristic->setValue(str); //Accept the data format of char
pCharacteristic->notify();


M5.Lcd.setCursor(0, 30);
M5.Lcd.printf(" %5.2f   %5.2f   %5.2f   ", accX, accY, accZ);
M5.Lcd.setCursor(140, 30);
M5.Lcd.print("G");


delay(500);  
  }




  

}
