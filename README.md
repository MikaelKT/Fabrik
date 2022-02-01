# Factory

## Table Of Contents
* [Introduction](#Introduction)
* [Installation](#installation)
     * [VS Code](#First-you-install-a-development-environment-like-VS-Code)
     * [Python](#python)
* [Updates](#updates)
* [Definitions of functions](#Pin-definition)
     * [Other Functions](#other-functions)

#
## Introduction

#### Factory is a program that brings Fischertechnik's 536632 to life.

All you need is the Fischertechnik factory 526632, a PC, Python, a terminal and a development environment.

#
## Usage

#### first open your Terminal and write
```
ssh pi@your_Factory_ip_adress
```
#### into the bar.(replace "your_Factory_ip_adress" with your Factory ip adress. After that it can be that you need to put in a password)

#### now you must go into the folder where you saved the "Fabrik.py" file

#### 
```
cd your_folder_where_Fabrik.py_is_saved
```
#### (replace "your_folder_where_Fabrik.py_is_saved" with your Factory folder where the Fabrik.py file is.)
#### now you can easily start the program with
```
python3 Fabrik.py
```






#
## Installation

#### First you install a development environment like VS Code
#### If you use a raspberry pi then type in a terminal

```
sudo apt update
```
#### and then
```
sudo apt install code
```

\
if you are using a other device with a different operating system then you can also click on the [link](https://code.visualstudio.com/download) to download it from the official website

### Python


#### Now you should install python.

#### you can do it by clicking on the extension icon

<img src="images/erweiterungssymbol.png"
     style="float: ; margin-top: 0px;" />



#### then type "Python" in the searchbar and then click on Python from the publisher microsoft



<img src="images/pythonsearchbar.png"
     style="float: ; margin-top: 0px;" />

#### now click on install and wait for it finished

#
## Updates

If you want to update VS Code you only have to write

```
sudo apt update
```
#### and then
```
sudo apt upgrade code
```

#### in your terminal

\
By default VS Code is set up to auto-update for macOS and Windows users.


#
## Pin definition

##### the module revpimodio2 allows us direct access to the pins via their assigned name.
### Without pneumatics
\
O_1 = turntable rotates to the right\
O_2 = turntable turns to the left\
O_3 = conveyor belt\
O_4 = Polisher(saw idk)\
O_5 = Furnace move in\
O_6 = Furnace move out\
O_7 = Crane to the left\
O_8 = crane to the right\
O_9 = red lamp (burner)

### With pneumatics
\
O_10 = compressor on\
O_11 = suction cup on\
O_12 = crane suction cup holder down\
O_13 = Furnace door up\
O_14 = Pusher to push material
## Other functions
I_10 = turntable detection button\
\
\
\
1 at light barrier means = not interrupted (so it gets current)\
0 at light barrier means = interrupted (so it gets no current)
