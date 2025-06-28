"""
演示文件的追加
"""
# 创建文件对象
f = open('test.txt', 'a', encoding='utf-8') # a模式下，文件不存在时会创建新文件
# 写入数据
f.write('\nWhat is your gender')
# close方法内置了flush的功能
f.close()