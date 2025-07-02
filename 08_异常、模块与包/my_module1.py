__all__ = ['test', 'test_A']
def test(a, b):
    print(a + b)

def test_A():
    print('testA')

def test_A():
    print('testA')

# 该模块中的测试语句，可以使用下面判断语句，当模块被直接运行时执行，当模块被导入时，不执行。
if __name__ == '__main__':
    test(1, 2)