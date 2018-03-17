# -*- coding:utf-8 -*-

from application import db
from application.model import *

queryRes = db.session.query(t_answers).filter(t_answers.Fquestion_type == 'Seasons').all()

for res in queryRes:
    print res.Fquestion_type
    print res.Fquestion_keywords
    print res.Fquestion_answer
    print '====================================================='

queryRes = queryRes = db.session.query(t_answers).filter(t_answers.Fquestion_type == 'Tea').all()

print 'count(Tea)=', len(queryRes)
