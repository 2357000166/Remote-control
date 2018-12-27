import socket
import subprocess

ip = input('本机IP：')
address = (ip,5554)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as link:
    link.bind(address)
    link.listen(1)
    print("正在等待连接----")
    while True:
        conn,addr = link.accept()
        with conn:
            print(addr,'已连接')
            data = conn.recv(1024)
            if data == 'exit':
                break
            ret = subprocess.getoutput(data)
            conn.send(('result: \n'+ret).encode('utf-8'))
            
            
            