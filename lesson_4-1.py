"""Lesson 4.1: Introduction to Networks
Network: A network is a group of entities that can communicate, even
though they are not directly connected.

Latency: The time it takes for a message to get from the source to the
destionation usually expressed in milliseconds (1/1000th of a second).

Bandwidth: The amount of information that can be transmitted per unit of
time usually expressed as Mbps (million bits per second).

Bit: The smallet unit of information expressed as an off/on (0/1) state.

Binary questions should have a 50/50 chance of having either answer for
the most efficient acquisition of information. 

Protocol: The set of rules that people agree to that tell you how two
entities talk to each other. For the web, client and server
communication is handled by the HyperText Transfer Protocol (HTTP). 
"""


"""Lesson 4.2: Make the Internet Work for You
protocol://host/path?query

Query Parameters
format: name = value
http://www.example.com/foo?query=stuff&query2=morestuff

First parameter is separated from the URL by ?
Following parameters are separated by &

Fragment
format: #fragment
http://www.example.com/foo#fragment

References a part of the page but is client-side, not host-side

Port
Followed by a colon
http://localhost:8000

HTTP: HyperText Transfer Protocol
http://www.example.com/foo

Request:
GET /foo HTTP/1.1
    Method: GET (or POST)
    Path: /foo
    Version: HTTP/1.1

Headers
Name: Value
    Host: www.example.com (because machines can have many names)
    User-Agent: Chrome (usually your browser)

Response:
HTTP/1.1 200 OK

Status Code and Reason Phrase
    200 - OK
    302 - Found
    404 - Not Found
    500 - Server Error

Headers
    Date: Tue Mar 2012 04:33:33 GMT
    Server: Apache /2.2.3 (Don't include this!)
    Content-Type: text/html;
    Content-Length: 1539

Servers
Static Content
    Pre-Written File
    Images
Dynamic
    Made on the fly
    Web Applications
"""