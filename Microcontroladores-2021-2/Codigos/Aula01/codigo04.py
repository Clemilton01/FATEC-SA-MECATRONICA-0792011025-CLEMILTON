import random 
#utilizar uma lista
#adiciona um valor a lista no final da lista
#numeros_sorteados.append(45)
def gerarNumeros(quant_numeros,minimo,maximo):
    numeros_sorteados = []
    while len(numeros_sorteados)<quant_numeros:
        #adiciona umm numero inteiro aleatorio
        sorteio = random.randint(minimo, maximo)
        if sorteio not in numeros_sorteados:
            numeros_sorteados.append(sorteio)
    #coloca a lsta em ordem
    numeros_sorteados.sort()
    return numeros_sorteados
numeros_mega_sena = gerarNumeros(6,1,60)
print('mega sena:',numeros_mega_sena)
numeros_quina = gerarNumeros(5,1,80)
print('quina:',numeros_quina)
numeros_lotofacil = gerarNumeros(15,1,50)
print('lotofacil:',numeros_lotofacil)

