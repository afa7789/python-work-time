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
	marcado=''
	for i in lines:
		tup = i.split('\t')
		print tup
		if ( len(tup) < 4 ):
			tup = i.split(' ')
			if (marcado == ''):
				for i in range(0,len(tup)):
					if '/' in tup[i]:
						marcado=i
			if ( len(tup) >= marcado+3 and ":" in tup[marcado+2] ) :
				entrada.append(tup[marcado+1])
				saida.append(tup[marcado+2])
		else:
			if (marcado == ''):
				for i in range(0,len(tup)):
					if '/' in tup[i]:
						marcado=i
			if ":" not in tup[marcado+2]:
				continue
			entrada.append(tup[marcado+1])
			saida.append(tup[marcado+2])

	entrada = stringToInt(entrada)
	saida = stringToInt(saida)
	calculado = map(operator.sub, saida, entrada) # in python 3, list(map(operator.sub, saida, entrada))
	soma+=sum(calculado)

print str(soma/60) + " horas " + str(soma%60) + " minutos"