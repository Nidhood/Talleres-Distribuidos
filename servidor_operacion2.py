import socket
import json
import numpy as np

def multiply_matrices(a, b):
    return np.dot(a, b).tolist()

def main():
    host = '192.168.56.4'  # Dirección IP del servidor de operación 2
    port = 5002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor de operacion 2 escuchando en {host}:{port}/TCP")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")

        data = conn.recv(4096).decode()
        matrices = json.loads(data)

        result = multiply_matrices(matrices['a'], matrices['b'])
        conn.send(json.dumps(result).encode())

        conn.close()

if __name__ == "__main__":
    main()