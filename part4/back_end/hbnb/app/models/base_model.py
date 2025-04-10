#!/usr/bin/python3

import uuid
from datetime import datetime
from hbnb.app import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

    def save(self):
        
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()