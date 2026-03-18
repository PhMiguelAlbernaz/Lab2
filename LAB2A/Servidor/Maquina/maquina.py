from Servidor.Operacoes import somar, subtrair, dividir, multiplicar, raiz
class Maquina:
    def __init__(self):
        pass
        self.somar= somar.Somar()
        self.subtrair= subtrair.Subtrair()
        self.multiplicar= multiplicar.Multiplicar()
        self.dividir= dividir.Dividir()
        self.raiz= raiz.Raiz()
    def execute(self, op:str, num1:float,num2:float):
        match op:
            case "+":
                res= self.somar.executar(num1,num2)
                return res
            case "-":
                res= self.subtrair.executar(num1,num2)
                return res
            case "x":
                res= self.multiplicar.executar(num1,num2)
                return res
            case "/":
                res= self.dividir.executar(num1,num2)
                return res
            case "*":
                res=self.raiz.executar(num1)
                return res
            case _:
                return None


