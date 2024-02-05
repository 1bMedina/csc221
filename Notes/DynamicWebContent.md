# Dynamic Web Content Notes 

## Video 1: Web applications and the request/response cycle
- we will be looking at the technology used to create websites
- front end consists of HTML, CSS, DOM, Javascript, JQuery
- back end consists of Django, Flask, Sqlite3, MySQL
- the browser is an application
- when a user clicks on a button it is intercepted by the application


## Video 2: Exploring the HTTP
- was created in 1990
- protocal-host-document
- the dominant application layre protocal on the internet
- invented to retrieve  HTML, images, Documents - RSS, Web Services and more

## Video 3: Using sockets to make network connections in python
- sockets are computer phone calls
- there is a protocal to tell who talks first
- application process < internet > application process
- a port is an application-specific or process-specific software communications endpoint.

## Video 4: Building a simple web browser in python
```
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org?page1.tm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data=mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode(),end='')
mysock.close()
```
- creates a socket in your computer
- socket.socket makes a phone
- mysock.connect dials the phone
- browser developer mode can be really healpful when debugging

## Video 5: Building a simple HTTP server in python
- a browser is an application that sends a get request, the server does something and sends the response
- the server already exists
- client must speak first

## Understanding browser developer mode
- 404 means the page wasnt found
- it grabs everything like links, css, fonts, javascript and builds up the request and the time it takes to grab them.
