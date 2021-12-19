from urllib.request import Request, urlopen

siteRequest = Request('http://www.pudim.com.br/')
try:
    resposta = urlopen(siteRequest)
except Exception as e:
    print(f'Site não disponivel', e)
else:
    print('Site disponivel!')