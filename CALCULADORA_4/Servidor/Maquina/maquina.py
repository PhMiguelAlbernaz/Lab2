
from Servidor.Operacoes import somar, subtrair, dividir, multiplicar, raiz
import socket
import json
class Maquina:
    def __init__(self):
        self.somar= somar.Somar()
        self.subtrair= subtrair.Subtrair()
        self.multiplicar= multiplicar.Multiplicar()
        self.dividir= dividir.Dividir()
        self.raiz= raiz.Raiz()
        self.COMMAND_SIZE = 9
        self.INT_SIZE = 8
        self.PORT = 3500
        self.SERVER_ADDRESS = "127.0.0.1"

    def receive_int(self,connection, n_bytes: int) -> int:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next integer read from the current connection
        """
        data = connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self,connection, value: int, n_bytes: int) -> None:
        """
        :param value: The integer value to be sent to the current connection
        :param n_bytes: The number of bytes to send
        """
        connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_str(self,connection, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connection.recv(n_bytes)
        return data.decode()

    def send_str(self,connection, value: str) -> None:
        """
        :param value: The string value to send to the current connection
        """
        connection.connection.send(value.encode())

    # TODO
    # Implement a method that sends and object and returns an object.
    # ...
    def send_object(self,connection, obj):
        """1º: envia tamanho, 2º: envia dados."""
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, self.INT_SIZE)  # Envio do tamanho
        connection.send(data)  # Envio do objeto

    def receive_object(self,connection):
        """1º: lê tamanho, 2º: lê dados."""
        size = self.receive_int(connection, self.INT_SIZE)  # Recebe o tamanho
        data = connection.recv(size)  # Recebe o objeto
        return json.loads(data.decode('utf-8'))

    def execute(self):
        """
            Runs the server server until the client sends a "terminate" action
    """
        s = socket.socket()
        s.bind(('', self.PORT))
        s.listen(1)
        print("Waiting for clients to connect on port " + str(self.PORT))
        keep_running = True
        while keep_running:
            print("On accept...")
            connection, address = s.accept()
            print("Client " + str(address) + " just connected")

            #Recebe messagens...
            last_request=False
            while not last_request:
                request_type = self.receive_str(connection,self.COMMAND_SIZE)
                if request_type == "add_obj  ":
                    dicionary = self.receive_object(connection)
                    if type(dicionary)==dict:
                        if dicionary["oper"]=="+":
                            result=dicionary["op1"]+dicionary["op2"]
                            dicionary["result"]=result
                            self.send_object(connection,dicionary)
                        elif dicionary["oper"]=="-":
                            result=dicionary["op1"]-dicionary["op2"]
                            dicionary["result"]=result
                            self.send_object(connection,dicionary)

                        elif dicionary["oper"]=="x":
                            result=dicionary["op1"]*dicionary["op2"]
                            dicionary["result"]=result
                            self.send_object(connection,dicionary)

                        elif dicionary["oper"]=="/":
                            result=dicionary["op1"]/dicionary["op2"]
                            dicionary["result"]=result
                            self.send_object(connection,dicionary)

                        elif dicionary["oper"]=="*":
                            result=dicionary["op1"]**(1/2)
                            dicionary["result"] = result
                            self.send_object(connection, dicionary)

                        else:
                            print("erro")
                    elif type(dicionary)==list:
                        if dicionary[0] == "+":
                            result = dicionary[1] + dicionary[2]
                            dicionary.append(result)
                            self.send_object(connection, dicionary)
                        elif dicionary[0] == "-":
                            result = dicionary[1] - dicionary[2]
                            dicionary.append(result)
                            self.send_object(connection, dicionary)

                        elif dicionary[0] == "x":
                            result = dicionary[1] * dicionary[2]
                            dicionary.append(result)
                            self.send_object(connection, dicionary)

                        elif dicionary[0] == "/":
                            result = dicionary[1] / dicionary[2]
                            dicionary.append(result)
                            self.send_object(connection, dicionary)

                        elif dicionary[0] == "*":
                            result = dicionary[1] ** (1 / 2)
                            dicionary.append(result)
                            self.send_object(connection, dicionary)

                        else:
                            print("erro")
                elif request_type =="bye      ":
                    print("Last request...")
                    last_request = True
                    keep_running = False

        print("Stopping...")
        s.close()
        print("Server stopped")

