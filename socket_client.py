import socket
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_sock.connect(("127.0.0.1",9090))
while True:
    send_msg=input("请输入发送的消息")
    if send_msg=="q":
        break

    client_sock.send(send_msg.encode("utf-8"))

    echo_date=client_sock.recv(1024)
    print(f"服务器发送来的数据是:{echo_date.decode("utf-8")}")

client_sock.close()
print("客户端已经关闭")