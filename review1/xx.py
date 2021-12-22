# import os

# filePrefix = 'Test'
fileSuffix = '.py'
fileNum = 3  # 文件个数
for i in range(3, 3 + fileNum):
    filename = str(i) + fileSuffix
    with open(filename, 'w') as f:
        f.write('')
