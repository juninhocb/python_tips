import locale
import json
dic = {"nome": "Carla", "idade": 19, "habilidades" : ['andar de skate', 'jogar bola']}
print(dic)  # {'nome': 'Carla', 'idade': 19, 'habilidades': ['andar de skate', 'jogar bola']}

##################### ACESSANDO OS DADOS ##################### 
print(dic['nome']) # Carla

print(type(dic['habilidades'])) # <class 'list'>
print(dic['habilidades']) # ['andar de skate', 'jogar bola']
print(dic['habilidades'][0]) # andar de skate


#####################  ATRIBUINDO VALORES ################### 
dic['idade'] = 20
print(dic) #{'nome': 'Carla', 'idade': 20, 'habilidades': ['andar de skate', 'jogar bola']}

#####################  DICIONARIO DENTRO DE DICIONARIO ################### 
dic2 = {"nome": "Eliana", "idade": 21, "habilidades": ['jogar bola']}

pessoas = {1: dic, 2: dic2}
print(pessoas)  # {1: {'nome': 'Carla', 'idade': 20, 'habilidades': ['andar de skate', 'jogar bola']}, 2: {'nome': 'Eliana', 'idade': 21, 'habilidades': ['jogar bola']}}
print(pessoas[2]) #{'nome': 'Eliana', 'idade': 21, 'habilidades': ['jogar bola']}
print(type(pessoas)) # <class 'dict'>

####################### ACESSANDO OS DADOS ITERANDO SOBRE ELES #############################
for data in dic: 
    print(data + " " + str(dic[data]))  ### nome Carla  \n idade 20 \n habilidades ['andar de skate', 'jogar bola']
# por padrão os dados vem em forma das chaves!!!, para pegar os valores, deve-se utilizar dic ['nome_chave'] como feito no primeiro acesso

########################### METODOS #############################

######################## ITEMS ############### 
# retornam os valores em dict items
print(dic.items())  # dict_items([('nome', 'Carla'), ('idade', 20), ('habilidades', ['andar de skate', 'jogar bola'])])
print(type(dic.items())) # <class 'dict_items'> 

# para acessar o valor do items, utiliza-se a chave valor

for key, value in dic.items():
    print(f"Chave: {key} com Valor: {value}")  
'''
Chave: nome com Valor: Carla
Chave: idade com Valor: 20
Chave: habilidades com Valor: ['andar de skate', 'jogar bola']
'''

######################## VALUES ############### 
# utilizado para pegar os valores do dicionário
print(dic.values())  # dict_values(['Carla', 20, ['andar de skate', 'jogar bola']])
for values in dic.values():
    print(values)
'''
Carla
20
['andar de skate', 'jogar bola']
'''

######################## KEYS ############### 
print(dic.keys()) # dict_keys(['nome', 'idade', 'habilidades'])

#################### DICT COMPREHENSIONS ################### 
# análogamente as list comprehensions criaremos um dicionário
dic3 = {i*1 : i*2 for i in range(5)}
print(dic3) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

#iterando sobre duas listas
nomes = ["carolina", "ana", "flavia"]
idades = [15, 16, 18]

dic4 = {nomes : idades for nomes, idades in zip(nomes,idades)}
print(dic4) # {'carolina': 15, 'ana': 16, 'flavia': 18}

########## iterando sobre uma lista
dic5 = {i : i for i in idades}
print(dic5)  #{15: 15, 16: 16, 18: 18} 
# OBS: SE FOR ITERAR COM UMA STRING, EXEMPLO "IDADES: ", o Dict será preenchido apenas com o último valor, por obterem chaves iguais

###################### iterando sobre um dict e uma lista
locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8') # deixando o valor em reais
celulares = ['iphone', 'android', 'google']
valores = {"preco1" : 1200, "preco2" : 1500, "preco3": 1800}
dic6 = {celulares: valores for celulares, valores in zip(celulares, valores.items())}
print(dic6)  ## {'iphone': ('preco1', 1200), 'android': ('preco2', 1500), 'google': ('preco3', 1800)}
## retirndo os preços
dic7 = {celulares: locale.currency(valores) for celulares, valores in zip(celulares, valores.values())}
print(dic7)  #{'iphone': 'R$ 1200,00', 'android': 'R$ 1500,00', 'google': 'R$ 1800,00'}

