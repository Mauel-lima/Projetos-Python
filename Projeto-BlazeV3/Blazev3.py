#importações
import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
import sys
import os
import json


#Importando dados sensíveis
with open('dados.json', 'r') as f:
    dados = json.load(f)
    
#Função para resetar o programa em caso de erro
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Telegram entrar
id_grupo = dados['id_grupo']
api_id = dados['api_id']
api_hash = dados['api_hash']
token = dados['token']
phone = dados['phone']   
client = TelegramClient('session', api_id, api_hash)   
client.connect()  
if not client.is_user_authorized():   
    client.send_code_request(phone)     
    client.sign_in(phone, input('Enter the code: ')) 
client.send_message(id_grupo,f'Recomeçando') 

#Criar as opções do navegador
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


#Entrar no chrome
navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get("https://historicosblaze.com/blaze/doubles")

#Variaveis
tendencia = 0
e = ' '*100
x=2
perg1=0
apostab = 2
aposta = 4
lucrof = 0
win = 0
win1 = 0
perd = 0
winb = 0
quantidade = '//*[@id="valueBet"]'
vermelho = '//*[@id="btn-check-red"]'
branco = '//*[@id="btn-check-white"]'
preto = '//*[@id="btn-check-black"]'
valorTot = '//*[@id="wallet"]'
url = "https://historicosblaze.com/blaze"

#Inicio do Código Abrindo a url
page_source = navegador.page_source
conteudo = BeautifulSoup(page_source, 'html.parser')

#Prcurando o item através do Soup
filtro_cores = conteudo.find_all("div", class_=re.compile('double-single double-single-exporter border'))
print(conteudo)

#Filtrando Cores
respostas1 = filtro_cores[0]
respostas2 = filtro_cores[1]
respostas3 = filtro_cores[2]
respostas4 = filtro_cores[3]
respostas5 = filtro_cores[4]
respostas6 = filtro_cores[5]
respostas7 = filtro_cores[6]

#Indetificador único da número que caiu
seed = respostas1.find("span", class_=re.compile("seed-table")).get_text().strip()

#Função caso seja prejuizo para a Blaze
def preju():
    print("Blaze saiu no Prejuizo")
    print("Pagou: ", pago)
    print("Total: ", total)
    print("Lucrou ", lucro )
    print(f'Saiu a cor: {cor}\n Seu número é: {numero}\n Minuto: {horario}\n Lucro Final: {lucrof}')
    print(f'='*30)
    print(f'\n'*3)

#Função caso seja lucro para a Blaze
def lucrou():
    print("Blaze saiu no Lucro")
    print("Pagou: ", pago)
    print("Total: ", total)
    print("Lucrou ", lucro )
    print(f'Saiu a cor: {cor}\n Seu número é: {numero}\n Minuto: {horario}\n')
    print(f'='*30)
    print(f'\n'*3)

