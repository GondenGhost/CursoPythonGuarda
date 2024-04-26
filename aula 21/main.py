class Personagem:
    def __init__(self, nome, vida, ataques):
        self.nome = nome
        self.vida = vida
        self.ataques = ataques

    def atacar(self, outro_personagem, ataque_escolhido):
        dano = self.ataques[ataque_escolhido]
        outro_personagem.vida -= dano
        print(f'{self.nome} usou {ataque_escolhido} em {outro_personagem.nome}! {outro_personagem.nome} agora tem {outro_personagem.vida} pontos de vida.')

personagens = [
    Personagem('Guerreiro', 100, {'Espadada': 20, 'Golpe Duplo': 30}),
    Personagem('Arqueiro', 80, {'Flechada': 15, 'Flechada Tripla': 35}),
    Personagem('Mago', 60, {'Bola de Fogo': 25, 'Raio': 40})
]

print("Escolha ""seu personagem:")
for i, personagem in enumerate(personagens):
    print(f'{i + 1}. {personagem.nome}')

escolha = int(input("Digite o número do seu personagem: ")) - 1
personagem_jogador = personagens[escolha]

personagem_inimigo = personagens[(escolha + 1) % len(personagens)]

while personagem_jogador.vida > 0 and personagem_inimigo.vida > 0:
    print("Escolha seu ataque:")
    for i, ataque in enumerate(personagem_jogador.ataques):
        print(f'{i + 1}. {ataque}')

    ataque_escolhido = list(personagem_jogador.ataques.keys())[int(input("Digite o número do seu ataque: ")) - 1]
    personagem_jogador.atacar(personagem_inimigo, ataque_escolhido)
    if personagem_inimigo.vida <= 0:
        break

    ataque_inimigo = list(personagem_inimigo.ataques.keys())[0]
    personagem_inimigo.atacar(personagem_jogador, ataque_inimigo)

if personagem_jogador.vida > 0:
    print(f'{personagem_jogador.nome} venceu a batalha!')
else:
    print(f'{personagem_inimigo.nome} venceu a batalha!')



