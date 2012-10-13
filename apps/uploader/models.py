from sqlalchemy import Column, Integer, Sequence, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class File(Base):
    __tablename__ = 'downloader_file'
    id          = Column(Integer, Sequence('id_seq'), primary_key=True)
    name        = Column(String(256))
    filename    = Column(String(256))
    comment     = Column(Text())

    def __init__(self, name, filename, comment=None):
        self.name     = name
        self.filename = filename
        self.comment  = comment

    def __repr__(self):
        return "<Entity('%d', '%s')>" % (self.id, self.name)

