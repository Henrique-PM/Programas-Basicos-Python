#Calculadora
while 1 == 1:
  print('=' * 40)
  print('              Calculadora        ')
  print('=' * 40)

  print('''[1] -> Soma
[2] -> Subtração
[3] -> Multiplicação
[4] -> Divisão
[5] -> Exponencial
[6] -> Resto
[7] -> Raiz (número para saber a raiz ,já o segundo é o índice/colocar 0.5,0.3,0.25  
[8] -> Sair             ''')
  print('=' * 40)

  num1 = float(input('Escolha um número: '))
  num2 = float(input('Escolha um outro ou mesmo número: '))
  calc = int(input('Escolha uma das opções acima: '))

  if calc == 1:
    soma = num1 + num2
    print('A soma do %f + %f = %f' % (num1, num2, soma))

  elif calc == 2:
    subs = num1 - num2
    print('A subtração do %f - %f = %f' % (num1, num2, subs))

  elif calc == 3:
    mult = num1 * num2
    print('A multiplicação do %f * %f = %f' % (num1, num2, mult))

  elif calc == 4:
    soma = num1 / num2
    print('A Divião do %f / %f = %f' % (num1, num2, soma))

  elif calc == 5:
    soma = num1**num2
    print('O exponencial do %f^%f = %f' % (num1, num2, soma))

  elif calc == 6:
    rest = num1 % num2
    print('O resto do %f / %f = %f' % (num1, num2, rest))

  elif calc == 7:
    raiz = pow(num1, num2)
    print('A raiz do %f por %f = %f' % (num1, num2, raiz))
  elif calc == 8:
    break
  else:
    print('Opção inválida')

print()
print()
print()
print()
print()
print()

#Pedra,papel e tesoura
import random

while 1 == 1:

  print('=' * 40)
  print('        Pedra,Papel e Tesoura      ')
  print('=' * 40)

  print('''[1] -> Pedra
[2] -> Papel
[3] -> Tesoura 
[4] -> Sair''')
  print('=' * 40)

  jj = int(input('Escolha uma das jogadas acima: '))

  if jj == 2:
    print('O jogador escolheu %d 🖐' % (jj))
  elif jj == 3:
    print('O jogador escolheu %d 🤞' % (jj))
  elif jj == 1:
    print('O jogador escolheu %d ✊ ' % (jj))
  elif jj == 4:
    break

  if jj == 1 or jj == 2 or jj == 3:
    print('Espere, É a vez do computador')
    print('=' * 40)

  jc = random.randint(1, 3)
  print('o computador escolheu o numero %d' % (jc))

  print()

  if jj == jc:
    print('A Jogada deu empate')
  elif jj == 1 and jc == 2:
    print('O computador VENCEU')
  elif jj == 1 and jc == 3:
    print('O jogador VENCEU')
  elif jj == 2 and jc == 1:
    print('O jogador VENCEU')
  elif jj == 2 and jc == 3:
    print('O computador VENCEU')
  elif jj == 3 and jc == 1:
    print('O computador VENCEU')
  elif jj == 3 and jc == 2:
    print('O jogador VENCEU')

  else:
    print('Jogada inválida')

print()
print()
print()
print()
print()
print()
#Adivinhação
import random

print('=' * 40)
print('         Jogo de Adivinhação      ')
print('=' * 40)

print('Vamos Jogar')
cp = random.randint(1, 1023)
print('Para sair digite o número zero/0')
while 1 == 1:
  jt = int(input('Tente adivinhar o número escolhido: '))
  if jt == 0:
    break
  if cp < jt:
    print(' O número secreto é menor')
  elif cp > jt:
    print('O número secreto é maior')
  elif cp == jt:
    print('PARABÉNS você acertou ')
    print(cp)
print('=' * 40)

print()
print()
print()
print()
print()
print()

#Forca
print('=' * 40)
print('                Forca     ')
print('=' * 40)
print('Para sair digite o valor 0') 
while 1==1:
    palavra = str(input('Digite a palavra misteriosa: ')).lower().strip()
    if palavra =="0":
        break 
    digit = []
    acert = []
    erro = 0
    while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acert else "."
        print(senha)
        if senha == palavra:
            print("🎉🎉🎉🎉  Você acertou  🎉🎉🎉🎉 ")
            break
         
        tent = input("Digite uma letra: ").lower().strip()
        if tent in digit:
            print("Você já tentou esta letra!")
            continue
        else:
            digit += tent
            if tent in palavra:
                acert += tent
            else:
                erro += 1
                print("Você errou!")   
        if erro == 6:
            print("Enforcado!")
            print('''=======
   |  
   O
  /|\ 
  /\ ''')
                       
            break
            print('='*5)  

    print() 
    print()      
    print('O jogador digitou {}'.format(digit))
    print('O jogador cometeu {} erros'.format(erro))         
   
