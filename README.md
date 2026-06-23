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

a tiny virtual pet for the raspberry pi pico w.

micropython first. display and buttons after the board is alive.

## stack

```txt
board       -> raspberry pi pico w
runtime     -> micropython
language    -> python
editor      -> vscode
extension   -> micropico
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

install the `micropico` vscode extension.

download the pico w micropython firmware:

- https://micropython.org/download/RPI_PICO_W/

flash it:

```txt
hold BOOTSEL
plug in the pico w
copy the .uf2 file to RPI-RP2
wait for the drive to disappear
```

upload code from vscode:

```txt
cmd+shift+p -> MicroPico: Configure project
cmd+shift+p -> MicroPico: Upload project to Pico
```

## hello board

`main.py`

```py
from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
```

the onboard led blinking means the board, firmware, cable, and editor path are good.

## project shape

```txt
.
├─ .vscode/
│  └─ settings.json
├─ .gitignore
└─ README.md
```

expected later:

```txt
main.py       -> pico entrypoint
lib/          -> display, input, and pet state modules
tools/        -> local helper scripts, if needed
```

## hardware

```txt
now
├─ raspberry pi pico w
└─ micro usb cable

later
├─ display
├─ breadboard
└─ buttons
```
