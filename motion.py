import time
from grove.grove_relay import GroveRelay
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor

def main():
    
    sensor = GroveMiniPIRMotionSensor(24)
    
    def on_detact():
        print('Phat hien chuyen dong!!!')
        time.sleep(1)
    
    sensor.on_detact = on_detact
    
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
