""" Syntax. """
# Como exibir uma mensagem.
	print "Welcome to Python!"

# Variaveis.
	number	= 	0			# Variavel de Numero.
	string	=	"Python"	# Variavel de Strings.

# Operações matemáticas.
	Addition 		= 	72 + 23		# 95.
	Subtraction 	= 	108 - 204	# -96.
	Multiplication 	= 	108 * 0.5	# 54.0.
	Division 		= 	108 / 9 	# 12.
	Squared			=	10 ** 2 	# 100.
	Exponentiation	=	3 ** 9 		# 19683.

# Calculando raiz quadrada.
	print sqrt(100)					# 10.

# Checando o tipo de variavel com type().
	print type(42)					# Int.
	print type(4.2)					# Float.
	print type('spam')				# Str.

""" Strings. """
"""
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5
"""

# Acessando por indice.
	print "MONTY"[4]		# Y.

# Exibindo o tamanho de uma string.
	print len("Python")		# 6.

# Convertendo uma string a minusculo.
	print "PYTHON".lower()	# python.

# Convertendo ao maiusculo.
	print "python".upper()	# PYTHON.

# Convertendo outros tipos de varaiveis ao string.
	print str(2)			# "2".

# Concatenação de Strings.
	print "Python" + " é " + "legal!"
	print "Python", "é", "legal!"

# Formatando strings com %.
	print "Estou aprendendo %s!" % ("Python")
	print "%s é %s" % ("Python", "legal")

""" Data e hora. """
# Importando.
	from datetime import datetime

# Exibindo data e hora.
	print datetime.now()

# Exibindo o dia.
	print now.day

# Exibindo o mês.
	print now.month

# Exibindo o ano.
	print now.year

# Exibindo a hora.
	print now.hour

# Exibindo os minutos.
	print now.minute

# Exibindo os segundos.
	print now.second

""" Condicionais e controle de fluxo. """
# Comparadores.
	Igual a ("==")
	Diferente de ("!=")
	Menor do que ("<")
	Menor ou igual a ("<=")
	Maior que (">")
	Maior ou igual a (">=")

# If/Else em single-line.
	linguagem = True if 100 != 10**2 else False	# False.

# Operadores booleanos.
    and (e), que verifica se as duas afirmações são True;
    or (ou), que verifica se pelo menos uma das afirmações é True;
    not (não), que gera o oposto da afirmação.

# Condicional If/Elif/Else.
	if 5 > 4:
		print "5 é maior que 4."
	elif 5 < 4:
		print "5 é menor que 4."
	else:
		print "5 é igual que 4."

# Condição if/else em single-line.
	print "5 é maior que 4" if 5 > 4 else "5 é menor ou igual que 4."

""" Funções. """
	def hello_world(n):
		print n

	hello_world(3)

""" Arrays """
# Layout de um array.
	ling 	=	["Python", "PHP", "Ruby"]

# Acessando itens.
	print ling[0]	# Python.
	print "Estou aprendendo", ling[0]

# Mudando itens.
	ling[2] = "Perl"	# Ruby vira Perl.

# Adicionando itens.
	ling.append("JavaScript")	# ["Python", "PHP", "Ruby", "JavaScript"]

# Removendo item.
	ling.remove("JavaScript")

# Numerando itens.
	print len(ling)

# Encontrando a posição de um item.
	print ling.index("Python")	# 0.

# Substituindo certo item.
	ling.insert(0, "C")	# Substitui Python por C.

# Printando cada item.
	for prog in ling:
		print "%s e uma linguagem de programacao." % (prog)

""" Dicionários. """
# Layout de um dicionário.
	lings	=	{"Python" : "Linguagem de programação.", "HTML" : "Linguagem de marcação"}

	lings = {
	"Python"	:	"Linguagem de programacao.",
	"HTML"		:	"Linguagem de marcacao"}

# Exibindo o valor de um key.
	print lings["Python"]	# Linguagem de programacao.

# Adicionando mais keys/values.
	lings["CSS"]	=	"Linguagem de estilo."

# Removendo um item.
	del lings["CSS"]

# Exibindo todas as keys.
	print my_dict.keys()

# Exibindo todos os values.
	print my_dict.values()

""" Loops. """
# Loop com While().
	count = 0
	while count < 10:
	    print "Hello, I am a while and count is", count
	    count += 1

# Loop com for.
	for i in range(20):
	    print i

""" Manipulando arquivos com open(). """
Modo de escrita. 			("w"). 	# Você só escreve.
Modo de leitura. 			("r"). 	# Você só poderá ler.
Modo de leitura e escrita. 	("r+").	# Você pode ler e escrever o arquivo.
Modo de adição. 			("a"). 	# Adiciona quaisquer novos dados que você gravar ao fim do arquivo.

# Abrindo um arquivo.
	my_file =   open("output.txt", "r+")

# Fechando um arquivo.
	my_file.close()

# Escrevendo um arquivo.
	my_file.write("Algo para escrever.")
	my_file.close()

# Lendo o arquivo.
	print my_file.read()
	my_file.close()

# Lendo linha por linha.
	print my_file.readline()	# Lê a primeira linha.
	print my_file.readline()	# Lê a segunda linha.
	my_file.close()
