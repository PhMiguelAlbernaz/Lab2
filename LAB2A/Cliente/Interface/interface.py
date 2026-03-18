from Servidor.Maquina import maquina


class Interface:
	def __init__(self):
		self.maquina = maquina.Maquina()
		pass
	def execute(self):
		print("Qual é o cálculo que quer efetuar? x + - / *")
		res:str = input()
		print("Preciso que introduza dois valores:")
		x:float = float(input("x="))
		y:float = float(input("y="))
		resultado=self.maquina.execute(res,x,y)
		print(resultado)

