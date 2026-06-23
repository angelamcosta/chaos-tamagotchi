import time
from machine import Pin, SPI

spi = SPI(
    0,
    baudrate=10_000_000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
)

cs = Pin(17, Pin.OUT)
rst = Pin(20, Pin.OUT)
dc = Pin(21, Pin.OUT)


def cmd(c):
    cs.off()
    dc.off()
    spi.write(bytearray([c]))
    cs.on()


def data(d):
    cs.off()
    dc.on()
    spi.write(bytearray([d]))
    cs.on()


def data_bytes(b):
    cs.off()
    dc.on()
    spi.write(b)
    cs.on()


def reset():
    rst.off()
    time.sleep(0.1)
    rst.on()
    time.sleep(0.1)


def init():
    reset()

    cmd(0x01)
    time.sleep(0.15)

    cmd(0x11)
    time.sleep(0.15)

    cmd(0x3A)
    data(0x05)

    cmd(0x29)
    time.sleep(0.1)


def set_window(x0, y0, x1, y1):
    cmd(0x2A)
    data_bytes(bytearray([0x00, x0, 0x00, x1]))

    cmd(0x2B)
    data_bytes(bytearray([0x00, y0, 0x00, y1]))

    cmd(0x2C)


def fill_screen(color):
    high = color >> 8
    low = color & 0xFF
    row = bytearray([high, low] * 128)

    set_window(0, 0, 127, 127)

    for _ in range(128):
        data_bytes(row)


init()

while True:
    print("red")
    fill_screen(0xF800)
    time.sleep(1)

    print("green")
    fill_screen(0x07E0)
    time.sleep(1)

    print("blue")
    fill_screen(0x001F)
    time.sleep(1)
