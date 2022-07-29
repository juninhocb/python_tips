
def main7(nmr):
    try:
        return nmr*main7(nmr-1) if nmr != 1 else 1
    except Exception as e:
        print(f"Excessão ao fazer o fatorial do número {nmr}: ", type(e))
        return

def main6(nmr1, nmr2, nmr3):
    return nmr1*nmr2*nmr3

def main5(**kwargs):  
    ## **kwargs não aceita dicionários no parâmetro, ele recebe os dados como Chave/valor e transforma-os em um dicionário
    print(type(kwargs)) ## <class 'dict'>
    for key, value in kwargs.items():
        print(f"Chave {key} e valor {value}")

def main4(*args):
    print(type(args)) # <class 'tuple'>
    print(args)  # ([1, 2, 3, 4, 5, 6],)
    try:
        print(args[3]) 
    except Exception as e: 
        print(type(e))
    ## RESPOSTA: <class 'IndexError'>
    ### MAX ##### 
    # identificando o maior número passado nos argumentos
    print(max(tuple(args[0]))) #6
    
def main3(*args):
    print(type(args)) # <class 'tuple'>  ## sempre será uma tupla, não importa o tipo do parâmetro passado
    print(args) #('Passando', 'Vários', 'Argumentos', 'Para', 'A', 'Função')
    print(args[0]) #Passando
    ########## MAX ##############
    # identificando o maior número da tupla pelo número de caracteres
    print(max(args, key = len))

def main2():
    print("rodarei por segundo")

def main ():
    print("sou o main do programa.")

########## classifica main como a função principal do sistema, depois rodará main2
if __name__ == '__main__': 
    main()
    print("entre as funções!!!")
    main2()
    main3("Passando", "Vários", "Argumentos", "Para", "A", "Função")
    main4([1,2,3,4,5,6])
    main5(nome = "andré", idade = "15", ocupacao = "andarilho")
    print(main6(1,2,3))  # 6
    try:
        print(main7(int(input("Digite um valor para calcular seu fatorial: "))))
    except Exception as e:
        print("Apenas valores inteiros são aceitos!!!", type(e))