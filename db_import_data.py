# -*- coding:utf-8 -*-

from application import db
from application.model import *
import os
import sys
import codecs

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

__DATADIR__ = 'data'
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), __DATADIR__)


# 由reg格式的数据注册表单中读取相应的文件并且写入数据库
def readRegFile(fileName, typeName):
    file = open(os.path.join(path, fileName), 'r')
    while True:
        lineKeyword = file.readline().strip().decode('utf-8')
        if lineKeyword:
            lineAnswerFile = file.readline().strip().decode('utf-8')
            textAnswer = ''
            with open(os.path.join(path, lineAnswerFile), 'r') as fileAnswer:
                for lineAnswer in fileAnswer:
                    textAnswer += lineAnswer.decode('utf-8')
            newAns = t_answers(typeName, lineKeyword, textAnswer)
            db.session.add(newAns)
        else:
            break
    file.close()


# Seasons
readRegFile('seasonsReg.txt', 'Seasons')

# Teas
readRegFile('teaReg.txt', 'Tea')

# # Materials
# fMaterials = open(os.path.join(path, 'materialsReg.txt'), 'r')


# # Effect
# fEffect = open(os.path.join(path, 'effectReg.txt'), 'r')


# final commit
db.session.commit()
