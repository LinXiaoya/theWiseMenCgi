# -*- coding:utf-8 -*-

from application import app, db
from application.NLPModule import seek_answer

question = "月经不调该喝什么茶"
print question

retCode, retMsg = seek_answer(question)

print 'retCode: ', retCode
print 'retMsg: ', retMsg

