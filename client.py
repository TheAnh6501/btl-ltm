import socket
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))
    client_socket.send(request.encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

def generate_item():
    item = send_request('generate_item')
    messagebox.showinfo("Chiếc nón kỳ diệu", f"Bạn đã quay được {item}!")


def main():
    root = tk.Tk()
    root.title("Chiếc nón kỳ diệu")
    root.geometry("900x900")

    # Picture
    image = Image.open("chiecNon.jpg")
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.pack()

    # Button
    item_button = tk.Button(root, text="Quay chiếc nón !!!", command=generate_item)
    item_button.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    main()