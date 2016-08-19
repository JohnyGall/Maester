# maester - A platform for running tests on multiple Android devices in series.
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
maester is built on a stack of technologies, and you will need to install them
all correctly to use maester.

1. Both maester and Appium require Node, you can find install instructions for
Node [here](https://nodejs.org/en/download/)

2. maester is built on top of Appium, you can install it from NPM by typing `npm install -g appium`
Make sure you meet the minimum requirements for
[Appium](https://www.npmjs.com/package/appium) on Android
(chances are you do if you the Android dev tools installed)

3. We use pm2 for managing Appium servers, you can install pm2 by typing: `npm install -g pm2`

4. Install all of the Python package Maester requires. Type pip install
-r requirements.txt

### Ok, Everything is Installed, Can You Help Me Get Started?
Sure! We have an example project [here](https://github.com/JohnyGall/Maester-Example)
that demonstrates how to write tests for a free and open source calculator app   
