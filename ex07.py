# -*- coding: utf-8 -*-

# 输出字符串。
print "Mary had a little lamb."
# 输出用“snow”代替了之前字符串中“%s”的结果。
print "Its fleece was white as %s." % 'snow'
# 输出字符串。
print "And everywhere that Mary went."
# 输出字符串“.”被乘以10的结果。
print "." * 10 # what'd that do?

# 将Cheese和Burger两个单词中的字母赋值到不同的自变量中。
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# 如果去掉“,”，将使得之后的变量运算结果的另起一行输出。
# 在同一行内输出两个字符串变量运算的结果，用“,”做间隔，输出上相距一格。
print end1 + end2 + end3 + end4 + end5 + end6 ,
print end7 + end8 + end9 + end10 + end11 + end12