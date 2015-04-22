# GoPiGo-Wifi
Drive GoPiGo through the interwebs

1. Run the Server.py script in GPGSocketServer. It runs on port 8888 of the raspberry pi.
2. Run the Client.py script in GPGSocketClient. Make sure that the IP address for the server matches. There will be a small window
 that will appear where you can input the direction commands.
    - w : forward
    - s : backward
    - d : right
    - a : left
    - x : stop

- Dependencies for Python:
    - The venv folder should have the dependencies for the client, so you should be able to use the python intepreter found in there, otherwise:
        - ws4py
        - tkinter
    - The server requires Tornado webserver, as well as the standard gopigo library that ships with the dexter industries distribution for the raspberry pi. 