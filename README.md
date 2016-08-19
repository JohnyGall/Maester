# Maester - A platform for running tests on multiple Android devices in series.
## By [John Gallagher](http://johnygall.github.io/) & [Joe Campbell](http://jcamp1095.github.io)

### What is Maester?
Maester is a platform, written in Python and using [Appium](http://appium.io/),
for running unit tests on multiple Android devices/emulators in series.

### Why Does Maester Exist?
The Android ecosystem is fragmented, with a huge number of possible device and
operating system version combinations. Each of these combinations has their own
little quirks so running unit tests on as many combinations as possible is the
key to ensuring that an app works for many users. Unfortunately, running unit
tests on a series of devices using the raw Appium Python bindings is a
surprising amount of work. Maester abstracts away much of this work, meaning you
can focus on writing great unit tests that run across devices.

### How do I Install and Set Up Maester?
Maester is built on a stack of technologies, and you will need to install them
all correctly to use Maester.

1. Both Maester and Appium require Node, you can find install instructions for
Node [here](https://nodejs.org/en/download/)

2. Maester is built on top of Appium, you can install it from NPM by typing
`npm install -g appium`. Make sure you meet the minimum requirements for
[Appium](https://www.npmjs.com/package/appium) on Android
(chances are you do if you the Android dev tools installed)

3. We use [pm2](https://github.com/Unitech/pm2) for managing Appium servers, you can install pm2 by typing:
`npm install -g pm2`

4. Install Measter itself by typing `pip install Maester`  

5. Install all of the Python package Maester requires.
Change into the directory where you installed Maester and type
Type `pip install -r requirements.txt`

### Ok, Everything is Installed, Can You Help Me Get Started?
There'll be an example project soon!


### Wait, is this Name of this Package a Game of Thrones Reference?!
No! The name of this package is a Song of Ice and Fire reference!
