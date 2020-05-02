import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim.com.br não está acessível no momento.')
else:
    print('Consegui acessar o site pudim.com.br.')
    print(site.read())