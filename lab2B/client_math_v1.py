import socket

# PORT e SERVER ADDRESS
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
# ----- enviar e receber strings ----- #
def receive_str(connect, n_bytes: int) -> str:
    data = connect.recv(n_bytes)
    return data.decode()

def send_str(connect, value: str) -> None:
    connect.send(value.encode())

def send_int(connect:socket.socket, value: int, n_bytes: int) -> None:
    connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

def receive_int(connect: socket.socket, n_bytes: int) -> int: 
    data = connect.recv(n_bytes)
    return int.from_bytes(data, byteorder='big', signed=True)
#-----------------------------------------------#

def main():
    #Socket & ligação
    connection = socket.socket()
    connection.connect((SERVER_ADDRESS,PORT))
    # Operação de soma
    send_str(connection,ADD_OP)
    # Perguntar ao utilizador quanto quer somar?
    a = 10
    b = 15
    send_int(connection,a, INT_SIZE)
    send_int(connection,b, INT_SIZE)
    res = receive_int(connection,INT_SIZE)
    print("O resultado da soma é:",res)
    # Operação de subtração
    send_str(connection,SUB_OP)
    # Perguntar ao utilizador que valores subtrair?
    send_int(connection,a, INT_SIZE)
    send_int(connection,b, INT_SIZE)
    res = receive_int(connection,INT_SIZE)
    print("O resultado da subtração é:",res)
    # Fechar a conexão
    send_str(connection,BYE_OP)
    connection.close()


if __name__=="__main__":
    main()