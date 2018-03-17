# -*- coding:utf-8 -*-

from application import app, db
from NLPModule import seek_answer


@app.route('/getAnswer', methods = ['POST'])
def getAnswer():
    if request.method == "POST":
        # USER AUTHENTICATE HERE 
        # 系统规模和技术架构未知，暂时不做用户认证，若后续有需要再添加
        question = request.form.get('question')
        retCode, retMsg = seek_answer(question)
        return jsonify({
            'retCode': retCode,
            'retMsg': retMsg
            })

