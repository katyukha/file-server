from bottle import run
from bottle import mount
from apps.uploader import uploader

mount('/uploader', uploader, name = 'uploader')
run(host='firemage.mooo.com', port=8137)
