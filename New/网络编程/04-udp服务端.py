#!/usr/bin/python3
import socket
if __name__ == '__main__':
    # 1. 创建服务端套接字对象
    # IPV4 and UDP
    udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 端口复用
    udp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #2 绑定端口号
    udp_server_socket.bind(('',12345))
    #3 接收数据
    recv_date,addr = udp_server_socket.recvfrom(1024)
    recv_date_content = recv_date.decode('utf-8')
    print('接收到的数据为',recv_date_content)
    # 6 发送数据
    send_data = '现在是服务端发送的数据'.encode('utf-8')
    udp_server_socket.sendto(send_data,addr)
    # 7 关闭套接字
    udp_server_socket.close()