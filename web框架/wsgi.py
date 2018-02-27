from wsgiref.simple_server import make_server

def RunServer(envuron, start_response):
    start_response('200 ok', [('Content-Tyep','text/html')])
    return ['<h1>hello,web</h1>'.encode('utf-8')]

if __name__ == "__main__":
    httpd = make_server('', 8001, RunServer)
    print('server on 8001')
    httpd.serve_forever()