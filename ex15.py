# -*- coding: utf - 8 -*-

# 导入sys模块中的agrv
from sys import argv

# 将参数赋值给左边的两个变量 
script, filename = argv

# 将文件对象赋值给txt这一变量
txt = open(filename)

# 输出文件名
print "Here's your file %r:" % filename
# 读取并输出txt中的内容
print txt.read()
txt.close()

# 要求用户再次输入文件名
print "Type the filename again:"
file_again = raw_input("> ")

# 将文件对象赋值给txt_again
txt_again = open(file_again)

# 读取并输出文件内容
print txt_again.read()
txt_again.close()