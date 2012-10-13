#!/usr/bin/env python
import bottle
from bottle import route, run
from bottle import mako_view as view
from bottle import mako_template as template
from bottle import request
from bottle import static_file
from bottle import HTTPError

from application import uploader


from settings import MEDIA_ROOT

from utils import save_file
from utils import AttrDict

@uploader.get('/', name='home',apply=[view('uploader/index.mako')])
def index(rdb):
    file_ids = rdb.lrange('file:global:ids',-11,-1) or []    # get ids of last files
    file_ids.reverse()
    files    = []
    for file_id in file_ids:
        obj = rdb.hgetall('file:%s:data' % file_id)
        obj = AttrDict(obj)
        files.append(obj)

    return {
             'files' : files,
             'url'   : uploader.get_url,
           }

@uploader.post('/upload/', name='upload', apply=[view('uploader/upload.mako')])
def upload(rdb):
    name = request.forms.name
    filedata = request.files.file
    description = request.forms.description
    if name and filedata!=u'' and filedata.file:
        id = rdb.incr('file:global:last-id')
        filename = filedata.filename

        filelen = save_file(filedata.file, "%s.%s" % (id,filename))

        #writing filedata to redis
        data = dict( id = id,
                     name = name,
                     filename = filename,
                   )
        if description:
            data.update(description=description)

        rdb.hmset('file:%s:data'%id, data)
        rdb.rpush('file:global:ids', id)
        return { 'filename'    : filename,
                 'filelen'     : filelen,
                 'file_loaded' : True }

    return {'file_loaded' : False}

@uploader.get('/file/<id>/<filename>', name='file')
def send_file(id, filename, rdb):
    return static_file("%s.%s" % (id,filename), root = MEDIA_ROOT)
    return HTTPError(404, 'File not found.')



