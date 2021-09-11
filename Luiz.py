import random
from random import randint
tentativas=1
sala=1
print("Guerreiros vocês estão na dungeon PYTHON onde só os melhores sobrevivem, fiquem atentos com as ameaças\nQue os jogos começem ")
while(sala<=8 and tentativas<=6):
    print("Você esta na sala: ", sala)
    caminho=int(input("Escolha seu caminho:\n[1] Caminho vermelho\n[2] Caminho preto\n"))
    while (caminho < 1 or caminho >2):
        print("CAMINHO INVALIDO")
        caminho=int(input("Escolha seu caminho:\n[1] Caminho vermelho\n[2] Caminho preto\n"))
    if (sala==6 and caminho==1):
        print("O caminho vermelho está fechado então você só pode passar pelo preto!\n")
        sala=sala+1
    elif (sala==8 and caminho==2):
        sala=1
        print("Você entrou em um portal misterioso que te levou para o inicio da dungeon\n")
        sala = randint(1,5)
    lista = ['Sala Black Mamba, sua mentalidade necessita ser de um vencedor, caso contrário será picado pela cobra mais venenosa do mundo',
        'Sala Husky, sua agilidade contará muito para avançar de fase, pois a sala está desabando e vocês não querem morrer esmagados ',
        'Sala Fallen, aqui a calma e a sutileza são fundamentais para não acordar o dragão ancião',
        'Sala Ace, o trabalho em equipe será essencial para desvendar a mensagem do enigma',
        'Sala Viper, tente não respirar a cortina tóxica altamente mortal',
        'Sala Azkaban, o prisioneiro mais perigoso de todos os reinos se encontra nessa sala, capture-o para avançar']
    print(random.choice(lista))
    sala=sala+caminho
    tentativas=tentativas+1
if sala==9:
    print("\nVocê saiu da dungeon, parabéns !!!")
elif tentativas >=7:
    print("\nVocê não tem mais tentativas !!!")
