
# coding: utf-8

# In[ ]:
#Importando ferramenta de tempo para posteriormente fechar o aplicativo
import time

#Criando o retorno para o aplicativo não fechar automaticamente
def reiniciar():
    resposta = input("Deseja realizar outra operação? (S/N)"
                    "\n" ).upper()
    if resposta == 'S':
        Calculadora()
            
    elif resposta == "N":
        print("Obrigado por utilizar esta calculadora!")
        time.sleep(4)
        exit()
    
    else:
        print("Opção inválida")
        reiniciar()
            
#Criando a calculadora
def Calculadora(): 
    #Boas vindas da calculadora
    entrada = "********** Pyhton Calculator **********"
    print(entrada)

    #Dando primeiro comando ao usuário (escolha da operação)
    print("Selecione o número de acordo com a operação desejada: " "\n")

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    operacao = (int(input("Digite sua opção (1/2/3/4)" "\n")))
    
    # Dando segundo comando ao usuário (escolha dos números)
    
    #soma
    if operacao == 1:
        soma_lambda = lambda numero1, numero2: numero1 + numero2
        numero1 = float(input("Escolha o primeiro número que deseja operar: "))
        numero2 = float(input("Escolha o segundo número que deseja operar: "))
        print("O resultado da sua operação é:" "\n" + str(soma_lambda(numero1, numero2)))
        reiniciar()
                     
    #subtração
    elif operacao == 2:
        print("Você escolheu subtração")
        subtracao_lambda = lambda numero1, numero2: numero1 - numero2
        numero1 = float(input("Escolha o primeiro número que deseja operar: "))
        numero2 = float(input("Escolha o segundo número que deseja operar: "))
        print("O resultado da sua operação é:" "\n" + str(subtracao_lambda(numero1, numero2)))
        reiniciar()
        
    #multiplicação
    elif operacao == 3:
        print("Você escolheu multiplicação")
        multiplicacao_lambda = lambda numero1, numero2: numero1 * numero2
        numero1 = float(input("Escolha o primeiro número que deseja operar: "))
        numero2 = float(input("Escolha o segundo número que deseja operar: "))
        print("O resultado da sua operação é:" "\n" + str(multiplicacao_lambda(numero1, numero2)))
        reiniciar()
        
    #divisão
    elif operacao == 4:
        print("Você escolheu divisão")
        divisao_lambda = lambda numero1, numero2: numero1 / numero2
        numero1 = float(input("Escolha o primeiro número que deseja operar: "))
        numero2 = float(input("Escolha o segundo número que deseja operar: "))
            if numero2 == 0:
                print("Impossível dividir por zero")
                Calculadora()
            else:
                print("O resultado da sua operação é:" "\n" + str(divisao_lambda(numero1, numero2)))
                reiniciar()
        
    #opção inválida
    else:
        print("##############################################"
              "\n" "############### OPÇÃO INVÁLIDA ###############"
              "\n" "##############################################"
              "\nO processo começará novamente abaixo")
        
        Calculadora()
     

        
    
Calculadora()

