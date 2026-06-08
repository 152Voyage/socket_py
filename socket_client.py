# 导入socket库
import socket

# 创建客户端socket（TCP协议）
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端（本机9090端口）
client_sock.connect(("127.0.0.1", 9090))

# 循环发送消息
while True:
    # 手动输入要发送的消息
    send_msg = input("请输入发送的消息")

    # 输入q退出循环
    if send_msg == "q":
        break

    # ===================== 解决粘包：发送规则 =====================
    # 1. 将字符串编码成字节数据
    data_bytes = send_msg.encode("utf-8")

    # 2. 生成4字节长度头（记录本条消息的长度）
    len_bytes = len(data_bytes).to_bytes(4, byteorder="big")

    # 3. 先发长度头，再发真实消息
    client_sock.send(len_bytes)
    client_sock.send(data_bytes)

    # ===================== 接收服务端的回声 =====================
    # 1. 先收4字节长度头
    echo_len = client_sock.recv(4)

    # 2. 解析出消息长度
    echo_data_len = int.from_bytes(echo_len, byteorder="big")

    # 3. 根据长度精准接收消息
    echo_date = client_sock.recv(echo_data_len)

    # 打印服务端返回的消息
    print(f"服务器发送来的数据是:{echo_date.decode("utf-8")}")

# 关闭客户端连接
client_sock.close()
print("客户端已经关闭")