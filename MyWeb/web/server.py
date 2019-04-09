from wsgiref.simple_server import make_server


def application(env, start):
    # start_response("200 OK", [("Content-Type", "text/html")])
    start('200 OK', [('Content-Type', 'text/html')])
    sb = bytes("<h1>Welcome , web!</h1>".encode())
    return [sb]


httpd = make_server("", 9000, application)
print("Server Http on port 9000")
httpd.serve_forever()

