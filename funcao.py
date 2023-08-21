# -*- coding: utf-8 -*-

import math

'''Exemplo de Função no Python.

def soma(a,b):
    resultado = a+b
    return resultado

s = soma(1, 2)
print(s)


#Outro exemplo de definição de no python.

def area_triangulo(base, altura):
    area = (base * altura)/2
   
base = float(input('coloque o valor da base do triangulo: '))
altura = float(input('coloque o valor da altura do triangulo: '))
mult = area_triangulo(base, altura)
print('a area do triangulo é: ', mult)


#Outro exemplo de definição de função

def linha_separacao():
    return print('-'*30)
linha_separacao()
print(' Promoção de vinhos - queima de estoque')
linha_separacao()
print(' Promoção de vinhos - Queima de Estoque')
linha_separacao()


#Parâmetros

def imprime_nome(nome):
    print("Nome: {}".format(nome))
   
imprime_nome("Guilherme")
imprime_nome("Thomas")
imprime_nome("Otavio")


#Exercicio 1 - Calcular o dobro de um número.

def dobrar_numero():
    numero = float(input("Digite um numero: "))
    resultado = numero * 2
    return resultado

print("O dobro do número é: ",dobrar_numero())
         

#Exercicio 2 - Crie uma função que soma dois números inteiros.    
   
def somar_numeros():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))    
    resultado = numero1 + numero2
    return resultado

print("A soma dos dois números é: ",somar_numeros())


#Exercicio 3 - Crie uma função que forneça o módulo do número.

def valor_modulo():
    numero = float(input("Digite um número: "))
    resultado = (numero**2)**1/2
    return resultado

print("O modulo do número é: ",valor_modulo())


#Exercicio 4 - Crie uma função que forneça o quadrado do numero.

def quadrado_de_n():
    numero = float(input("Digite um número: "))
    resultado = numero**2
    return resultado

print('O quadrado do número é: ',quadrado_de_n())


#Exercicio 5 - Crie um código para calcular o Fatorial de um número.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input("Digite um número que você quer calcular o fatorial: "))

print("O fatorial de",n ,"é", fatorial(n))


#Exercicio 6 - Crie uma função que retorna o maior entre dois números.

def busca_maior():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2
   
print('O maior número é: ',busca_maior()


#Exercicio 7 - Crie uma função que retorne o antecessor do número.

def buscar_antecessor():
    numero = float(input("Digite um número: "))
    antecessor = numero - 1
    return antecessor

print('O antecessor é: ',buscar_antecessor())


#Exercicio 8 - Crie uma função que retorna o menor entre dois números

def busca_menor():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero1 < numero2:
        return numero1
    else:
        return numero2
   
print('O menor número é: ',busca_menor())


#Exercicio 9 - Crie uma função que verifica se um número é par:

def verificar_par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        return print("O número é par!")
    else:
        return print("O número é ímpar!")
   
print(verificar_par())


#Exercicio 10 - Crie uma para calcular a raiz quadrada de um número.

def raiz_quadrada():
    num = float(input("Digite um valor: "))
    quadrado = math.sqrt((num))
    return quadrado

print("A raiz quadrada é: ", raiz_quadrada())


#Exercicio 11 - Crie um codigo para somar dois numeros complexos

#Definição de Função

def somar_numeros_complexos(num1, num2):
    real = num1[0] + num2[0]
    imaginaria = num1[1] + num2[1]
    resultado = (real, imaginaria)
    return resultado

#Solicita as partes real e imaginÃ¡ria do primeiro nÃºmero complexo ao usuÃ¡rio
real1 = float(input("Digite a parte real do primeiro nÃºmero complexo: "))
imaginaria1 = float(input("Digite a parte imaginÃ¡ria do primeiro nÃºmero complexo: "))

#Solicita as partes real e imaginÃ¡ria do segundo nÃºmero complexo ao usuÃ¡rio
real2 = float(input("Digite a parte real do segundo nÃºmero complexo: "))
imaginaria2 = float(input("Digite a parte imaginÃ¡ria do segundo nÃºmero complexo: "))

#Cria as representações dos números complexos como tuplas (parte real, parte imaginária)
num1 = (real1, imaginaria1)
num2 = (real2, imaginaria2)

#Realiza a soma dos nÃºmeros complexos
soma = somar_numeros_complexos(num1, num2)

#Exibe o resultado
print("A soma dos números complexos Ã©:", soma)


#Exercicio 12 - Crie um codigo completo e detalhado que retorne as duas raizes de
#uma equação de segundo grau usando a formula de bascara


# Definição de função

def calcular_raizes(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz, raiz

    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

# Solicita os coeficientes da equaÃ§Ã£o de segundo grau ao usuÃ¡rio
coeficiente_a = float(input("Digite o coeficiente a: "))
coeficiente_b = float(input("Digite o coeficiente b: "))
coeficiente_c = float(input("Digite o coeficiente c: "))

# Calcula as razões
raiz1, raiz2 = calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)

# Exibe as razões
print("As razões da equaÃ§Ã£o sÃ£o:")
print("Raiz 1:", raiz1)
print("Raiz 2:", raiz2)


#Exercicio 13 - Crie um codigo para calcular o mudulo de um vetor... em N dimensões


#definição de função

def calcular_modulo_vetor(vetor):
    soma_quadrados = 0
    for componente in vetor:
        soma_quadrados += componente**2
    modulo = math.sqrt(soma_quadrados)
    return modulo

# Solicita as componentes do vetor ao usuário
dimensoes = int(input("Digite o número de dimensões do vetor: "))
vetor = []
for i in range(dimensoes):
    componente = float(input(f"Digite o componente {i+1} do vetor: "))
    vetor.append(componente)

# Calcula o módulo do vetor
modulo = calcular_modulo_vetor(vetor)

# Exibe o resultado
print("O módulo do vetor é:", modulo)


#Crie um codigo utilizando função para criar a sequencia de Fibonacci para os
#primeiro n elementos.
#Apresente-os e a seguir informe quais desses são numeros primo

#importar o sys
import sys

#Definir Função
def fibonacci(n):
    sequencia_fibonacci = [1, 1]

    while len(sequencia_fibonacci) < n:
       
        proximo_numero = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
        sequencia_fibonacci.append(proximo_numero)

    return sequencia_fibonacci

def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
   
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % 1 == 0:
            return False
       
    return True

n = int(input("Digite o valor de 'n': "))
fibonacci_seq = fibonacci(n)

#Mostra a sequência de Fibonacci
print("Sequência de Fibonacci:")
print(fibonacci_seq)

#Mostra quais números são primos
primos = [numero for numero in fibonacci_seq if eh_primo(numero)]
print("Números primos na sequência de Fibonacci:")
print(primos)

#Exercicio 15 - Parâmetros, argumentos, *args, **kwars

def cal_sal(valor, horas=220):
    return horas * valor

valor_total = cal_sal(299.25)
print (valor_total)

------------

def func_missao_dificil(nome, *args, funcao='agente', **kwargs):
    print(f'Nome do agente: {nome}')
    print(f'Função: {funcao}')
    print(args)
    print(kwargs)
   
params = {
             'id_agente': '007',
             'proxima_missao': 'Impossível'
         }

func_missao_dificil(
    'James Bond',
    'Missao 1',
    'Missao 2',
    **params
)

#----------


#Definição de função

def soma(*args):
    return sum(args)

resultado = soma (2, 4, 6, 8)
print(resultado) #Deve imprimir 20

#----------


#Exercicio 16 - Calculadora Avançada

#Definir função

def calculadora(**kwargs):
    num1 = kwargs.get('num1', 0)
    num2 = kwargs.get('num2', 0)
    operacao = kwargs.get('operacao', 'soma')
   
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return print('divisâo por zero')
       
resultado = calculadora(num1=10, num2=5, operacao='subtracao')
print(resultado)


#Exercicio 17 - Média Simples
#Crie uma função que recebe um número inderteminado de argumentos nomeados representado as notas

def media_nota(*args):
    return sum(args) / len(args)

numeros = [float(x) for x in input("Digite uma lista de números separados por espaço:").split()]
resultado = media_nota(*numeros)
print(f"A média é: {resultado}")


#Exercicio 18 - Concaenação de Strings

#Definir função

def concatena_strings(*args):
    return ''.join(args)

strings = input("Digite uma lista de strings separadas por espaço: ").split()
resultado = concatena_strings(*strings)
print(f"A concatenação das strings é: {resultado}")


#Exercicio 19 - Contagem de Vogais

#Definir função

def conta_vogais(*args):
    vogais = 'aeiouAEIOU'
    count = 0
    for arg in args:
        count += sum(1 for char in arg if char in vogais)
    return count

strings = input("Digite uma lista de strings separados por espaço: ").split()
resultado = conta_vogais(*strings)
print(f"Total de vogais: {resultado}")
'''

#Exercicio 20 - Calculadora de Desconto

#Definição de função

def calc_desc(**kwargs):
    total = kwargs.get('total', 0)
    desconto = kwargs.get('desconto', 0.1)
    valor_com_desconto = total * (1 - desconto)
    return valor_com_desconto

total = float(input("Digite o valor total: "))
desconto = float(input("Digite a taxa de desconto (em decimal): "))
resultado = calc_desc(total=total, desconto=desconto)
print(f"Total com desconto: {resultado}")