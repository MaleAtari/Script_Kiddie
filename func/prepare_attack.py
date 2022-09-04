from itertools import product

import requests

def prepare_payload(payload):
    for x in payload:
        for k, i in x.items():
            if i == None:
                print('*' * 50)
                print('Podaj tekst lub pozostaw pole puste, wtedy zostanie uzyte do ataku')
                i = input(f'{k} : ')
                x[k] = i
    print('*' * 50)
    return payload
            
def final_payload(payload, word):
    new = {}
    for x in payload:
        for k, i in x.items():
            if i == '':
                new[k] = str(word)
            else:
                new[k] = i
                
    return new





####### Create Brute Force ###############



def final_combo(combo_list, text):
    fcombo = []
    for c in combo_list:
        fcombo.append(str(text) + ''.join(c))
    return fcombo

def unpack_dict(dictionary):
    for i in dictionary.keys():
        for k in dictionary.values():
            return (i, k)
        

class BruteForce:
    def __init__(self, char_length, chars, static_text):
        self.char_length = char_length
        self.chars = chars
        self.static_text = static_text
        self.combos = final_combo(list(product(self.chars, repeat=self.char_length)), self.static_text)
        self.length = len(self.combos)
        
        

