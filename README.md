# Google Coral Dev Board Setup Guide

#### 1. Requirements

``Note: Do not power the board or connect any cables until instructed to do so.``


Before you begin, collect the following hardware:

- A host computer running Linux (recommended), Mac, or Windows 10
- Python 3 installed
- One microSD card with at least 8 GB capacity and an adapter
- One USB-C power supply (2-3 A / 5 V), e.g., a phone charger
- One USB-C to USB-A cable (to connect to your computer)
- An available Wi-Fi connection (or Ethernet cable)

#### 2. Flash the Board

Follow [this link](https://coral.ai/docs/dev-board/get-started/#flash-the-board) to flash the board.

#### 3. Install MDT (on Host Computer)

#### Linux/Mac:

Open a terminal and execute the following commands:

```bash
$ python3 -m pip install --user mendel-development-tool
$ echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
$ source ~/.bash_profile
```
#### Windows:

```bash
$ python3 -m pip install --user mendel-development-tool
$ echo "alias mdt='winpty mdt'" >> ~/.bash_profile
$ source ~/.bash_profile
```

#### 4. Connect to the Board's Shell via MDT

For macOS 10.15 (Catalina) and later, USB-based MDT connections are not supported. Instead, MDT functions over the local network. 

- Connect the board to your computer using a USB-C cable to the board's "OTG" port. 
- On your host computer terminal, verify that MDT detects your board:
    
```bash
$ mdt devices
```
![Devices list](/images/mdt_shell.png) 

- Initiate the device shell using MDT

```bash
$ mdt shell
```
![Connect to the shell](/images/mdt_shell1.png) 

#### 5. Connect to the Internet

To connect the Coral board to the internet, you can use Ethernet or Wi-Fi depending on your setup. 

Follow [this link](https://coral.ai/docs/dev-board/get-started/#connect-internet) for detailed information

- Verify the connection:
```bash
$ nmcli connection show
```

![Network Connection](/images/network.png) 


#### 6. Update the Mendal Software and Dependencies.

```bash
$ sudo apt-get update 
 
$ sudo apt-get dist-upgrade
```

#### 7. Now run the Demo App in the Coral Board

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

#### 8. Run a model using the PyCoral API

![Macaw](/images/macaw.jpg) 

![Result 1](/images/result1.png) 

![Result 2](/images/result2.png) 

To demonstrate varying inference speeds, the example repeats the same inference five times. It prints the time to perform each inference and then the top classification result (the label ID/name and the confidence score, from 0 to 1.0).


### MacOS Connection Setup 

#### Method 1:

- Connect over USB OTG - You can also connect to the serial console without the micro-B USB cable, but only if your host computer is Linux or Mac, and your board is fully booted up.

![OTG Connection](/images/method1-otg.png)

- Run this command in the macOs Terminal wheather the coral board is connected or not.

```shell
ls /dev/cu.usbmodemcoralboard1
```

Output:
```shell
/dev/cu.usbmodemcoralboard1 
```
- Connect to the device shown using a serial console program such as screen as follows.

```shell
screen /dev/cu.usbmodemcoralboard1 115200
```

It will prompt you black screen.

- The default username and password are both `mendel` 
- When you're done, kill the screen session by pressing `CTRL+A K Y` to confirm.


#### Method 2: 

 

- Install the mendel-development tool 

 
```bash
prasannareddy@Prasi ~ % pip install mendel-development-tool 
```
 
- Export the mdt path to the .bash_profile 
```bash
 prasannareddy@Prasi ~ % export PATH="/Users/prasannareddy/Library/Python/3.10/bin:$PATH" 
```

- After editing the file, apply the changes to be effected.

```bash
source ~/.bash_profile. 
```
 

- Now, when you enter the command `mdt shell` you can connect to the coral board. 

*Note: Make sure your macOS network and coral board network should be the same* 
