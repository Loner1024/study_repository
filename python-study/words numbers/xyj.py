fr = open("xyj.txt","r")  #读取文件
words = []
num = {}
for line in fr:
    line=line.strip
    if len(line) == 0:
        continue
    for x in range(0,len(line)):
        print(line)
        break
fr.close() #关闭文件