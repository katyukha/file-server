from settings import MEDIA_ROOT

import os.path

def save_file(file_obj, name):
    """ Saves file to MEDIA_ROOT

        @param file_obj: file-like object that represents file to be uploaded.
        @param name:     file will be saved wit hthis name
        @return:         length of file been saved
    """
    filepath = os.path.join(MEDIA_ROOT, name)
    f = open(filepath, 'wb')
    while True:
        chunk = file_obj.read(1024*100)
        if not chunk:
            break
        f.write(chunk)
    length = f.tell()
    f.close()
    return length

class AttrDict(dict):
    def __setattr__(self, name, value):
        self.update({name : value})

    def __getattribute__(self, name):
        try:
            return super(AttrDict, self).__getattribute__(name)
        except AttributeError:
            return self.get(name, None)
