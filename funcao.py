# -*- coding: utf-8 -*-

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

import math

def raiz_quadrada():
    num = float(input("Digite um valor: "))
    quadrado = math.sqrt((num))
    return quadrado

print("A raiz quadrada é: ", raiz_quadrada())


#Exercicio 11 - Crie um código para somar dois números complexos. (incompleto)

#Definir uma função
def somar_numeros_complexos(num1, num2):
real = num1[0]

#Solicita partes real e imaginatoria do primeiro complexo ao usuario.
real1 = float(input("Digite a parte real do primeiro número complexo: ")
imaginario1 = float(input("Digite a parte imaginária do primeiro número complexo: "))

#Solicita partes real e imaginatoria do segundo complexo ao usuario.
real2 = float(input("Digite a parte real do segundo número complexo: ")
imaginario2 = float(input("Digite a parte imaginária do segundo número complexo: "))

#Cria as representações dos números complexos como tuplas
num1 = (real1, imaginario1)
num2 = (real2, imaginario2)

#Realiza a soma
soma = somar_numeros_complexos(num1, num2)

#Exibe o resultado
print("A soma dos números complexos é:", soma)
'''

#Exercicio 12 - Crie um código completo e detalhado que retorne as duas raizes em uma equação de segundo grau 
#usando a formula de bascara.

#Definir uma função

def calcular_raizes(a, b ,c):
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
        raiz2 = complex(parte_real,-parte_imaginaria)
        return raiz1, raiz2
    
    #Entrada de dados pelo usuário
    print('Informe os valores para A, B e C')
    a=float(input())
    b=float(input())
    c=float(input())
    
    #Chamada da função que calcula as raízes
    x1,x2=calcular_raizes(a,b,c)
    #Saida de resultados
    print ('As Raízes são {} e {}'.format(x1,x2))

