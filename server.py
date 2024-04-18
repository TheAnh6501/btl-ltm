import socket
import random

def generate_random_item():
    items = ['5 triệu', '10 triệu', '20 triệu', '30 triệu']
    return random.choice(items)


def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    if request == 'generate_item':
        item = generate_random_item()
        client_socket.send(item.encode())

    else:
        client_socket.send('Invalid request'.encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")
        handle_client(client_socket)

if __name__ == "__main__":
    main()