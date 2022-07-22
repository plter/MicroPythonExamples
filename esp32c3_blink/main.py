from machine import Pin
import uasyncio


async def main():
    p = Pin(12, Pin.OUT)
    while True:
        p.on()
        await uasyncio.sleep(1)
        p.off()
        await uasyncio.sleep(1)
    pass


if __name__ == '__main__':
    uasyncio.run(main())
