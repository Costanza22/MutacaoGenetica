import random

itens = [(2, 8), (2, 5), (2, 15), (2, 7), (2, 6)] 
capacidade_mochila = 10  
populacao_tamanho = 50 
geracoes = 200
taxa_mutacao = 0.1 

def aptidao(individuo):
    peso_total = 0
    valor_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso_total += itens[i][0]
            valor_total += itens[i][1]
    if peso_total > capacidade_mochila:
        return 0  
    else:
        return valor_total
populacao = []
for _ in range(populacao_tamanho):
    individuo = [random.randint(0, 1) for _ in range(len(itens))]
    populacao.append(individuo)

for geracao in range(geracoes):
    aptidoes = [aptidao(individuo) for individuo in populacao]
    
    nova_populacao = []
    total_aptidoes = sum(aptidoes)
    for _ in range(populacao_tamanho):
        pai1 = random.choices(populacao, weights=aptidoes)[0]
        pai2 = random.choices(populacao, weights=aptidoes)[0]
        filho = []
        for gene1, gene2 in zip(pai1, pai2):
            if random.random() < 0.5:
                filho.append(gene1)
            else:
                filho.append(gene2)
        nova_populacao.append(filho)
    for individuo in nova_populacao:
        for i in range(len(individuo)):
            if random.random() < taxa_mutacao:
                individuo[i] = 1 - individuo[i]
    
    populacao = nova_populacao


melhor_individuo = max(populacao, key=aptidao)
melhor_valor = aptidao(melhor_individuo)
print("Melhor solução:")
print("Itens selecionados:", [i+1 for i in range(len(itens)) if melhor_individuo[i] == 1])
print("Valor total:", melhor_valor)
