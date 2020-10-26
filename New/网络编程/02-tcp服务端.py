import socket
if __name__ == '__main__':
    # 1. 创建服务端套接字对象
    # IPV4 and TCP
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #2 绑定端口号
    tcp_server_socket.bind(('',12346))
    # 3 开始监听
    tcp_server_socket.listen(128)
    # 4 等待接受客户端连接请求
    service_client_socket,ip_port = tcp_server_socket.accept()
    # print(service_client_socket,ip_port)
    # 5 接收数据
    recv_date = service_client_socket.recv(1024)
    recv_date_content = recv_date.decode('utf-8')
    print('接收到的数据为',recv_date_content)
    # 6 发送数据
    send_data = '现在是服务端发送的数据'.encode('utf-8')
    service_client_socket.send(send_data)
    # 7 关闭套接字
    service_client_socket.close()
    tcp_server_socket.close()