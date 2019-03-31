#Exercise II other form lesson 15

import http.server
import socketserver
import termcolor


PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open("Form2.html", 'r')
            contents = f.read()
            f.close()
        elif '/echo' in self.path:
            if 'chk=on' in self.path:
                message = self.path.split('=')[1]
                message2 = message.split('&')[0]
                message2 = message2.upper()
                contents = """<html><body style="background-color: red;"><h4>RECIEVED:</h4>"""+ message2 + """<br><a href="/">[MAIN PAGE]</a><html><body>"""
            else:
                message = self.path.split('=')[1]
                contents = """<html><body style="background-color: red;"><h4>RECIEVED:</h4>""" + message + """<br><a href="/">[MAIN PAGE]</a><html><body>"""
        else:
            f = open('Error.html','r')
            contents = f.read()
            f.close()


        # Generating the response message
        self.send_response(200)


        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


#Main program

Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    httpd.serve_forever()


print("")
print("The server is Stopped")