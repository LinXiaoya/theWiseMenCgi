# -*- coding=utf8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'wisemen.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = "0AQ38M80GtVXi0k9N0szUEIdI2jm7UhM"

ACCEPT_KEYWORD = '114514' # 自动添加好友的关键词
ACCEPT_GREETING = '你好，请问有乜帮到你？' # 自动添加好友后的打招呼

UNKNOWN_MSG = '抱歉，目前我还没学会回答这个问题哦~' # 收到不支持的类型
NEED_GROUP = '请在群聊里问我哦~' # 只支持群聊
NEED_PRIVATE = '请私下问我哦~'
