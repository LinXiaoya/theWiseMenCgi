# -*- coding:utf-8 -*-

import MeCab

question = '夏天上火该喝什么茶'

mecabTagger = MeCab.Tagger('-d ./application/mecab-dict')
seperated = mecabTagger.parse(question)
phrase = []
for x in seperated.split('\n'):
    if x.split('\t')[0] == 'EOS':
        break
    # print x
    # phrase.append({'phrase': x.split('\t')[0], 'part': x.split(',')[0].split('\t')[1]})
    word = x.split('\t')[0]
    prop = x.split('\t')[1].split(',')
    print x
    print word, ' ', prop[0], ' ', prop[3]

