# chaos-tamagotchi

```txt
        .      *        .
   *        .       *        .

      ██████╗██╗  ██╗ █████╗  ██████╗ ███████╗
     ██╔════╝██║  ██║██╔══██╗██╔═══██╗██╔════╝
     ██║     ███████║███████║██║   ██║███████╗
     ██║     ██╔══██║██╔══██║██║   ██║╚════██║
     ╚██████╗██║  ██║██║  ██║╚██████╔╝███████║
      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

              < pocket void pet >
```

a tiny virtual pet for the raspberry pi pico w with an st7735 display.

micropython first. display bring-up now. buttons and pet state next.

## stack

```txt
board       -> raspberry pi pico w
runtime     -> micropython
language    -> python
editor      -> thonny
env         -> local python venv for tools only
```

## local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

there are no required python packages yet. the venv is here for later tooling, scripts, formatters, or device helpers.

## pico setup

install Thonny:

- https://thonny.org/

download the pico w micropython firmware:

- https://micropython.org/download/RPI_PICO_W/

flash it:

```txt
hold BOOTSEL
plug in the pico w
copy the .uf2 file to RPI-RP2
wait for the drive to disappear
```

upload code from Thonny:

```txt
open main.py
save to Raspberry Pi Pico as main.py
run main.py
```

## display text test

`main.py` is currently standalone so it can be saved to the Pico and run from
Thonny without uploading extra modules. It initializes the ST7735 over SPI0,
fills the display black, and renders:

```txt
angi lila
hello world
```

The earlier red, green, and blue smoke test confirmed the pico, micropython
firmware, spi wiring, and st7735 initialization path are good.

## display wiring

```txt
st7735     -> pico w
SCK/SCL    -> GP18
SDA/MOSI   -> GP19
CS         -> GP17
RST/RES    -> GP20
DC/A0      -> GP21
VCC        -> 3V3
GND        -> GND
```

## project shape

```txt
.
├─ .vscode/
│  └─ settings.json
├─ CHANGELOG.md
├─ .gitignore
├─ main.py
└─ README.md
```

expected later:

```txt
lib/          -> display, input, and pet state modules
tools/        -> local helper scripts, if needed
```

## hardware

```txt
now
├─ st7735 display
├─ raspberry pi pico w
├─ breadboard/jumper wires
└─ micro usb cable

later
└─ buttons
```

## documentation

- [getting started with Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
- [thonny](https://thonny.org/)
- [picozero](https://picozero.readthedocs.io/en/latest/)
