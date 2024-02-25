from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server=HTTPServer, handlerClass=SimpleHTTPRequestHandler):
    serverAddress = ('127.0.0.1', 8000)
    httpd = server(serverAddress, handlerClass)
    print('\033[33m'+"[~] Starting httpd..." + '\033[0m')
    httpd.serve_forever()

run()
