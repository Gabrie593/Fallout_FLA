# Obter o número a ser convertido
number = float(input("Type the number the you wanna convert: "))

# Definindo variáveis para uso posterior
binary = (" ")
zero = ("0")
one = ("1")

# Realizando a conversão
while number > 0:
    (division) = int(number) / 2
    if (division % 1) == 0:
        binary = binary + zero
    else:
        binary = binary + one
    number = int(division)

# Imprimindo o resultado de trás para a frente
print(binary[::-1])
    
    