########## filtrando valores com condicional 
dic8 = {cel: locale.currency(val) for cel, val in zip(celulares, valores.values()) if val > 1300}  
print(dic8) # {'android': 'R$ 1500,00', 'google': 'R$ 1800,00'}

dic9 = {cel: locale.currency(val) if val > 1300 else f"valor abaixo! {val}" for cel, val in zip(celulares, valores.values())} 
print(dic9) # {'iphone': 'valor abaixo! 1200', 'android': 'R$ 1500,00', 'google': 'R$ 1800,00'}

dic10 = {f"{cel} *Valor abaixo do preço estipulado" if val  < 1300 else cel : locale.currency(val) for cel, val in zip(celulares, valores.values())}
print(dic10) # {'iphone *Valor abaixo do preço estipulado': 'R$ 1200,00', 'android': 'R$ 1500,00', 'google': 'R$ 1800,00'}

##################### TRABALHANDO COM JSON ##################### 
with open("pessoas.json") as json_data:
    python_data = json.load(json_data)

print(type(python_data)) # <class 'dict'>
print(python_data)
'''
{'pessoas_buri': [{'name': 'Ana', 'idade': 25, 'clt': True}, {'name': 'Paula', 'idade': 20, 'clt': False}], 
'pessoas_capao': [{'name': 'Andressa', 'idade': 19, 'clt': False}]}
'''

# acessando os dados da Paula
print(python_data['pessoas_buri'][1])  # {'name': 'Paula', 'idade': 20, 'clt': False}
print(python_data['pessoas_buri'][1].values()) # dict_values(['Paula', 20, False])
print(python_data['pessoas_buri'][1].items()) # dict_items([('name', 'Paula'), ('idade', 20), ('clt', False)])
for key, values in python_data['pessoas_buri'][1].items():
    print(f"Chave: {key} Valor: {values}")

'''
Chave: name Valor: Paula
Chave: idade Valor: 20
Chave: clt Valor: False
'''
### acessando uma lista de json 
with open("pessoasLista.json") as json_dataList:
    python_dataList = json.load(json_dataList)

print(type(python_dataList))  # <class 'list'>
print(python_dataList)
'''
[
{'pessoas_buri': [{'name': 'Ana', 'idade': 25, 'clt': True}, {'name': 'Paula', 'idade': 20, 'clt': False}], 
'pessoas_capao': [{'name': 'Andressa', 'idade': 19, 'clt': False}]}, {'estados unidos': {
'pessoas_novayork': [{'name': 'Jhon', 'idade': 35, 'clt': False}], 
'pessoas_chicago': [{'name': 'Clarie', 'idade': 18, 'clt': False}, {'name': 'Anne', 'idade': 24, 'clt': False}]}}]
'''

'''
https://docs.python.org/pt-br/3/library/json.html#encoders-and-decoders
tipo de dados apos serem convertidos
'''

########### LENDO UMA STRING PYTHON NO FORMATO JSON E TRANSFORMANDO EM DADOS PYTHON ##########

jsonStringData = """
  {
  "pessoas_buri":
    {
        "name": "Ana",
        "idade": 25,
        "clt": true
    }
}
 """


python_data_from_python_string = json.loads(jsonStringData)
print(f"Dados da string python: {python_data_from_python_string}")
#Dados da string python: {'pessoas_buri': {'name': 'Ana', 'idade': 25, 'clt': True}}


#### transformando dados do python em formato de dados JSON
dicWillJson  = {
    "name": "Kennedy",
    "idade": 18,
    "clt": False
}

jsonObject = json.dumps(dicWillJson)
print(type(jsonObject))  # <class 'str'>
print(jsonObject)  # {"name": "Kennedy", "idade": 18, "clt": false}

dicWillJson2  = {
    "name": "Kennedy",
    "idade": 18,
    "habilidades": ["jogar bola", "jogar xadrez"] 
}

#colocar as chaves em ordem alfabetica
jsonObject2 = json.dumps(dicWillJson2, sort_keys= True)
print(jsonObject2)  # {"habilidades": ["jogar bola", "jogar xadrez"], "idade": 18, "name": "Kennedy"}

#escrever em um arquivo json
with open('novas_pessoas.json', 'w') as new_pessoas:
    json.dump(dicWillJson2, new_pessoas)


# escrever em um arquivo json com a identação json
with open('novas_pessoas2.json', 'w') as new_pessoas2:
    json.dump(dicWillJson, new_pessoas2, indent= 4)


