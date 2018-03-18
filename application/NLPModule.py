# -*- coding:utf-8 -*-  

import sys
import MeCab
from luis_sdk import LUISClient
from config import *
import codecs
from application import app, db
from model import *
from sqlalchemy import and_, or_

__DEBUGGING__ = True

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


APPID = '3f8d3c92-4d53-4ef0-8233-2f12cb3a6772'
APPKEY = 'ad9e9a24ee2144c98e810f8d1a711d6e'
SUPPORTED_TYPE = ['Seasons', 'Materials', 'Effect']


def predict_intent(question):
    # 调用LUIS进行语义预测
    client = LUISClient(APPID, APPKEY, True)
    res = client.predict(question)
    question = question.decode('utf-8')

    intent = res.get_top_intent().get_name()
    entList = []
    ents = res.get_entities()
    for ent in ents:
        entList.append({
            'type': ent.get_type(),
            'entity': question[ent.get_start_idx():ent.get_end_idx() + 1]
        })
    return intent, entList


def divide_entities(question):
    # 调用MeCab分词并且取出关键词
    mecabTagger = MeCab.Tagger('-d ./application/mecab-dict')
    seperated = mecabTagger.parse(question)
    phrase = list()
    for x in seperated.split('\n'):
        if x.split('\t')[0] == 'EOS':
            break
        word = x.split('\t')[0]
        prop = x.split('\t')[1].split(',')

        if __DEBUGGING__:
            print word, ' ', prop[0], ' ', prop[3]
        allowVoca = {
            'a': 1,
            'v': 2,
            'n': 2
        }
        if (prop[0] in allowVoca) and (eval(prop[3]) >= allowVoca[prop[0]]):
            if __DEBUGGING__:
                print 'Accepted: ', word
                print 'Prop length:', prop[3]
                print 'AllowVoca length:', allowVoca[prop[0]]
            phrase.append({'entity': word.decode('utf-8')})
    if __DEBUGGING__:
        print phrase
    return phrase

def seek_answer(question):
    #try:
    questionDecoded = question.strip().encode('utf-8')
    #except:
    #    print "PASS encoded check"
        # pass
    intent, entityList = predict_intent(questionDecoded)               # 获取语义判断
    if intent != 'Seasons':
        entityList = divide_entities(questionDecoded)

    if __DEBUGGING__:
        print 'INTENT: ', intent
        print 'ENTITY LIST: ', entityList

    retCode = -1
    retMsg = UNKNOWN_MSG

    while True:
        if intent not in SUPPORTED_TYPE:
            break
        
        ans = None
        try:                                        # 根据主语寻找相应知识
            if intent == 'Seasons':
                season = None
                for ent in entityList:
                    if ent['type'] == 'SeasonName':
                        season = ent['entity']
                        break
                if __DEBUGGING__:
                    print 'Season: ' + season
                if season is None:
                    break
                queryRes = db.session.query(t_answers).filter(
                    and_(
                        t_answers.Fquestion_type == 'Seasons', 
                        t_answers.Fquestion_keywords.like('%' + season + '%'))
                    ).first()
                if queryRes is None:
                    break
                ans = "以上是根据【" + season + "】为您推荐的配方：\n" + queryRes.Fquestion_answer

            else:
                queryRes = db.session.query(t_answers).filter(or_(t_answers.Fquestion_answer.like('%' + ent['entity'] + '%') for ent in entityList)).all()
                if __DEBUGGING__:
                    print "notSeason queryRes=", len(queryRes)
                for index in range(0, 3 if len(queryRes) > 3 else len(queryRes)):
                    if queryRes[index] and (queryRes[index].Fquestion_type != 'Seasons'):
                        if ans is None:
                            ans = ""
                        ans += queryRes[index].Fquestion_answer
                if ans is None:
                    break

                entityString = ""
                for ent in entityList:
                    if entityString != "":
                        entityString += "、"
                    entityString += "【" + ent["entity"] + "】"
                ans = "以上是根据" + entityString + "为您推荐的配方：\n" + ans

            if ans is None:
                break

            retCode = 0
            retMsg = ans.strip()

        except Exception as e:
            retMsg = e.message
            break

        break

    return retCode, retMsg

