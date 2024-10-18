#importar a biblioteca para operar com vetores
import numpy as np
#importar a biblioteca para plotar o autômato
import matplotlib.pyplot as plt

#criar uma função que aplica a regra de transição
def AplicarRegra(estado_atual):
    #criar um vetor de zeros do mesmo tamanho do vetor de estados atuais
    novo_estado = np.zeros(shape=estado_atual.shape)

    #percorrer todas as células do autômato celular
    for i in range(celulas):
        #identificar o padrão formado pela célula e suas duas vizinhas imediatas
        padrao = f'{estado_atual[i-1]}{estado_atual[i]}{estado_atual[(i+1)%celulas]}'
        #atribuir o novo estado utilizando os padrões da regra selecionada
        novo_estado[i] = padroes[padrao]
    
    #retorna o vetor com os estados do próximo passo de tempo
    return novo_estado
    
#definir o número da regra
regra = 30
#converter a regra para base binária
regra_bin = format(regra,'08b')

#relacionar os bits da regra com os possíveis padrões
padroes = {'111':regra_bin[0],'110':regra_bin[1],'101':regra_bin[2],'100':regra_bin[3],
           '011':regra_bin[4],'010':regra_bin[5],'001':regra_bin[6],'000':regra_bin[7]}

#definir a quantidade de passos
passos = 1000

#calcular a quantidade de células
celulas = 1 + 2 * passos

#selecionar o índice da posição central do autômato
centro = celulas // 2

#definir a matriz que é o autômato celular em si
grade = np.zeros(shape=(passos+1,celulas),dtype=int)

#definir a configuração inicial com apenas a célula central viva
grade[0,centro] = 1

#aplicar a função de transição pelo número de passos
for t in range(1,passos+1):
    #aplica a função no conjunto de estados do passo de tempo anterior
    novo_estado = AplicarRegra(grade[t-1])
    #atribui o conjunto de estados para o passo de tempo atual
    grade[t] = np.copy(novo_estado)

#criar a figura
fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(19.20,10.80),dpi=400,tight_layout=True)

#adicionar informações ao título do gráfico
ax.set_title(f'Regra {regra} - {passos} passos de tempo')

#definir a legenda do eixo x
ax.set_xlabel('Células')

#definir a legenda do eixo y
ax.set_ylabel('Passos de tempo')

#desenhar o autômato celular na figura
ax.imshow(X=grade,cmap='binary')

#mostrar na tela
#plt.show()

#salvar figura
plt.savefig(f'regra{regra}_{passos}passos.png')

#fechar a figura
plt.close()
