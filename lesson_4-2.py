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