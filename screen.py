import time
from machine import Pin, SPI

WIDTH = 128
HEIGHT = 128

BLACK = 0x0000
WHITE = 0xFFFF

# RP2350 microcontroller / 2 hardware SPI controllers
spi = SPI(
    0,
    baudrate=10_000_000,
    polarity=0,
    phase=0,
    sck=Pin(18), # clock wire
    mosi=Pin(19) # data wire, pico sends lcd receives
)

cs = Pin(17, Pin.OUT) # chip select
dc = Pin(21, Pin.OUT) # data/command
rst = Pin(20, Pin.OUT) # reset

def reset():
    rst.value(1)
    time.sleep_ms(50)
    rst.value(0)
    time.sleep_ms(50)
    rst.value(1)
    time.sleep_ms(50)
    
def send_data_or_command(value, is_data):
    cs.value(0)
    dc.value(is_data)
    spi.write(bytearray([value]))
    cs.value(1)

def cmd(value):
    send_data_or_command(value, False)

def data(value):
    send_data_or_command(value, True)
    
def data16(value):
    data(value >> 8)
    data(value & 0xFF)

reset()
cmd(0x2A) # columns
data16(10)
data16(80)
cmd(0x2B) # rows
data16(20)
data16(20)
cmd(0x2C) # write to RAM
data16(BLACK)