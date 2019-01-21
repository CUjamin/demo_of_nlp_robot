import importlib,sys
import nltk


importlib.reload(sys)

# #-----------英文词干提取器---------------------
# porter = nltk.PorterStemmer()
# print(porter.stem('lying'))
# #-----------词性标注器------------------------
# text = nltk.word_tokenize("And now for something completely different")
# print(nltk.pos_tag(text))
# #-----------词性自动标注器------------------------
# default_tagger = nltk.DefaultTagger('NN')
# raw = '我 累 个 去'
# tokens = nltk.word_tokenize(raw)
# print(default_tagger.tag(tokens))

# sys.setdefaultencoding("utf-8")

# for word in nltk.corpus.sinica_treebank.tagged_words():
# #     print(word[0], word[1])

raw = 'i want to find the cities what are located in China'
tokens = nltk.word_tokenize(raw)
print(nltk.pos_tag(tokens))


