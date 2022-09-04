import sys
import requests
from bs4 import BeautifulSoup


def inspect_page(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print('Nie da sie polaczyc ze strona. Sprawdz adres strony')
            sys.exit()
    except:
        print('Podany adres nie istnieje')
        sys.exit()
        
    print('kod odpowiedzi:  ', response.status_code)
    
    # Try to find login panel and catch Form
    content = BeautifulSoup(response.content, 'html.parser')
    catched = []
    form = content.find('form', method=('post', 'POST'))
    if form == None:
        print('Nie moge znalezc panelu logowania')
        sys.exit()
    print(' ***** Znalazlem panel logowania ****')
    for i in form.find_all('input'):
        try:
            catched.append({i['name']: i['value']})
        except:
            catched.append({i['name']: None})
    print('Udalo sie przechwycic dane do panelu logowania')
    print('*' * 50)
   
    
    return catched


    
    
