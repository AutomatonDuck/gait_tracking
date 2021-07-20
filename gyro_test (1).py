import smbus
from time import sleep
import math

#IMU intialization
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0X19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0X38
ACCEL_XOUT_H = 0X3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0X3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

#testing code
gx_list = []

def MPU_init():
    #write to sample rate
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #write to power managment
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #write to configuration
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #write to GYRO config
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    
    #write to interrupt register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    
    value = ((high << 8)|low)
    
    if(value > 32768):
        value = value - 65536
    return value

bus = smbus.SMBus(1)
Device_Address = 0x68

MPU_init()

def step_count(list_name):
    if((max(list_name) - min(list_name)) >= 5):
        print("Step Detected")
    list_name.clear()
    pass

print("Reading Data")

while True:
    
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
    
    #AFS_SEL = 0
    Ax = acc_x/16384.0
    Ay = acc_y/16384.0
    Az = acc_z/16384.0
    
    #AFS_SEL = 0
    Gx = gyro_x/131.0
    gx_list.append(Gx)
    if(len(gx_list) == 5):
       step_count(gx_list)
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0
    
    print(f"Gx = {Gx:.3f} \u00b0  \tGy = {Gy:.3f} \u00b0 \tGz = {Gz:.3f} \u00b0  \tAx = {Ax:.3f} g  \tAy = {Ay:.3f} g  \tAz = {Az:.3f} g")
    sleep(0.5)