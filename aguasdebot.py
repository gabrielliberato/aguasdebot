import tweepy
import time
from keys import *
from random import randint

música = ["É pau, é pedra, é o fim do caminho",
          "É um resto de toco, é um pouco sozinho",
          "É um caco de vidro, é a vida, é o Sol",
          "É a noite, é a morte, é o laço, é o anzol",
          "É peroba do campo, é o nó da madeira",
          "Caingá, candeia, é o Matinta Pereira",
          "É madeira de vento, tombo da ribanceira",
          "É o mistério profundo, é o queira ou não queira",
          "É o vento ventando, é o fim da ladeira",
          "É a viga, é o vão, festa da cumeeira",
          "É a chuva chovendo, é conversa ribeira",
          "Das águas de março, é o fim da canseira",
          "É o pé, é o chão, é a marcha estradeira",
          "Passarinho na mão, pedra de atiradeira",
          "É uma ave no céu, é uma ave no chão",
          "É um regato, é uma fonte, é um pedaço de pão",
          "É o fundo do poço, é o fim do caminho",
          "No rosto, o desgosto, é um pouco sozinho",
          "É um estrepe, é um prego, é uma ponta, é um ponto",
          "É um pingo pingando, é uma conta, é um conto",
          "É um peixe, é um gesto, é uma prata brilhando",
          "É a luz da manhã, é o tijolo chegando",
          "É a lenha, é o dia, é o fim da picada",
          "É a garrafa de cana, o estilhaço na estrada",
          "É o projeto da casa, é o corpo na cama",
          "É o carro enguiçado, é a lama, é a lama",
          "É um passo, é uma ponte, é um sapo, é uma rã",
          "É um resto de mato, na luz da manhã",
          "São as águas de março fechando o verão",
          "É a promessa de vida no teu coração",
          "É uma cobra, é um pau, é João, é José",
          "É um espinho na mão, é um corte no pé",
          "São as águas de março fechando o verão",
          "É a promessa de vida no teu coração",
          "É pau, é pedra, é o fim do caminho",
          "É um resto de toco, é um pouco sozinho",
          "É um passo, é uma ponte, é um sapo, é uma rã",
          "É um belo horizonte, é uma febre terçã",
          "São as águas de março fechando o verão",
          "É a promessa de vida no teu coração",
          "Au, edra, im, minho",
          "Esto, oco, ouco, inho",
          "Aco, idro, ida, ol, oite, orte, aço, zol",
          "São as águas de março fechando o verão",
          "É a promessa de vida no teu coração"
          ]
versos = []
for verso in música:
    if verso not in versos:
        versos.append(verso)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def tuita():
    n = randint(1, len(versos) - 1)
    timeline = tweepy.Cursor(api.user_timeline).items()
    for i in timeline:
        if versos[n] == i.text:
            print(f"'{i.text}' já foi tuitado... apagando")
            api.destroy_status(i.id)
    api.update_status(versos[n])
    print(f"'{versos[n]}' tuitado")



while True:
    tuita()
    time.sleep(3600)
