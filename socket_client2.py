# 导入socket库
import socket
# 导入time库，用于延时等待
import time

# 创建客户端socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
client_sock.connect(("127.0.0.1", 9090))

# 自动连续发送3条消息（测试粘包用）
for i in range(3):
    # 生成消息：消息0、消息1、消息2
    msg = f"消息{i}"

    # 字符串转字节
    data_bytes = msg.encode("utf-8")

    # ===================== 加粘包处理 =====================
    # 生成4字节长度头
    len_bytes = len(data_bytes).to_bytes(4, byteorder="big")

    # 先发长度头
    client_sock.send(len_bytes)

    # 再发真实消息内容
    client_sock.send(data_bytes)

    # 打印发送提示
    print(f"已发送：消息{i}")

# 等待0.5秒，让服务端处理完所有消息
time.sleep(0.5)

# 优雅关闭连接（不会强制断开报错）
client_sock.shutdown(socket.SHUT_RDWR)
client_sock.close()

print("客户端已经关闭")