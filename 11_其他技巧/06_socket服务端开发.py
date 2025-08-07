"""
演示Socket服务端开发
"""
import socket
# 创建Socket对象
socket_server = socket.socket()

# 绑定ip地址和端口
socket_server.bind(('localhost', 8888))

# 监听端口
socket_server.listen(1)     # listen方法内接收一个整数参数表示最大允许的连接数


# 等待客户端连接
# result = socket_server.accept()
# conn = result[0]        # 获取客户端的socket对象
# ip_port = result[1]     # 获取客户端的ip地址和端口
conn, address = socket_server.accept()  # accept方法返回一个元组，元组内包含两个元素，第一个元素是客户端的socket对象，第二个元素是客户端的ip地址和端口
# accept方法是一种阻塞的方法，等待客户端连接后才会向下执行
print("客户端已连接", address)

while True:
    # 接受客户端信息,要使用客户端和服务端的本次连接的对象，而非socket_server对象
    data: str= conn.recv(1024).decode("utf-8")
    # recv方法接收一个整数参数表示接收数据的最大字节数,返回值是一个字节数组也就是bytes对象，不是字符串，可以通过UTF-8解码成字符串，阻塞的方法
    print(f"客户端发来的消息是:{data}")

    # 发送回复信息
    msg = input("请输入你要与客户端回复的消息：")
    if msg == "exit":
        break
    conn.send(msg.encode("utf-8"))  # encode方法将字符串转换成字节数组

# 关闭连接
conn.close()
socket_server.close()