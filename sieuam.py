import time
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.grove_relay import GroveRelay
from grove.display.jhd1802 import JHD1802
from grove.grove_servo import GroveServo


def main():
    
    sensor = GroveUltrasonicRanger(22)
    servo = GroveServo(16)
    relay = GroveRelay(18)
    lcd = JHD1802()
    
    while True:
        distance = round(sensor.get_distance(), 2)
        print('Range = {}(cm)'.format(distance))
        lcd.setCursor(0, 0)
        lcd.write('Khoang cach: {}cm'.format(distance))
        if distance > 20:
            relay.on()
            servo.setAngle(0)
        else:
            relay.off()
            servo.setAngle(180)

if __name__ == '__main__':
    main()