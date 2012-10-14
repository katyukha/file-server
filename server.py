from bottle import run
from bottle import mount
from bottle import debug

from controllers import *
from apps.uploader import uploader

mount('/uploader', uploader, name = 'uploader')





if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default='localhost', dest='host', help="Host name to listen to")
    parser.add_argument("--port", default='8000', type=int, dest='port', help='Port to listen to'),
    parser.add_argument("--server", default='wsgiref', dest='server', help='Server adapter to use'),
    parser.add_argument("--debug", action='store_true', help='Enable dubug mode'),
    parser.add_argument("--reload", action="store_true", help="auto-reload on file changes."),
    args = parser.parse_args()

    debug(args.debug)
    run(host=args.host, port=args.port, server=args.server, reloader=args.reload)
else:
    from bottle import app
    application = app()
