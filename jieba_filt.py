# encoding=utf-8
# 使用开源代码-结巴中文分词
import jieba

f = open('outcome.txt')
ff = f.read()

seg_list = jieba.cut(ff, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

