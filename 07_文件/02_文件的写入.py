"""
演示文件的写入
"""
# 创建文件对象
f = open('test.txt', 'w', encoding='utf-8') # w模式下，文件不存在时会创建新文件

# 写入数据
f.write('hello world！！！')

# flush刷新，将缓存中的信息写入文件
# f.flush()

# close方法内置了flush的功能
f.close()