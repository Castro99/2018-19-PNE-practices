
import socketserver
import http.server
import termcolor
from P6.Seq import Seq

PORT = 8000


def seq_analysis(msg):

    actions = {}

    # The function calculations
    msg = msg.split("&")
    seq = Seq(msg.pop(0).split("=")[-1].upper())
    bases = "ACTG"

    if not all(c in bases for c in seq.strbases):
        actions = "Error"
        return actions

    actions.update({"Seq": seq.strbases})
    # Possible functions
    base = ""
    for request in msg:
        if "base" in request:
            base += request[-1]
        elif "count" in request or "perc" in request:
            operation = request.split("=")[-1]
            action = seq.call_function(operation, base)
            actions.update({"Result for " + base +" " + operation: action})

        elif request == "chk=on":
            action = seq.len()
            actions.update({"Len": action})


    return actions

    # Sending message back


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Printing the request line
        termcolor.cprint(self.requestline, 'blue')

        request = self.requestline.split()[1]
        actions = request.split("?")[-1]

        if self.path.startswith("/seq"):
            analysis = seq_analysis(actions)
            if analysis == "ERROR":
                f = open("error.html", 'r')
                contents = f.read()
                f.close()
            else:
                results = ""
                for key, value in analysis.items():
                    results += "<p>"+key+" : "+str(value)+"</p>"

                contents = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Sequence Analysis</title>
                    </head>
                    <body>
                     <h1>Result of the Analysis</h1>
                      {}
                      <a href="/">Home page</a>
                    </body>
                    </html>""".format(results)

        elif self.path == "/":
            f = open("Form.html", 'r')
            contents = f.read()
            f.close()

        else:
            f = open("Error.html", 'r')
            contents = f.read()
            f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()


        self.wfile.write(str.encode(contents))


# Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("")
print("Server Function finished")