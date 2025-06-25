# 取出列表内的偶数
old_list = [1,2,3,4,5,6,7,8,9,10]
temp = list(old_list)
new_list = []
new_for_list = []
"""
while循环
"""
index = 0
while index < len(temp):
    num = temp.pop(0)
    if num % 2 == 0:
        new_list.append(num)
print(f"通过while循环，从列表：{old_list}中取出偶数，组成新列表：{new_list}")

"""
for循环
"""
for element in old_list:
    if element % 2 == 0:
        new_for_list.append(element)
print(new_for_list)


