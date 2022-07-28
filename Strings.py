string = "olá mundo"
newStr = "Ol@ Mundo Especial!!!"
newStr2 = " Olá mundo com espaços indevidos   "
newStr3 = "Ol1 Mundo23 Especial12!!!"
listString = ["o","l","á","m","u","n","d","o"]
#tamanho da string
print(len(string)) #9

## acessando pontos da string
print(string[:2]) #ol
print(string[1:])  #lá mundo
print(string[1]) # l

## acessando pelo final da string
print(string[-2:]) #do
print(string[-9:]) #olá mundo pelo final da string

## acessando pelo final
print(string[:-1]) #olá mund

#invertendo
print(string[::-1]) #odnum álo

##concatenando
print(string + "! sou o José") #olá mundo! sou o José

## verificando se há determinadas letras na string
print(True if "a" in string else False) #false
print(True if "o" in string else False) #true
print(True if not "á" in string else False) #false

########################## METODOS #########################################################
#################### FIND ###################
## encontrando um valor na string com o metodo find, utilizado apenas em string
print(string.find("a")) # -1
print(string.find("o")) # 0
#################### INDEX ###################
## encontrando um valor na string com o metodo index, este, pode ser utilizado em uma lista, tupla e gera uma excessão
try:
    print(string.index("a"))
except Exception as e:
    print("Ocorreu uma excessão: ", type(e))
### RESULTADO: Ocorreu uma excessão:  <class 'ValueError'>
try:
    print(string.index("o")) 
except Exception as e:
    print("Ocorreu uma excessão: ", type(e))
### RESULTADO: 0
###################### UPPER #########################
## colocando toda a cadeia da string em maísculo   ------- upper()
print(string.upper()) # OLÁ MUNDO
###################### LOWER #########################
## agora colocando partes em maísculo e outras partes em minusculo  ------ lower()
print(string[0:2].upper() + string[2::].lower())  ##OLá mundo
###################### STR #########################
## converter int para str ------- str(arg1)
inteiro = 2 
print(type(str(inteiro)))   ## <class 'str'> lembrando que em python tudo é um objeto
###################### REPLACE #########################
##substituindo caractere em uma string --- replace(arg1, arg2)
print(string.replace("olá", "hello")) ##hello mundo
###################### ISALPHA #########################
## verificando se a string contém apenas letras (não pode haver espaço nem letras com acento)  ----- isalpha()
print(string.replace("á", "a").isalpha())  #False
print(string[0:2].isalpha())  #True
###################### ISALNUM #########################
## verificando se é um alfanúmerico  ----- isalnum()
print("ol21wksjs23".isalnum()) #True
###################### STRIP #########################
## retirando os espaços em branco ------- strip()
print(newStr2) #' Olá mundo com espaços indevidos   ' 
print(newStr2.replace("com", "sem").strip())  # 'Olá mundo sem espaços indevidos'
###################### JOIN #########################
## juntando a string com um delimitador específicado
print("-".join(listString))  #o-l-á-m-u-n-d-o
print("H".join(listString)) #oHlHáHmHuHnHdHo
print(" ".join(listString)) #o l á m u n d o
###################### JOIN COM FILTRO #########################
print(" ".join(filter(str.isalpha, newStr))) #O l M u n d o E s p e c i a l
print("".join(filter(str.isalnum, newStr3)))  #Ol1Mundo23Especial12
###################### SPLIT #########################
## Separando uma string conforme um delimitador (que será excluído da string), transformando ela em uma lista
print(string.split())  #['olá', 'mundo']
print(string.split('o')) #['', 'lá mund', '']












