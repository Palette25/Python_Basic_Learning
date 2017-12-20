#------------------------------------------------WSGI_server------------------------------------------------#
from wsgiref.simple_server import make_server
from WSGI_hello import application

httpd  = make_server('', 9000, application)
print('Serving HTTP on port 9000')
httpd.serve_forever()
