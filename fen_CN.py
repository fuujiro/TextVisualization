# coding = utf-8
# 2018/7/1
# 检查空格和中文 
import os,sys
import os.path
import re
RootDir = os.getcwd() 
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

def start(rootDir):
    for f in os.listdir(rootDir):
        sourceF = os.path.join(rootDir,f)
        if os.path.isfile(sourceF):
            a = os.path.splitext(f) #去除扩展名
            checkName(a)
        if os.path.isdir(sourceF):
            checkName(f)
            start(sourceF)

#文件数组
"""
注意这地方的编码格式。windows文件名字的编码格式为gbk
"""
def checkName(f):
    #ff = f.decode('gbk').encode('utf-8') 
    ff = f.decode('gbk')
    #print(ff)
    match = zhPattern.search(ff) #匹配中文
    if match:
        print (ff)
        Chinese.append(f)
    for i in f:
           if i.isspace(): #检查空格
               print(f)
               name.append(f)

#输出到txt
def wirte():
    f = open(RootDir+"/checkReslut.txt", "w+")
    f.write("space :\n")

    for i in range(0, len(name)):
        f.write(name[i] + "\n")

    f.write("\nChinese :\n")
    for i in range(0, len(Chinese)):
        f.write(Chinese[i] + "\n")  

    f.close()

if __name__=="__main__":
    name = []
    Chinese = []
    start(RootDir)
    wirte()
    os.system("pause")