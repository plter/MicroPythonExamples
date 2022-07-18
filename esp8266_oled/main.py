import ssd1306
from machine import Pin, I2C

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

if __name__ == '__main__':
    display.fill(0)
    display.text('Hello World', 0, 0, 1)
    display.show()
