"""
类型注解主要功能：
    1、帮助第三方IDE工具对代码进行类型推断，协助做代码提示
    2、帮助开发者自身对变量进行类型注释

类型注解仅仅是提示性的，并非决定性的

1、变量的类型注解
2、函数（方法）形参列表和返回值的类型注解
3、Union类型
"""
import random
from typing import Union

# 为变量设置类型注解     基础语法： 变量: 类型
var_1 : int = 100
var_2 : float = 13.14
var_3 : bool = True
var_4 : str = "hello world"
class Student:
    pass
var_5 : Student = Student()

# 数据容器的类型注解分为简单的类型注解和详细的类型注解
var_6 : list = [1,2,3,4,5]
var_7 : list[int] = [1,2,3,4,5]

# 元组类型设置类型详细注解，需要将每一个元素的详细类型都写出来
var_8 : tuple[str, int, bool] = ["Hello", 666, True]

# 字典类型设置类型详细注解，需要两个类型，第一个是key第二个是value
var_9 : dict[str, int] = {"age": 18}

"""
除了使用 变量:类型 ，这种语法做注解外，也可以在注释中进行类型注解
语法： # type: 类型
"""
var_10 = random.randint(1, 100) # type: int
var_11 = random.random() # type: float


"""
函数和方法的形参和返回值的类型注解语法：
    def 函数方法名(形参名: 类型, 形参名: 类型,......) -> 返回值类型：
        pass
"""
def add(a: int, b: int) -> int:    # -> int表示函数的返回值类型
    return a + b


"""
使用Union[类型, ......, 类型] 可以定义联合类型注解
注意：使用Union类型，必须先导包
"""
my_list: list[Union[int, str]] = [1, "hello", 2, "world"]
my_dict: dict[str, Union[int, str]] = {"name": "张三", "age": 18}

def func(data: Union[int, str]) -> Union[int, str]:
    pass