import time
import framebuf
from machine import Pin, SPI

spi = SPI(0, baudrate=10_000_000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
cs = Pin(17, Pin.OUT)
dc = Pin(21, Pin.OUT)
rst = Pin(20, Pin.OUT)

WIDTH = 128
HEIGHT = 128

buffer = bytearray(WIDTH * HEIGHT * 2)
fb = framebuf.FrameBuffer(buffer, WIDTH, HEIGHT, framebuf.RGB565)

def cmd(c):
    cs(0)
    dc(0)
    spi.write(bytearray([c]))
    cs(1)

def data(d):
    cs(0)
    dc(1)
    spi.write(bytearray([d]))
    cs(1)

def reset():
    rst(1)
    time.sleep_ms(50)
    rst(0)
    time.sleep_ms(50)
    rst(1)
    time.sleep_ms(50)

def init():
    reset()

    cmd(0x01)
    time.sleep_ms(150)

    cmd(0x11)
    time.sleep_ms(150)

    cmd(0x3A)
    data(0x05)

    cmd(0x36)
    data(0xC8)

    cmd(0x29)
    time.sleep_ms(100)

def window(x0, y0, x1, y1):
    cmd(0x2A)
    cs(0)
    dc(1)
    spi.write(bytearray([0, x0, 0, x1]))
    cs(1)

    cmd(0x2B)
    cs(0)
    dc(1)
    spi.write(bytearray([0, y0, 0, y1]))
    cs(1)

    cmd(0x2C)

def show():
    window(0, 0, WIDTH - 1, HEIGHT - 1)
    cs(0)
    dc(1)
    spi.write(buffer)
    cs(1)

init()

fb.fill(0x0000)
fb.text("angi lila", 22, 35, 0xFFFF)
fb.text("hello world", 18, 55, 0xFFFF)
show()

while True:
    time.sleep(1)