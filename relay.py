import time
from grove.grove_relay import GroveRelay

relay = GroveRelay(5)


while True:
    relay.on()
    time.sleep(1)
    relay.off()
    time.sleep(1)