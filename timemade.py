import operator
import sys

def stringToInt(vetorString):
	retorno = []
	for i in vetorString:
		tup=i.split(':')
		horaMinutos = int(tup[0]) *60
		minutos =  int(tup[1]) + horaMinutos
		retorno.append(minutos)
	return retorno

soma=0;

for i in range(1,len(sys.argv)):
	text_file = open(sys.argv[i], "r")
	lines = text_file.readlines()
	entrada=[]
	saida=[]
	for i in lines:
		tup = i.split('\t')
		if ":" not in tup[3]:
			continue
		entrada.append(tup[2])
		saida.append(tup[3])

	entrada = stringToInt(entrada)
	saida = stringToInt(saida)
	calculado = map(operator.sub, saida, entrada) # in python 3, list(map(operator.sub, saida, entrada))
	soma+=sum(calculado)

print str(soma/60) + " horas " + str(soma%60) + " minutos"