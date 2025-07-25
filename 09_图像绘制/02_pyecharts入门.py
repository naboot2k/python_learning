from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 创建折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])

# 添加y轴数据
line.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

# 设置全局配置项set_global_opts()来设置
line.set_global_opts(
    title_opts=TitleOpts(title="折线图", pos_left="center", pos_top="20"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过render方法，将代码生成图表
line.render("折线图.html")