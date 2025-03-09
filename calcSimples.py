def somar(num1,num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def multiplica(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    if num2 == 0:
        print("Não é possivel fazer divisão a zero")
        return None
    else:
        return num1 / num2

def main():
    print("Calculadora simples, digite uma opção:")
    escolha = input("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n")
    escolha = int(escolha)
    
    num1, num2 = input("Digite os dois valores desejados, separados por virgula:").split(",")
    num1, num2 = int(num1), int(num2)
    
    if escolha == 1:
        print(somar(num1, num2))
    elif escolha == 2:
        print(subtrair(num1,num2))
    elif escolha == 3:
        print(multiplica(num1,num2))
    elif escolha == 4:
        resultado = dividir(num1,num2)
        if resultado is not None:
            print(resultado)
    else:
        print("Escolha errada, tente novamente")

if __name__ == "__main__":
    main()