# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
odd_numbers = 0
even_numbers = 0
 
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
 
# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)

#Determinadas expressões podem ser simplificadas sem alterar o comportamento do programa.
#Tente se lembrar de como o Python interpreta a verdade de uma condição e observe que essas duas formas são equivalentes:
#while number != 0: e while number:.

# Definir um número de chances

counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)

# Exemplo de 'for'

for i in range(10):
   print("O valor de i é atualmente", i)

# Potencia
 
power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)

  power *= 2   

  
import time
i = 1
for i in range(6):
   print(i, "Mississippi") 
   time.sleep(1)
   print("Pronto ou não, aqui vou eu!")     
