#!/usr/bin/python
import bme280
import I2C_LCD_driver
from DFRobot_Oxygen import *


mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Hello Friends!", 1)
time.sleep(2)

COLLECT_NUMBER   = 10              # collect number, the collection range is 1-100
IIC_MODE         = 0x01            # default use IIC1
oxygen = DFRobot_Oxygen_IIC(IIC_MODE ,ADDRESS_3)
def loop():
    oxygen_data = oxygen.get_oxygen_data(COLLECT_NUMBER)
    temperature,pressure,humidity = bme280.readBME280All()
    
    string1 = "O2: %4.1f"%oxygen_data  
    string2 = " T: %4.1f"% temperature
    mylcd.lcd_display_string(string1+string2, 1)
    print(string1," ",string2)
    string3 = "P :%5.1f"%pressure
    string4 = " H: %4.1f"%humidity
    mylcd.lcd_display_string(string3+string4, 2)
    print (string3," ",string4)
    time.sleep(2)


if __name__ == "__main__":
  while True:
    loop()