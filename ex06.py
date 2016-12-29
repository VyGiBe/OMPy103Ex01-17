# -*- coding: utf-8 -*-

# 用具体的值替换字符串中的%d，并将该字符串赋值给新建变量x。
x = "There are %d types of people." % 10
# 创建字符串变量binary并赋值。
binary = "binary"
# 创建字符串变量do_not并赋值。
do_not = "don't"
# 将已赋值的变量分别代替之前字符串中的%s，其位置一一对应，并将该替换结果赋值到新建变量y。
y = "Those who know %s and those who %s." % (binary, do_not)

# 输出字符串变量x的值
print x
# 输出字符串变量x的值
print y

# 以x的值替换之前字符串中的“%r”，并输出
print "I said: %r." % x
# 以y的值替换之前字符串中的“%s”，并输出
print "I also said: '%s'." % y

# 新建变量hilarious，并给其赋值False这一布尔值。
hilarious = False
# 新建变量joke_evaluation，将字符串赋值于它。
joke_evaluation = "Isn't that joke so funny?! %r"

# 将hilarious的值替换joke_evaluation中的“%r”，并输出该结果。
print joke_evaluation % hilarious

# 新建字符串变量w，并赋值。
w = "This is the left side of..."
# 新建字符串变量e，并赋值。
e = "a string with a right side."

# 输出两个字符串相加的结果，注意到相加的顺序影响输出结果。“+”对于字符串的运算是两个字符串的尾首连接。
print w + e
