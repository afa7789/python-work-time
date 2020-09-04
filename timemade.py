import operator

def stringToInt(vetorString):
	retorno = []
	for i in vetorString:
		tup=i.split(':')
		horaMinutos = int(tup[0]) *60
		minutos =  int(tup[1]) + horaMinutos
		retorno.append(minutos)
	return retorno

text_file = open("file.txt", "r")
lines = text_file.readlines()
entrada=[]
saida=[]
for i in lines:
	tup = i.split('\t')
	entrada.append(tup[2])
	saida.append(tup[3])

entrada = stringToInt(entrada)
saida = stringToInt(saida)
calculado = map(operator.sub, saida, entrada) # in python 3, list(map(operator.sub, saida, entrada))

print sum(calculado)/60