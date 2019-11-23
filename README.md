# csailab
How to Control a Raspberry Pi Robot by andriod APP
Method of controlling raspberry pi robot by andriod app:

For the robot we have updated the app control mode.

There is an appserver.py file in the server folder. After running it, you can open a server to monitor the connection of the mobile app.

If you have already installed a program for a robot product, just update its code:

Browse the root directory of the robot product in the Raspberry Pi terminal with the command cd [robot_name].

Update the project with sudo git pull.

If you want to set the appserver.py to run automatically, you can refer to the following methods:

With the command sudo nano startup.sh

Edit the startup.sh file and change the //PATH/server.py to //PATH/appserver.py

Press ctrl + x to exit, press y to save the changes, press enter to confirm.

Then it will automatically run the mobile terminal program the next time you turn it on.
