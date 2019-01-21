import nltk
import importlib,sys

importlib.reload(sys)

# 执行后判断特征a和特征b的分类分别是3和2
#
# 因为训练集中特征是a的分类是3的最多，所以会归类为3
#
# 当然实际中训练样本的数量要多的多，特征要多的多
my_train_set = [
    ({'feature1': u'a'}, '1'),
    ({'feature1': u'a'}, '2'),
    ({'feature1': u'a'}, '3'),
    ({'feature1': u'a'}, '3'),
    ({'feature1': u'b'}, '2'),
    ({'feature1': u'b'}, '2'),
    ({'feature1': u'b'}, '2'),
    ({'feature1': u'b'}, '2'),
    ({'feature1': u'b'}, '2'),
    ({'feature1': u'b'}, '2'),
]
classifier = nltk.NaiveBayesClassifier.train(my_train_set)
print(classifier.classify({'feature1': u'a'}))
print(classifier.classify({'feature1': u'b'}))

test_set=[
    ({'cujamin': u'b'}, 'cuj'),
    ({'cujamin': u'b'}, 'cuj'),
    ({'cujamin': u'b'}, 'amin'),
    ({'cujamin': u'b'}, 'amin'),
    ({'cujamin': u'b'}, 'amin')
]
classifier = nltk.NaiveBayesClassifier.train(test_set)
print(classifier.classify({'cujamin': u'b'}))