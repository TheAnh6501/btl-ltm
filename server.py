import socket
import random

def generate_random_item():
    items = ['5 triệu', '10 triệu', '20 triệu', '30 triệu']
    return random.choice(items)


def handle_client(client_socket):
    request = client_socket.recv(1024).decode() #Nhận và phân tích dữ liệu
    if request == 'generate_item':
        item = generate_random_item()
        client_socket.send(item.encode())

    else:
        client_socket.send('Invalid request'.encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Ipv4 và giao thức TCP
    server_socket.bind(('localhost', 8888)) # vì client và server hiện tại chạy trên cùng 1 máy, kết nối tới localhost
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")
        handle_client(client_socket)

if __name__ == "__main__":
    main()