import socket

#创建对象
socket_server=socket.socket()
#绑定ip地址和端口
socket_server.bind(("localhost",8888))

#监听端口
socket_server.listen(1)

#等待客户端连接
result:tuple=socket_server.accept()#(链接对象，客户端地址信息)
conn=result[0]
address=result[1]
print(f"接收到了客户端的链接，客户端信息是：{address}")
while True:
    data:str=conn.recv(1024).decode("UTF-8")

    print(f"客户端发来的消息是：{data}")

    msg=input(f"请输入你要和客户端回复的消息是：")
    if msg=='exit':
        break
    conn.send(msg.encode("UTF-8"))


conn.close()
socket_server.close()