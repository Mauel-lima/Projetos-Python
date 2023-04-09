import telebot
from time import sleep
import random
import string

#Acesso ao BOT
bot = telebot.TeleBot("6073931311:AAGDwQCUmm9hwyNGOUIksq3A9EJZWonheWM")
# responde ao comando /start

#Variáveis
resp1 = '18'
resp2 = 'brasilia'
resp3 = 'arco iris'
resp4 = 'ddd'
resp5 = 'swift'
x = 0
codigo = 0

#Tratando áudio e vídeo
@bot.message_handler(content_types=['photo', 'audio','voice'])
def aud_foto(message):
    if message.content_type == 'photo':
        # Lida com mensagem de imagem
        bot.reply_to(message, "Não queria um nude, por favor responda de maneira correta!")
    elif message.content_type in ['voice','audio']:
        # Lida com mensagem de áudio
        bot.reply_to(message, "Não pedi um podcast, por favor responda de maneira correta!")

#Mesagem de ínicio
@bot.message_handler(commands=['start'])
def inicio(message):
    bot.reply_to(message, "Olá! Seja bem vindo a 2° parte do enigma. Sou o Emanuel , o criador desse enigma, estou aqui para te ensinar como prosseguir")
    sleep(3)
    bot.send_message(message.chat.id,"1 -  Caso a pergunta seja pessoal, as respostas estarão nos meus perfis como tik tok o instagram.")
    sleep(3)
    bot.send_message(message.chat.id,"2 - Responda tudo em letras minisuculas e sem caracteres especiais.")
    sleep(3)
    bot.send_message(message.chat.id,"3 - Algumas respostas serão compostas exemplo 'ana banana'.")
    sleep(3)
    bot.send_message(message.chat.id,"4 - Para recomeçar tudo digite '/start'")
    sleep(3)
    bot.send_message(message.chat.id,"5 - Divirta-se")
    sleep(3)
    bot.send_message(message.chat.id,"Para comecar digite 'comecar enigma'")
    
#Funções
def gerar_codigo():
    letras_numeros = string.ascii_letters + string.digits
    codigo = ''.join(random.choices(letras_numeros, k=30))
    return codigo
def comecar(message):
    bot.reply_to(message, f"Muito bem! Vamos começar")
    sleep(3)
    bot.send_message(message.chat.id,"No programa eu facilitei, mas aqui vai ser díficil!")
    sleep(3)
    bot.send_message(message.chat.id,"Qual é a idade do criador desse enigma? ")
def perg2(message):
    bot.reply_to(message, f"Muito bem! Resposta correta, vamos para a próxima")
    sleep(3)
    bot.send_message(message.chat.id,  'Brincadeiras a parte, foi dificil planejar todas essas etapas e para ter meus 5 reais tem que fazer por merecer')
    sleep(3)
    bot.send_message(message.chat.id, 'Nessa os mais velhos vão ter vantagem.')
    sleep(3)
    bot.send_message(message.chat.id,'Responda a seguinte pergunta 77-88-2-555-33-2-222-2-7-444-8-2-555-3-666-22-777-2-7777-444-555 ?')
def perg3(message):
    bot.reply_to(message, f"Uau, um gênio?! Vamos para a próxima!")
    sleep(3)
    bot.send_message(message.chat.id,"Tem 7 letras, ou seja, 7 palavras, juntas o 'vlavaav' forma o ? ")
def perg4(message):
    bot.reply_to(message, f"Impressionado que tenha conseguido responder!")
    sleep(3)
    bot.send_message(message.chat.id,"A próxima será mais dificil! ")
    sleep(3)
    bot.send_message(message.chat.id,"Complete as letras que faltam na seguinte sequência jfmamjjason_udtqcsson_stqqss_?")
def perg5(message):
    bot.reply_to(message, f"Certo! Vamos à última pergunta!")
    sleep(3)
    bot.send_message(message.chat.id,"not yph")
    sleep(1)
    bot.send_message(message.chat.id,"varja pisct")
    sleep(1)
    bot.send_message(message.chat.id,"hpp")
    sleep(1)
    bot.send_message(message.chat.id,"wifst")
    sleep(1)
    bot.send_message(message.chat.id,"og")
    sleep(1)
    bot.send_message(message.chat.id,"Dica: ama grana")
    sleep(1)
    bot.send_message(message.chat.id,"O que significa wifst na sequência acima?")

#Tratar as mensagens
@bot.message_handler(func=lambda message: "" in message.text.lower())
def mensagens(message):
    global x
    sender = message.chat.first_name
    print(sender, 'Respondeu ', message.text.lower())
    if message.text.lower() ==  'comecar enigma':
        comecar(message)
    elif message.text.lower() == resp1:
        perg2(message)
    elif message.text.lower() == resp2:
        perg3(message)
    elif message.text.lower() == resp3:
        perg4(message)
    elif message.text.lower() == resp4:
        perg5(message)
    elif message.text.lower() == resp5:
        bot.send_message(message.chat.id,"Parabéns")
        with open('/gif/win.gif', 'rb') as gif:
            bot.send_document(message.chat.id, gif)
        if x == 0 and message.chat.id != 1924955712:
            bot.reply_to(message, f"Tire um print da última resposta mostrando o gif, e envie para o Whatsapp 61984161365 junto com o seu nome e o código abaixo")
            sleep(3)
            codigo = gerar_codigo()
            bot.send_message(message.chat.id, codigo)
            bot.send_message(message.chat.id,"Muito obrigado por participar!")
            bot.send_message(1755856821,f'{sender} Ganhou o desafio  seu código é {codigo}')
            x = 1
        elif message.chat.id == 1924955712:
            bot.reply_to(message, f"Você não pode mais ganhar :(")
        else:
            bot.reply_to(message, f"Infelizmente, você não foi o primeiro!")
            bot.send_message(message.chat.id,"Muito obrigado por participar!")
            sleep(3)
    else:
        bot.send_message(message.chat.id,"Inválido! Tente novamente!")

# inicia o bot
bot.polling()

