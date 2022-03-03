import time
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802

def main():
    
    sensor = DHT('11', 5)
    lcd = JHD1802()
    
    while True:
        humi, temp = sensor.read()
        lcd.setCursor(0, 0)
        lcd.write('Nhiet do: {}C'.format(temp))
        lcd.setCursor(1, 0)
        lcd.write('Do am: {}%'.format(humi))
        time.sleep(1)
        
if __name__ == '__main__':
    main()
