import time
from grove.display.jhd1802 import JHD1802

def main():
    lcd = JHD1802()
    
    lcd.setCursor(0, 0)
    lcd.write('     Nhom 4')
    lcd.setCursor(1, 0)
    lcd.write(' Thuc hanh IOT')
if __name__ == '__main__':
    main()