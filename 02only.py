import sys
import time
import math
sys.path.append("../..")
from DFRobot_Oxygen import *

COLLECT_NUMBER   = 10              # collect number, the collection range is 1-100
IIC_MODE         = 0x01            # default use IIC1

'''
  The first  parameter is to select iic0 or iic1
  The second parameter is the iic device address
  The default address for iic is ADDRESS_3
  ADDRESS_0                 = 0x70
  ADDRESS_1                 = 0x71
  ADDRESS_2                 = 0x72
  ADDRESS_3                 = 0x73
'''
oxygen = DFRobot_Oxygen_IIC(IIC_MODE ,ADDRESS_3)
def loop():
  oxygen_data = oxygen.get_oxygen_data(COLLECT_NUMBER)
  print("oxygen concentration is %4.2f %%vol"%oxygen_data)
  time.sleep(1)

if __name__ == "__main__":
  while True:
    loop()