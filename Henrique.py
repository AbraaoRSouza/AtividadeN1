from random import randint
x=1
sala=1
while(sala<=8 and x<=7):
    print("Você esta na sala: ", sala)
    caminho=int(input("Escolha seu caminho:\n[1] Caminho vermelho\n[2] Caminho preto\n"))
    if (sala==6 and caminho==1):
        print("O caminho vermelho está fechado então você só pode passar pelo preto!\n")
        sala=sala+1
    elif (sala==8 and caminho==2):
        sala=1
        print("Você entrou em um portal misterioso que te levou para o inicio da dungeon\n")
        sala = randint(1,5)
    sala=sala+caminho
    x=x+1
