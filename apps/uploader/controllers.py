#!/usr/bin/env python
import bottle
from bottle import route, run
from bottle import mako_view as view
from bottle import mako_template as template
from bottle import request
from bottle import static_file
from bottle import HTTPError
from bottle.ext import sqlalchemy

from application import uploader

from models import File

from settings import MEDIA_ROOT

@uploader.get('/', name='home')
@view('index.html')
def index(db):
    files = db.query(File).all()
    return {
             'files' : files,
             'url'   : uploader.get_url,
           }

@uploader.post('/upload/', name='upload')
def upload(db):
    name = request.forms.name
    data = request.files.data
    comment = request.forms.comment
    if name and data!=u'' and data.file:
        raw = data.file.read()
        filename = data.filename
        f = open(MEDIA_ROOT+filename, 'wb')
        f.write(raw)
        f.close()
        file_obj = File(name, filename, comment)
        db.add(file_obj)
        return { 'file' : file,
                 'file_loaded' : True }

    return {'file_loaded' : False}

@uploader.get('/file/<filename>', name='file')
def send_file(filename, db):
    file = db.query(File).filter_by(filename=filename).first()
    if file:
        return static_file(file.filename, root = MEDIA_ROOT)
    return HTTPError(404, 'File <%s(%s)> not found.' % (file.name, file.filename))



