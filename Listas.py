l = [1,2,3,4,5,6]
lStr = ["ana", "carolina", "joao", "joaquina"]
def multiplica2(nmr):
    return nmr*2
#################### ACESSANDO ELEMENTOS DA LISTA ###########
print(lStr[0]) #ana
print(lStr[0:2]) #['ana', 'carolina']
#acessando todos eles
for i in lStr: 
    print(i)
## ou 
for i in range(len(lStr)):
    print(lStr[i])

####################### ACESSANDO O ÚLTIMO ELEMENTO DA LISTA ########
print("Último elemento da lista: ", lStr[-1])

####################### CLONANDO UMA LISTA SEM MANTER A REFERENCIA ENTRE ELAS ########
# fazendo isto, quando mudar l, não mudaremos l2 
l2  = l[:]
print("Lista clonada! ", l2)  ##  [1, 2, 3, 4, 5, 6]

#################### SUBSTITUINDO ELEMENTOS DA LISTA ###########
lStr[0] = "Carla" 
print(lStr) #['Carla', 'carolina', 'joao', 'joaquina']

## verifica se há elemento na lista

print('carolina' in lStr)  #true
print('roberta' in lStr) #false

#################### DESCOBRINDO O MAIOR ELEMENTO DA LISTA ###########
print(f"Maior número da lista: {max(l)}")

#################### DESCOBRINDO O MENOR ELEMENTO DA LISTA ###########
print(f"Menor número da lista: {min(l)}")

#################### DESCOBRINDO O ELEMENTO COM MAIOR NMR DE CARACTERES DA LISTA ###########
print(f"Elemento com maior número de caracteres da lista: {max(lStr, key= len)}")

#################### ENUMERATE ###########
# enumerando os elementos de uma lista
for key, values in enumerate(lStr):
    print(f"Elemento: {values} com chave: {key} ")

#################### ZIP ###########
# atribuindo valores de uma lista a outra 
## OBS*** NAO PRECISAM SER DO MESMO TAMANHO, ELE FAZ A ATRIBUICAO DOS PONTOS ATE O TAMANHO MAX DA MENOR DELAS
for numbers, names in zip(l, lStr):
    print(f"Número: {numbers} Nome: {names}")

#################### LEN ###########
#verificando o tamanho da lista
print(len(lStr))  # 4
print(len(l)) # 6

#################### LIST COMPREHENSION ###########
# adicionando elementos em uma lista com list comprehension
l2 = [i for i in range(5)]
print(l2) #[0, 1, 2, 3, 4]
l3 = [multiplica2(i) for i in range(4)]
print(l3) #[0, 2, 4, 6]
l4 = [i+1 for i in l]
print(l4) #[2, 3, 4, 5, 6, 7]

#################### APPEND ###########
#adicionando elementos na lista
lStr.append("roberta")
print(lStr) #['Carla', 'carolina', 'joao', 'joaquina', 'roberta']


####################  INDEX ###########
# retorna o índice da lista do elemento que quer acessar
try: 
    print(f"Número do índice procurado é {lStr.index('roberta')}")
except Exception as e:
    print("Não existe esta string na lista de strings... Erro: ", type(e))

################## INSERT #############
# adiciona elementos na lista em um determinado indice
lStr.insert(3, "joana")
print(lStr)  #['Carla', 'carolina', 'joao', 'joana', 'joaquina', 'roberta']

################## REMOVE #############
# remove um elemento pelo valor
lStr.remove("joaquina")
print(lStr) # ['Carla', 'carolina', 'joao', 'joana', 'roberta']

################## DEL #############
# remove um elemento da lista pelo índice
del(lStr[0])
print(lStr)  #['carolina', 'joao', 'joana', 'roberta']

################## POP #############
# remove um elemento da lista pelo índice e retorna seu valor 
print(lStr.pop(0)) #carolina

# se chamar a função sem parâmetros ele remove o último elemento
print(lStr.pop()) # roberta

######################### SORT #############
# ordenando listas
l3 = ["c", "a", "b"]
l3.sort()
print(l3) #['a', 'b', 'c']
# de forma contrária 
l3.sort(reverse= True)
print(l3) #cba
l.sort(reverse= True)
print(l) #[6, 5, 4, 3, 2, 1]
l4 = ['3', '1', '2', '21']
l4.sort()
print(l4) #['1', '2', '21', '3']
#aplicando parse nos valores
l4.sort(key = lambda str : int(str))
print(l4)

######################### SORTED #############
# igual ao sort, porém retorna uma lista
print(sorted(l4, key= lambda str:int(str)))   #['1', '2', '3', '21']