#Entrando em um loop
while True:
    
    #Resetando variáveis
    passou = 0
    cor1 = ""

    #Indetificar que o mesmo resultado não vai se repetir
    seed1 = seed

    #Buscando os itens que queremos dentro do código html
    cor = respostas1.find("span", class_=re.compile("color-table")).get_text().strip()
    cor2 = respostas2.find("span", class_=re.compile("color-table")).get_text().strip()
    cor3 = respostas3.find("span", class_=re.compile("color-table")).get_text().strip()
    cor4 = respostas4.find("span", class_=re.compile("color-table")).get_text().strip()
    cor5 = respostas5.find("span", class_=re.compile("color-table")).get_text().strip()
    cor6 = respostas6.find("span", class_=re.compile("color-table")).get_text().strip()
    cor7 = respostas7.find("span", class_=re.compile("color-table")).get_text().strip()
    numero1 = respostas2.find("span", class_=re.compile("number-table")).get_text().strip()
    numero = respostas1.find("span", class_=re.compile("number-table")).get_text().strip()
    horario = respostas1.find("span", class_=re.compile("minute-table")).get_text().strip()
    data = respostas1.find("span", class_=re.compile("date-table")).get_text().strip()
    vermelho = respostas1.find("span", class_=re.compile("redbets-table")).get_text().strip()

    #Formatando de maneira correta
    vermelho = re.sub('[R,$,.]','',vermelho)
    branco = respostas1.find("span", class_=re.compile("whitebets-table")).get_text().strip()
    branco = re.sub('[R,$,.]','',branco)
    preto = respostas1.find("span", class_=re.compile("blackbets-table")).get_text().strip()
    preto = re.sub('[R,$,.]','',preto)
    
    #Transformando em números para fazer os calcúlos
    vermelho = int(vermelho)
    branco = int(branco)
    preto = int(preto)
    
    #Condições para definir se saiu no lucro ou no prejuizo em cada cor
    if cor == "Black":
        pago = (preto*2)
        soma = (branco+vermelho)
        total = (soma+preto)
        lucro = total - pago
        if pago < soma:
            lucrou()
        else:
            preju()
    elif cor == "Red":
        pago = (vermelho*2)
        soma = (branco+preto)
        total = (soma+vermelho)
        lucro = total - pago 
        if pago < soma:
            lucrou()
        else:
            preju()
    elif cor == "White":
        pago = (branco*14)
        soma = (vermelho+preto)
        total = (soma+branco)
        lucro = total - pago
        if pago < soma:
            lucrou()
        else:
            preju()
    else:
        print("Pequeno erro:")
        time.sleep(2)
    if perg1 == 1:
        x=x*2
        aposta = aposta*2+x
    else:
        x=2
        aposta = 4
    if aposta >=16:
        apostab = apostab*2
    else:
        apostab=2
    
    #Estratégias
    numero= int(numero)
    if cor == cor2 and cor2 == cor3:
        print("Tendencia")
        tendencia = 1
    elif cor == "White":
        tendencia=1
    else:
        tendencia = 0

        #Confirmando entrada e enviando pelo telegram
        if numero == 1 or numero == 4 or numero == 5 or numero == 7 or numero == 9 or numero == 10 or numero == 13:
            cor1 = "Red"
            seed1 = seed
            cor1_emoji = '🔴'
            print("Entrar na ", cor1, " protegendo no White")
            client.send_message(id_grupo, f'✅ ENTRADA CONFIRMADA{e}👻 ENTRAR= {cor1_emoji}+⚪️{e} 🧐 Após o número ({numero}){e}🧠Bata a meta e vaza')
            time.sleep(2)

            #Entrando em loop até rodar o próximo número
            while seed == seed1:
                page_source = navegador.page_source
                while True:
                    try:
                        soup = BeautifulSoup(page_source, 'html.parser')
                        filtro_cores = soup.find_all("div", class_=re.compile('double-single double-single-exporter border'))
                        respostas1 = filtro_cores[0]
                        break
                    except:
                        restart_program()
                seed = respostas1.find("span", class_=re.compile("seed-table")).get_text().strip()
                cor = respostas1.find("span", class_=re.compile("color-table")).get_text().strip()
                passou = 1

        #Estratégia alternativa
        elif numero == 2 or numero == 3 or numero == 6 or numero == 8 or numero == 11 or numero == 12 or numero == 14:
            cor1 = "Black"
            seed1 = seed
            cor1_emoji = '⚫'
            print("Entrar na ", cor1, " protegendo no White")
            client.send_message(id_grupo, f'✅ ENTRADA CONFIRMADA{e}👻 ENTRAR= {cor1_emoji}+⚪️{e} 🧐 Após o número ({numero}){e}🧠Bata a meta e vaza')
            time.sleep(2)

            #Entrando em loop até rodar o próximo número
            while seed == seed1:
                page_source = navegador.page_source
                while True:
                    try:
                        soup = BeautifulSoup(page_source, 'html.parser')
                        filtro_cores = soup.find_all("div", class_=re.compile('double-single double-single-exporter border'))
                        respostas1 = filtro_cores[0]
                        break
                    except:
                        restart_program()
                seed = respostas1.find("span", class_=re.compile("seed-table")).get_text().strip()
                cor = respostas1.find("span", class_=re.compile("color-table")).get_text().strip()
                passou = 1
        else:
            print("FUI")
            pass

    #Confirmando se ganhou ou não
    if cor == cor1:
        win = win+1
        print("Win")
        client.send_message(id_grupo, f'Win')
        perg1=0
    elif cor == "White" and passou == 1:
        winb +=1
        print("Win Branco")
        client.send_message(id_grupo, f'Win Branco')
        perg1=0

    #Entrada em martingale 1
    elif cor1 != "" and cor != cor1 and cor != "White":
        print("G1")
        seed1 = seed
        print("Martingale na ", cor1, " protegendo no White")
        client.send_message(id_grupo, f'Martingale 1 = {cor1_emoji}+⚪️. 😳😳')

        #Entrando em loop até rodar o próximo número
        while seed == seed1:
            page_source = navegador.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            filtro_cores = soup.find_all("div", class_=re.compile('double-single double-single-exporter border'))
            respostas1 = filtro_cores[0]
            seed = respostas1.find("span", class_=re.compile("seed-table")).get_text().strip()
            cor = respostas1.find("span", class_=re.compile("color-table")).get_text().strip()

        #Confirmando se ganhou ou não
        if cor == cor1:
            win = win+1
            print("Win")
            client.send_message(id_grupo, f'Win')
            perg1=0
        elif cor == "White" and passou == 1:
            winb +=1
            print("Win Branco")
            client.send_message(id_grupo, f'Win Branco')
            perg1=0
        elif cor1 != "" and cor != cor1 and cor != "White":
            print("Perdemo")
            client.send_message(id_grupo, f'Perdemo')
            perg1 = 1
            perd +=1
        else:
            pass
    else:
        pass

    #Definindo porcentagem de acertos
    if win != 0 and perd == 0:
        porc = 100
    elif win != 0 and perd != 0:
        porc = ((win+winb)*100)/(win+winb+perd)
        porc = round(porc, 2)
    else:
        porc=0
    print(f'Ganhamos: {win} \nBrancos: {winb}\nPerdemos: {perd} \nPorcentagem: {porc}%')
    if tendencia != 1:
        client.send_message(id_grupo,f'✅{win}{e}⛔️{perd} {e}⚪️{winb}{e}🎯Acertamos: {porc}%')
    else:
        pass
    if perg1 >=1:
        print("Dando um tempo")
        time.sleep(5)
    else:
        pass

    #Entrando em loop até rodar outro número
    while seed == seed1:
        page_source = navegador.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        respostas = soup.find_all("div", class_=re.compile('double-single double-single-exporter border'))
        respostas1 = respostas[0]
        seed = respostas1.find("span", class_=re.compile("seed-table")).get_text().strip()
        cor = respostas1.find("span", class_=re.compile("color-table")).get_text().strip()
   
#Disconectar do Telegram
client.disconnect()
