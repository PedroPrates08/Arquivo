#Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.   


#Informando como o usuário ira digitar o seu arquivo
arq = input("Digite o nome do arquivo que vc deseja abrir: ")

#Abrindo o arquivo digitado pelo usuário
arquivo = open(arq)

#Lendo a(s) linha(s) do arquivo aberto pelo usuário
linhas  = arquivo.readlines()

#Lendo o arquivo aberto, linha por linha
for linha in linhas:
    print(linha)


