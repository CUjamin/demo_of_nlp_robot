# ---------------------分块-----------------------



# ---------------------语法分析-----------------------
# N：        名词
# Det：      限定词
# NP：       名词短语
# V：        表示动词
# VP：       动词短语
# S：        句子
#
# (S
#     (NP 小明)
#     (VP
#         (V 追赶)
#         (NP
#             (Det 一只)
#             (N 兔子))))
#


# ----------------------文法分析--------------------------
# 文法是一个潜在的无限的句子集合的一个紧凑的特性，它是通过一组形式化模型来表示的，文法可以覆盖所有结构的句子，
# 对一个句子做文法分析，就是把句子往文法模型上靠，如果同时符合多种文法，那就是有歧义的句子
#
# 最重要的结论：文法结构范围相当广泛，无法用规则类的方法来处理，只有利用基于特征的方法才能处理

# 文法特征举例：单词最后一个字母、词性标签、文法类别、正字拼写、指示物、关系、施事角色、受事角色
#
# 因为文法特征是一种kv，所以特征结构的存储形式是字典
#
# 不是什么样的句子都能提取出每一个文法特征的，需要满足一定的条件，这需要通过一系列的检查手段来达到，
# 包括：句法协议（比如this dog就是对的，而these dog就是错的）、属性和约束、术语


# ----------------------特征结构的处理--------------------------
# import nltk
# fs1 = nltk.FeatStruct(TENSE='past', NUM='sg')
# print(fs1)
# print()
# fs2 = nltk.FeatStruct(POS='N', AGR=fs1)
# print(fs2)

# raw=open('forgotten_times.txt').read()
# print(raw)

# sql0.fcfg:
# S[SEM = (?np + WHERE + ?vp)] -> NP[SEM =?np] VP[SEM =?vp]
#
# VP[SEM = (?v + ?pp)] -> IV[SEM =?v] PP[SEM =?pp]
# VP[SEM = (?v + ?ap)] -> IV[SEM =?v] AP[SEM =?ap]
# NP[SEM = (?det + ?n)] -> Det[SEM =?det] N[SEM =?n]
# PP[SEM = (?p + ?np)] -> P[SEM =?p] NP[SEM =?np]
# AP[SEM =?pp] -> A[SEM =?a] PP[SEM =?pp]
#
# NP[SEM = 'Country="greece"'] -> 'Greece'
# NP[SEM = 'Country="china"'] -> 'China'
#
# Det[SEM = 'SELECT'] -> 'Which' | 'What'                   //SELECT
#
# N[SEM = 'City FROM city_table'] -> 'cities'               //{column} FROM {table}
#
# IV[SEM = ''] -> 'are'
# A[SEM = ''] -> 'located'
# P[SEM = ''] -> 'in'

# 结果：
# (S[SEM=(SELECT, City FROM city_table, WHERE, , , Country="china")]
#   (NP[SEM=(SELECT, City FROM city_table)]
#     (Det[SEM='SELECT'] What)
#     (N[SEM='City FROM city_table'] cities))
#   (VP[SEM=(, , Country="china")]
#     (IV[SEM=''] are)
#     (AP[SEM=(, Country="china")]
#       (A[SEM=''] located)
#       (PP[SEM=(, Country="china")]
#         (P[SEM=''] in)
#         (NP[SEM='Country="china"'] China)))))
# from nltk import load_parser
# cp = load_parser('sql0.fcfg')
# query = 'What cities are located in China'
# tokens = query.split()
# for tree in cp.parse(tokens):
#     print(tree)
# print()
# query = 'i want to find the cities what are located in China'
# tokens = query.split()
# for tree in cp.parse(tokens):
#     print(tree)
#

# -----------------------------

