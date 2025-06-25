"""
演示Python中变量的相关操作
"""

# 定义一个变量，用来记录钱包的余额
wallet_value = 50

# 通过print语句，输出变量记录的内容
# *不同内容可以用逗号隔开*
print("钱包还有：",wallet_value,"元")

# 买了一个雪糕，消费10元
wallet_value = wallet_value - 10
print("雪糕10元，买完雪糕后，钱包还有：",wallet_value,"元")