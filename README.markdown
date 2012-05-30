Video Chat
=================

A simple video chat client implementation using sockets. 
It's created and maintained by [Anil Shanbhag](http://github.com/anilshanbhag) & [Ashwin Paranjpee](http://www.cse.iitb.ac.in/~ashwinp), IIT Bombay.


Hack Night
-----------
This application was developed in Hack Night , a fun coding weekend . This project is only for educational purposes .


Installation
----------
On one session  
> $ python server.py
Another session
> $ python client.py


Working
----------
Sockets are the main thing in this app. Client socket connects to server socket . Py OpenCV was used to retrieve frames from webcam feed , they are compressed to jpg and transmitted . At the other end the image is decompressed and shown.


Copyright and license
---------------------

Copyright 2012 Anil Shanbhag

Distributed under GPL v2
