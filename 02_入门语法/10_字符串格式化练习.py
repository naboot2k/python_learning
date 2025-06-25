# 公司名
name = "Alibaba"
# 公司股价
stock_price = 168.09
# 公司股票代码
stock_code = '003032'
# 股票每日增长系数，浮点数类型
stock_price_daily_growth_factor = 1.05
# 增长天数
growth_days = 10

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数：%.2f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** growth_days))