# documenting the learning process

## what the hardware is doing

```t
LCD GND -> Pico GND
LCD VCC -> Pico 3V3(OUT)
LCD SCL -> Pico GP18
LCD SDA -> Pico GP19
LCD RES -> Pico GP20
LCD DC  -> Pico GP21
LCD CS  -> Pico GP17
LCD BL  -> Pico 3V3(OUT)
```

- VCC/GND provide power
- BL powers the backlight
- SCL and SDA are used for SPI communication
- CS selects the display
- DC tells the display whether the next byte is a command or display data
- RES resets the controller

## understanding SPI

```py
spi = SPI(
    0,
    baudrate=10_000_000,
    sck=Pin(18),
    mosi=Pin(19)
)
```

SPI is a communication protocol. the pico sends bits to the display over a data wire (G19) while a clock wire (G18) provides timing. the display receives commands and pixels through this connection.

## setting up pins

```py
cs = Pin(17, Pin.OUT)
dc = Pin(21, Pin.OUT)
rst = Pin(20, Pin.OUT)
```

these pins are used to control the display.

> dc.value(0) mens that the next bytes are commands/instructions. dc.value(1) means that the next bytes are data
> CS = 0 → listen
> CS = 1 → ignore
> hardware usually fails silently

## the frame buffer

```py
buffer = bytearray(WIDTH * HEIGHT * 2)
fb = framebuf.FrameBuffer(
    buffer,
    WIDTH,
    HEIGHT,
    framebuf.RGB565
)
```

instead of drawing directly to the display, we draw into memory first. for a 128x128 RGB565 display (my case):

```txt
128 × 128 pixels
2 bytes per pixel
128 × 128 × 2
= 32768 bytes
```

> [!IMPORTANT]
> for the LCD, the matrix model is screen[y][x]

## drawing text

```py
fb.fill(0x0000)
fb.text(
    "angie lila",
    22,
    35,
    0xFFFF
)
```

the text is drawn into memory, not yet onto the physical display.

## sending the image to the LCD

show() transfers the frame buffer to the LCD over SPI. Until show() runs, the LCD cannot see the changes.