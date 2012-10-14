from bottle import mako_view as view
from bottle import get
from bottle import static_file
from bottle import url

from settings import STATIC_ROOT

@get('/static/:path#.+#', name='static_file')
def static(path):
    return static_file(path, root = STATIC_ROOT)

@get('/', name='home', apply=[view('index.mako')])
def index():
    return {
            'url' : url,
           }

