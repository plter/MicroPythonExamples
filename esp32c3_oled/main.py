import machine

from ssd1306 import SSD1306_I2C

OLED_WIDTH = 128
OLED_HEIGHT = 64

if __name__ == "__main__":
    sda = machine.Pin(4)
    scl = machine.Pin(5)
    i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

    oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
    oled.fill(0)
    oled.text(f"Hello World", 0, 0)
    oled.show()
