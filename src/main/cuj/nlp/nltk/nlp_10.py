import sys,importlib
import pynlpir

# ------------------开始---------------------
print('------------------Start---------------------')
# ------------------分词----------------------
print('------------------分词---------------------')
importlib.reload(sys)
pynlpir.open()

s = '聊天机器人到底该怎么做呢？'
segments = pynlpir.segment(s)
for segment in segments:
    print(segment[0], '\t', segment[1])

# -----------------关键词提取--------------------------
print('------------------关键词提取---------------------')

s = '聊天机器人到底该怎么做呢？'
key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print(key_word[0], '\t', key_word[1])

# -----------------分词+关键词提取--------------------------
print('------------------分词+关键词提取---------------------')
s = '海洋是如何形成的'
segments = pynlpir.segment(s, pos_names='all',pos_english=False)
for segment in segments:
    print(segment[0], '\t', segment[1])
key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print(key_word[0], '\t', key_word[1])
print('------------------分词+关键词提取 - 2---------------------')
s = '十个人'
segments = pynlpir.segment(s, pos_names='all',pos_english=False)
for segment in segments:
    print(segment[0], '\t', segment[1])
key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print(key_word[0], '\t', key_word[1])

print('------------------End---------------------')
pynlpir.close()
# --------------------结束---------------------------
