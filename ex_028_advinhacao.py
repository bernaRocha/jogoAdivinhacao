#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

from time import sleep #faz o computador esperar por alguns segundos

computador = randint(0, 10) #faz o computador "pensar/escolher" um número
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? ")) #usuário tenta adivinhar
print("PROCESSANDO.....")
sleep(3)

if jogador == computador:
    print("Parábens! Você acertou")
else:
    print("Ganhei! Eu pensei no número {} e não no número {}".format(computador, jogador))



#print("Pensei no número {}".format(computador))
