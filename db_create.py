# -*- coding:utf-8 -*-

from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_TRACK_MODIFICATIONS
from application import db
import os.path
db.create_all()
