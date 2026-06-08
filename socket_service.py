import socket
from operator import truediv

service_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind
service_sock.bind(("127.0.0.1",9090))
#listen
service_sock.listen(5)
print("侦听中")
#accept
client_conn,client_addr=service_sock.accept()
print(f"客户端的地址是{client_addr}")
while True:
    date_bytes=client_conn.recv(1024)

    if not date_bytes:
        print("客户端断开连接")
        break

    recv_msg=date_bytes.decode("utf-8")
    print(f"收到：{recv_msg}")

    client_conn.send(date_bytes)
    print(f"发送：{recv_msg}")

    client_conn.close()
    service_sock.close()