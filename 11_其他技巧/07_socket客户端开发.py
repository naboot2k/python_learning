"""
演示Socket客户端开发
"""
import socket
# 创建Socket对象
socket_client = socket.socket()

# 连接到服务器
socket_client.connect(('localhost', 8888))

while True:
    # 发送消息
    msg = input("请输入要发送的消息：")
    if msg == "exit":
        break
    socket_client.send(msg.encode('utf-8'))

    # 接受返回消息
    recv_data = socket_client.recv(1024)
    print(f"服务端返回的消息是：{recv_data.decode('utf-8')}")

# 关闭连接
socket_client.close()