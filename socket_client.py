import socket
#creat a client socket
client_pc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect the server_pc
client_pc.connect(("127.0.0.1",5381))
#send some date to the server_pc
count=client_pc.send("你好，tcp/ip".encode("utf-8"))
