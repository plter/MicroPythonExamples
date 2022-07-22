import machine

from ssd1306 import SSD1306_I2C

OLED_WIDTH = 128
OLED_HEIGHT = 64


def off_builtin_leds():
    p = machine.Pin(12, machine.Pin.OUT)
    p.off()
    p = machine.Pin(13, machine.Pin.OUT)
    p.off()


if __name__ == "__main__":
    off_builtin_leds()

    sda = machine.Pin(4)
    scl = machine.Pin(5)
    i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

    oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
    oled.fill(0)
    oled.text(f"Hello World", 0, 0)
    oled.show()
