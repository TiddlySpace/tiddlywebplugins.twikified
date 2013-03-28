"""
Represents the twikifier (node app) side and simply sends back pre-determined data.
This probably isn't the best way to implement this but works for now.
"""
import socket
from threading import Thread


def fake_twikifier(socket_file, data_to_return):
    buffer_size = 4096
    connections_backlog = 5

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(socket_file)
    server_socket.listen(connections_backlog)

    connection, client_address = server_socket.accept()
    try:
        while True:
            received_data = connection.recv(buffer_size)
            if received_data:
                connection.sendall(data_to_return)
            else:
                break

    finally:
        connection.close()
        server_socket.close()


def start_server(socket_file, data_to_return):
    server_thread = Thread(target=fake_twikifier, args=(socket_file, data_to_return))
    server_thread.start()