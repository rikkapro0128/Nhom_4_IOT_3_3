import random
import time
from grove.grove_servo import GroveServo
from grove.display.jhd1802 import JHD1802


def main():
    
    servo = GroveServo(16)
    lcd = JHD1802()
    
    while True:
        num = random.randrange(0, 180)
        servo.setAngle(num)
        lcd.setCursor(0, 0)
        lcd.write('Angle Random:{}'.format(num))
        print('Angle Random: {}'.format(num))
        time.sleep(1)

if __name__ == '__main__':
        main()

