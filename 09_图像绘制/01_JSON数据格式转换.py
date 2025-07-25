# 导入json模块
import json

# 准备符合json格式要求的python数据
data = [{"name": "张三", "age": 18}, {"name": "王五", "age": 20}]

# 通过json.dumps(data)方法把python数据转化为了json数据
data = json.dumps(data, ensure_ascii=False)  # 第二个参数保证中文格式正确
print(type(data))       # json就是一个拥有特定格式的字符串
print(data)

# 通过json.loads(data)方法把json数据转化为python数据
data1 = '[{"name": "张三", "age": 18}, {"name": "王五", "age": 20}]'
print(type(data1))
data2 = json.loads(data1)
print(type(data2))

s = '{"name": "张三", "age": 18}'
d = json.loads(s)
print(d)