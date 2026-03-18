
import socket
COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "add_obj  "
SYM_OP = "sym      "
BYE_OP = "bye      "
SUB_OP = "sub      "
END_OP = "stop     "

PORT = 3500
SERVER_ADDRESS = "127.0.0.1"

# ---------------------- interaction with sockets ------------------------------
def receive_int(connection, n_bytes: int) -> int:
    data = connection.recv(n_bytes)
    return int.from_bytes(data, byteorder='big', signed=True)

def send_int(connection, value: int, n_bytes: int) -> None:
    connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

def receive_str(connection, n_bytes: int) -> str:
    data = connection.recv(n_bytes)
    return data.decode()

def send_str(connection, value: str) -> None:
    connection.current_connection.send(value.encode())
# ---------------------------------------------------------------------------------------

def main():
    s = socket.socket()
    s.bind(("", PORT))
    s.listen(1)
    print("Waiting for clients to connect on port " + str(PORT))
    keep_running = True
    while keep_running:
        connection, address = s.accept()
        print("Client " + str(address) + " just connected")
        last_request = False
        #Recebe messagens...
        while not last_request:
            # Qual é o tamanho da string? print(len("_add".encode('utf-8')))
            # Porque razão o tamanho para int é 8 bytes?
            request_type = receive_str(connection,COMMAND_SIZE)
            if request_type == ADD_OP:
                a = receive_int(connection,INT_SIZE)
                b = receive_int(connection,INT_SIZE)
                print("Pediram para somar:",a,"+",b)
                result = a + b
                send_int(connection,result, INT_SIZE)
            elif request_type == SUB_OP:
                a = receive_int(connection,INT_SIZE)
                b = receive_int(connection,INT_SIZE)
                print("Pediram para subtrair:",a,"-",b)
                result = a-b
                send_int(connection,result, INT_SIZE)

            elif request_type == BYE_OP:
                last_request = True
                keep_running = False
                s.close()
    print("Server stopped")

if __name__=="__main__":
    main()