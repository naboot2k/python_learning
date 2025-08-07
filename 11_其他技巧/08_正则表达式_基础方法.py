"""
python正则表达式，使用re模块，并基于re模块中的三个基础方法来做正则匹配。
分别是：match、search、findall三个基础方法
1、re.match(匹配规则, 被匹配字符串)
    从被匹配字符串开头进行匹配，匹配成功返回匹配对象（包含匹配信息），匹配不成功返回空
    注意：开头必须匹配，不然就匹配不成功
2、search(匹配规则, 被匹配字符串)
    搜索整个字符串，找出匹配的。从前往后，找到第一个后，就停止，不会继续向后；整个字符串都找不到，返回None
3、findall(匹配规则, 被匹配字符串)
    搜索整个字符串，找出所有匹配的。返回一个列表，列表的元素是匹配的字符串
"""
import re

# match 从头匹配
s = 'python itheima'
# s = '1python itheima'  #匹配不成功
result = re.match("python", s)
print(result)
print(result.span())
print(result.group())

# search 搜索匹配
s1 = '1python itheima python'
result = re.search("python", s1)
print(result)
print(result.span())
print(result.group())

# findall 搜索全部匹配
s2 = '1python itheima python'
result = re.findall("python", s2)
print(result)

