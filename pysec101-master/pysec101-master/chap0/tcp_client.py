import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'

port = 50000

msg = ''

while msg != 'exit':
    # 標準入力からデータを取得
    msg = input('-> ')

    # サーバにデータを送信
    data = sock.recv(1024)

    # サーバから受信したデータを出力
    print('Received from server: ' + str(data))

sock.close()    