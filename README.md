# Google Coral Dev Board Setup Guide

### 1. Requirements
<span style="color:red">Note: Do not power the board or connect any cables until instructed to do so.</span>


Before you begin, collect the following hardware:

- A host computer running Linux (recommended), Mac, or Windows 10
- Python 3 installed
- One microSD card with at least 8 GB capacity and an adapter
- One USB-C power supply (2-3 A / 5 V), e.g., a phone charger
- One USB-C to USB-A cable (to connect to your computer)
- An available Wi-Fi connection (or Ethernet cable)

## 2. Flash the Board

Follow [this link](https://coral.ai/docs/dev-board/get-started/#flash-the-board) to flash the board.

## 3. Install MDT (on Host Computer)

### Linux/Mac:

Open a terminal and execute the following commands:

```bash
$ python3 -m pip install --user mendel-development-tool
$ echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
$ source ~/.bash_profile
```
### Windows:
```bash
$ python3 -m pip install --user mendel-development-tool
$ echo "alias mdt='winpty mdt'" >> ~/.bash_profile
$ source ~/.bash_profile
```

### 4. Connect to the Board's Shell via MDT

For macOS 10.15 (Catalina) and later, USB-based MDT connections are not supported. Instead, MDT functions over the local network. 

- Connect the board to your computer using a USB-C cable to the board's "OTG" port. 
- On your host computer terminal, verify that MDT detects your board:
    
```bash
$ mdt devices
```
- Initiate the device shell using MDT
```bash
$ mdt shell
```
### 5. Connect to the Internet
To connect the Coral board to the internet, you can use Ethernet or Wi-Fi depending on your setup. 

Follow [this link](https://coral.ai/docs/dev-board/get-started/#connect-internet) for detailed information

- Verify the connection:
```bash
$ nmcli connection show
```

### 6. Update the Mendal Software and Dependencies.
```bash
$ sudo apt-get update 
 
$ sudo apt-get dist-upgrade
```

### 7. Now run the Demo App in the Coral Board

- In Dev board terminal
```bash
$ edgetpu_demo –stream
```
If connected via MDT over USB On your desktop (connected to the Dev Board via USB), open http://192.168.100.2:4664 in a web browser. 
This should display a video playing in your browser. The demo uses a pre-recorded video to highlight real-time object detection by the MobileNet model running on the Dev Board. 

- If you have a monitor attached to the Dev Board, you can see the demo directly on that screen.
```bash
$ edgetpu_demo –device
```
This displays the demo directly on the connected monitor. 

### 8. Run a model using the PyCoral API

