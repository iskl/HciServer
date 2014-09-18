# Extend the Sensory Ability of Desktop Computer using Mobile Device (Server Side)

## Description

This project is the server side of my coursework for Human Computer Interaction class.

The project, made up of server side and client side, intends to extend the sensory ability of desktop computer, by using mobile devices like an Android Phone. For instance, user can shake the phone in a specific orientation to control the volume of playing movie on computor up and down, or rollover the phone to pause the playing movie.

The reasons for coming up with this project consist of these aspects as follows:

 * Desktop computer is short of sensory ability. Microphone, camera and touchpad are not standard equipped.
 * The sensors of mobile devices are abundant and are often standard epuipped.
 * The way to combine desktop computer and mobile device is convenient.

This project is a prototype of sensor combination between desktop computer browser and mobile phone. It combines the two by using Internet and QR code. User can use gesture effected on mobile phone to control the behaviour of movie playing in the computer.

The figure blow illustrates the framework of this project (both server side and client side)

![image](https://raw.githubusercontent.com/iskl/HciServer/master/docs/fig.png)

## Technical Detail

The server side consists of front end and back end.

### Back End

For back end, I use Flask, a lightweight web server framework written in Python, to act as the central controller of the whole plan. It receivers the HTTP requests from front end (the web page) and client side (the Android app). The trigger from client side registers the commands to load to a buffer. The query from front end extract the commands. It is worth mentioning that, when the front end has operated the command, it will push an notification to the back end naming as "Ack" and when back end receives the notification, it deletes the regestered commands in buffer.

So far, The implemented commands includes:

 * Play
 * Pause
 * Volume Up
 * Volume Down
 * Fullscreen
 * Ack
 
New command can be added conveniently if the work of gesture detector is done.

The back end is also responsible for storing static web pages and static resources incluing the movie file.

### Front end

The front end is a (so far, only one page) dynamic web page written in HTML/CSS and Javascript, with jQuery framework equipped. An AJAX polling is executed initially to query the pending command in back end. The front end use jPlayer, a plugin based on jQuery, to act as movie player. When the polling procedure receives command, the command will be transfered to jPlayer to affect.

A QR code is shown on web page, to combine the client side and server side together at first. The phone shall capture the QR code using any QR Apps before controlling. The detailed information can be found in README.md in client side.

## Steps of Server Deployment

The server side project can be deployed on any environment where have Python runtime running, e.g. Ubuntu 14.04 x64, Debain 7.10 x64 and Windows 7 SP1 x86.

The tutorial below assumes to deploy on Ubuntu 14.04 x64.

 1. Install Python runtime and related libs.

 ```shell
 sudo apt-get install build-essential python python-dev
 ```
 
 * Install pip and install Flask using pip.
 
 ```shell
 sudo apt-get install pip
 sudo pip install flask
 ```
 * Install git and clone this repository from github
 
 ```shell
 sudo apt-get install git
 git clone https://github.com/iskl/HciServer.git
 ```
 
 * Run the server
 
 ```shell
 cd HciServer
 python HciServer.py
 ```
 The server is now runing and you can view the web page at http://127.0.0.1:5000

Note: It is assumed that the server occupied the IP address of 192.168.200.167. If not, it can be modified by

```shell
ifconfig eth0 192.168.200.167
```

# Reference:

 * [Flask](http://flask.pocoo.org/) Microframework for Python based on Werkzeug, Jinja 2.
