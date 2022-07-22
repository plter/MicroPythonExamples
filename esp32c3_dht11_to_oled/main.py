import machine, dht, uasyncio

from ssd1306 import SSD1306_I2C

OLED_WIDTH = 128
OLED_HEIGHT = 64


def off_builtin_leds():
    p = machine.Pin(12, machine.Pin.OUT)
    p.off()
    p = machine.Pin(13, machine.Pin.OUT)
    p.off()


async def show_data(oled: SSD1306_I2C, d):
    while True:
        d.measure()
        oled.fill(0)
        oled.text(f"T: {d.temperature()}'C", 0, 0)
        oled.text(f"H: {d.humidity()}%", 0, 8)
        oled.show()
        await uasyncio.sleep(2)
    pass


async def main():
    off_builtin_leds()

    sda = machine.Pin(4)
    scl = machine.Pin(5)
    i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

    oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
    d = dht.DHT11(machine.Pin(8))

    await show_data(oled, d)


if __name__ == "__main__":
    uasyncio.run(main())
