# 导入socket库，用于网络通信
import socket
# 导入threading库，用于多线程处理，同时服务多个客户端
import threading


# 定义函数：专门处理【一个客户端】的通信
# client_conn：和客户端通信的连接通道
# client_addr：客户端的地址(IP, 端口)
def talk_with_client(client_conn, client_addr):
    # 打印当前连接的客户端地址
    print(f"所连接客户端的地址是{client_addr}")

    # 无限循环，持续和客户端通信
    while True:
        try:
            # ===================== 解决粘包：第一步 =====================
            # 1. 先固定接收 4 字节（这是消息长度头，我们约定好的）
            len_bytes = client_conn.recv(4)

            # 如果没有收到长度数据，说明客户端正常断开连接
            if not len_bytes:
                print(f"客户端离开:{client_addr}")
                break  # 退出循环，结束和这个客户端的通信

            # 2. 将4字节的长度头，转换成数字（得到消息真实长度）
            data_len = int.from_bytes(len_bytes, byteorder="big")

            # 3. 根据长度，精准接收【一条完整消息】（彻底解决粘包）
            data = client_conn.recv(data_len)

            # 将字节数据解码成字符串
            msg = data.decode("utf-8")
            # 打印收到的客户端消息
            print(f"收到的消息为：{msg}")

            # ===================== 回声回复 =====================
            # 回复规则必须和发送一致：先发长度头，再发消息内容
            client_conn.send(len_bytes)  # 发送长度头
            client_conn.send(data)  # 发送真实消息

        # 捕获异常：客户端强制关闭（直接点×），导致连接中断
        except ConnectionResetError:
            print(f"客户端强制断开:{client_addr}")
            break  # 退出循环，结束线程


# 主函数：服务端启动入口
def main():
    # 1. 创建服务端socket对象（TCP协议）
    service_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定IP和端口（本机9090端口）
    service_sock.bind(("127.0.0.1", 9090))

    # 3. 开始监听客户端连接
    service_sock.listen(5)
    print("多线程服务器已启动，等待客户端连接===")

    # 无限循环：持续等待新客户端连接
    while True:
        # 阻塞等待客户端连接
        # conn：新的连接通道
        # addr：客户端地址
        conn, addr = service_sock.accept()
        print(f"客户端的地址为:{addr}")

        # 创建新线程，专门处理这个客户端
        # target：线程要运行的函数
        # args：传递给函数的参数
        t = threading.Thread(target=talk_with_client, args=(conn, addr), daemon=True)

        # 启动线程
        t.start()


# 判断是否是主程序运行
if __name__ == "__main__":
    main()