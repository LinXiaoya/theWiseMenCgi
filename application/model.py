# -*- coding:utf-8 -*-

from application import db

class t_answers(db.Model):
    Fid = db.Column(db.Integer, primary_key=True)
    Fquestion_type = db.Column(db.String(60))
    Fquestion_keywords = db.Column(db.String(120))      # 格式是'#关键词1#关键词2#关键词3#...' 查找时使用 like '%#%(keyword)s#%' % {'keyword': keyword}
    Fquestion_answer = db.Column(db.String(4096))
    def __init__(self, Fquestion_type, Fquestion_keywords, Fquestion_answer):
        self.Fquestion_type = Fquestion_type
        self.Fquestion_keywords = Fquestion_keywords
        self.Fquestion_answer = Fquestion_answer
    def __repr__(self):
        return '[t_answer]<Fid=%(Fid)s|Fquestion_type=%(Fquestion_type)s|Fquestion_keywords=%(Fquestion_keywords)s>|Fquestion_answer=%(Fquestion_answer)s' % {
            'Fid': self.Fid,
            'Fquestion_type': self.Fquestion_type,
            'Fquestion_keywords': self.Fquestion_keywords,
            'Fquestion_answer': self.Fquestion_answer
            }

