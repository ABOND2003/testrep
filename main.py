import socket

def find_free_port():
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp_socket.bind(('localhost', 0))
    _, port = temp_socket.getsockname()
    temp_socket.close()
    return port
def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Сервер запущен на порту {port}")
    while True:
        conn, addr = server_socket.accept()
        print(f"Подключено к {addr}")
        data = conn.recv(1024).decode('utf-8')
        print(f"Получено от клиента: {data}")
        conn.send("Данные успешно получены!".encode('utf-8'))
        conn.close()
if __name__ == "__main__":
    free_port = find_free_port()
    start_server(free_port)