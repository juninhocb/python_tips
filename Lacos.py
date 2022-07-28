nomes = ["carla", "roberto", "patricia", "joao"]
idades = [15, 18, 20, 12, 28]
#################### OPERADOR TERNÁRIO ###################
x = 10
print ("par" if x % 2 == 0 else "impar") 
#################### ZIP ###################
for n, i in zip(nomes, idades):
    print("nome:", n + " idade:", i)

strr = "Andar de avião é legal"
strList = strr.split()
#################### ENNUMERATE ###################
for key, value in enumerate (strList):
    print(f'Palavra {key}: {value}')
 #################### LIST COMPREHENSION ###################   
y = [i for i in strList]
print(y)
reformulando = " ".join(y)
print(f"{nomes[0][0:1].upper()}{nomes[0][1:]} disse que {reformulando.lower()}")
 #################### WHILE SIMPLES ################### 
n = 5
it = 1
while n >= 1: 
    print(f'nmr da iteração {it}')
    n -= 1
    it +=1
#################### WHILE FOREVER ###################  
# [2]BREAK SAI DO WHILE
# [4]CONTINUE SAI APENAS DO BLOCO DE FUNCAO QUE ESTÁ, MAS VOLTA AO WHILE SEM PASSAR PELO RESTO DO CÓDIGO   
# [5]PASS APENAS DEIXA PASSAR PARA PROXIMA INSTRUCAO
while True:
    
    x = input('digite um valor: ')
    if x == '3':
        print('executando')
    if int(x) == 2:
        print('saindo')
        break
    if x == '4':
        print('executando, mas sem o opa')
        continue
    if x == '5':
        print("Opa, executando")
        pass
        print("Executarei!!!")
    
    print('opaa')
    
print('saí do while e to saindo')