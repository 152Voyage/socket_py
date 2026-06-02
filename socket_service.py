import socket
#创建一个服务端的套接字
serer_pc=socket.socket(socket.AF_INET,socket.SOCK_STREAM )
#将该套接字绑定一个地址和端口
serer_pc.bind(("127.0.0.1",5381))
#listen
serer_pc.listen(5)
print("server_pc is listing")
#accept
conn,addr=serer_pc.accept()
print(f"连接我的第一个客户端的地址是{addr}")
date_bytes=conn.recv(1024)
date_str=date_bytes.decode("utf-8")
print(f"收到消息：{date_str}")
conn.close()  # 关闭和这个客户端的连接
serer_pc.close()  # 关闭服务端套接字
print("✅ 服务端已关闭连接")

