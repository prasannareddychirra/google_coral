# Google Coral Dev Board Setup Guide

## Requirements

**Note: Do not power the board or connect any cables until instructed to do so.**

Before you begin, collect the following hardware:

- A host computer running Linux (recommended), Mac, or Windows 10
- Python 3 installed
- One microSD card with at least 8 GB capacity and an adapter
- One USB-C power supply (2-3 A / 5 V), e.g., a phone charger
- One USB-C to USB-A cable (to connect to your computer)
- An available Wi-Fi connection (or Ethernet cable)

## Flash the Board

Follow [this link](https://coral.ai/docs/dev-board/get-started/#flash-the-board) to flash the board.

## Install MDT (on Host Computer)

### Linux/Mac:

Open a terminal and execute the following commands:

```bash
$ python3 -m pip install --user mendel-development-tool
$ echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
$ source ~/.bash_profile

### Windows:

$ python3 -m pip install --user mendel-development-tool
$ echo "alias mdt='winpty mdt'" >> ~/.bash_profile
$ source ~/.bash_profile
```

### Connect to the Board's Shell via MDT

For macOS 10.15 (Catalina) and later, USB-based MDT connections are not supported. Instead, MDT functions over the local network. 

- Connect the board to your computer using a USB-C cable to the board's "OTG" port. 
- On your host computer terminal, verify that MDT detects your board:
    
```bash
$ mdt devices
```
