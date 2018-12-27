import socket

ip = input('服务器IP：')
address = (ip,5554)
while True:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as link:
        link.connect(address)
        data = str(input('请输入要执行的命令：'))
        link.send(str(data).encode('utf-8'))
        ret = link.recv(1024)
        print(ret.decode('utf-8'))