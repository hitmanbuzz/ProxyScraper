import requests
import json

print('''
|--------------------------|
      By Hitman-2005
 Discord: H I T M A N#0001
|--------------------------|''')

print('\n')

print('"y" for yes and "n" for no!')
option1 = 'y'
option2 = 'n'

def http():
    option_result1 = input('HTTP Proxies y/n: ')
    if option_result1 == option1:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all')
        result = response.text
        with open('http_proxies.txt', 'w') as f:
            f.write(result)
            f.write('\n')
    else:
        print('Please rerun the program again')
http()

def socks4():
    option_result2 = input('Socks4 Proxies y/n: ')
    if option_result2 == option1:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all')
        result = response.text
        with open('socks4_proxies.txt', 'w') as f:
            f.write(result)
            f.write('\n')
    else:
        print('Please rerun the program again')
socks4()

def socks5():
    option_result3 = input('Socks5 Proxies y/n: ')
    if option_result3 == 'y':
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all')
        result = response.text
        with open('socks5_proxies.txt', 'w') as f:
            f.write(result)
            f.write('\n')
    else:
        print('Please rerun the program again')
socks5()
