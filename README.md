# python-time-in-week

- Pequeno script de python p/ interpretar os valores dos campos de hora trabalha na empresa, visto que acontece que quando se bate pontos adicionais eles ainda não são contabilizados por inteiro na contagem final. Portanto fiz um script so p/ ler e transformar tudo em minutos e subtrair e tomar quantas horas já foram feitas ao final.

- Para rodar :
 - `git clone https://github.com/afa7789/python-time-in-week.git contador`
 - `cd contador`
 - `python timemade.py`

exemplo de file.txt:

	exemplo	31/08/2020	11:42	11:54		  
	exemplo	31/08/2020	12:19	13:56		  
	exemplo	31/08/2020	16:08	17:45		  
	exemplo	31/08/2020	17:45	18:50		  
	exemplo	31/08/2020	18:53	19:14		  esqueci de bater o ponto novamente
	exemplo	31/08/2020	19:15	20:01		  
	exemplo	31/08/2020	20:01	20:27		  
	exemplo	01/09/2020	11:15	11:59		  
	exemplo	01/09/2020	12:03	12:32		  
	exemplo	01/09/2020	12:53	17:46		  Volta após almoço
	exemplo	01/09/2020	17:46	19:36		  
	exemplo	02/09/2020	10:02	10:48		  
	exemplo	02/09/2020	10:49	10:54		  
	exemplo	02/09/2020	11:48	11:54		  
	exemplo	02/09/2020	11:56	11:57		  
	exemplo	02/09/2020	12:45	13:20		  
	exemplo	02/09/2020	13:20	16:50		  
	exemplo	02/09/2020	16:50	19:17		  
	exemplo	03/09/2020	09:42	12:21		  
	exemplo	03/09/2020	13:36	14:37		  entrada após o almoço
	exemplo	03/09/2020	14:37	15:15		  
	exemplo	03/09/2020	15:17	17:35

## OBS: 
- o arquivo é uma copia da tabela com mouse, feito no gestor da empresa. é apenas copiar e colar e nomear de file.txt
- o padrão ali é ser separado por "\t".