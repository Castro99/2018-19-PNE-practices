#Exercise I other form lesson 15

import http.server
import socketserver
import termcolor

PORT = 8000

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        name = self.path.split('?')

        #--- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if name[0] == '/':
            f = open('Form1.html', 'r')
            contents = f.read()
        elif name[0] == '/echo':
            name1 = name[1].split('=')
            contents = """<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>ECHO MESSAGE</title>
            </head>
            <body>"""
            contents += "<p>{}</p>".format(name1[1])
            contents += """<a href="/">[MAIN PAGE]</a>
            </body>
            </html>"""

        else:
            f = open('Error.html', 'r')
            contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        #--- Sending the body of the response message
        self.wfile.write(str.encode(contents))

#--- main program
with socketserver.TCPServer(('', PORT), TestHandler) as httpd:
    print('Serving at PORT: {}'.format(PORT))

    try:
       httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
print('The server is stopped')
