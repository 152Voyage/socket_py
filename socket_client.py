import socket
#creat a client socket
client_pc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect the server_pc
client_pc.connect(("127.0.0.1",5381))
#show the address and port
print(f"客户端1的IP和端口号是{client_pc.getsockname()}")
#send some date to the server_pc
count=client_pc.send("你好啊，tcp/ip".encode("utf-8"))
print(f"客户端1一共发送{count}字节")
