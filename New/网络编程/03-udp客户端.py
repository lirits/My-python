import socket
if __name__ == '__main__':
# 1. 创建客户端套接字对象
# AF_INET = IPV4
# socket.SOCK_DGRAM = UDP传输协议
    udp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 2. 和服务端套接字建立连接
#     udp_client_socket.connect(("172.19.218.36",12345))
# 3. 发送数据
    send_data = '你好你好'.encode('utf-8')
    udp_client_socket.sendto(send_data,('172.19.218.36',12345))
# 4. 接收数据
    recv_data = udp_client_socket.recv(1024)#接收数据最大字节数
    recv_data_context = recv_data.decode('utf-8')
    print('接收的数据为:%s'%recv_data_context)
# 5. 关闭客户端套接字
    udp_client_socket.close()