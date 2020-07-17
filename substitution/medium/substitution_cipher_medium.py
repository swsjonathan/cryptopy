import secrets
import string
import json

def main():    
    plain_text = 'Super Mario'
    key = generate_key()  
    #store key in a file 
    with open('key.json', 'w') as f:
        json.dump(key,f)

    cipher_text = encryptor(plain_text, key)
    with open('cipher_text.txt', 'w') as f:
        f.write(cipher_text)
  
    #store key in a file 
    decryptor(cipher_text,key)

#generate cipher key
def generate_key():
    key = dict()
    characters = string.ascii_lowercase + string.digits + string.punctuation + string. whitespace
    characters_list = list(characters)

    for i in characters:
        value = secrets.choice(characters_list)
        key[i] = value
        characters_list.remove(value)
    return key
       
#encypt plaintext using generated key
def encryptor(plain_text, key):
    cipher_text = []
    for i in plain_text.lower():        
        if i in key.keys():
            cipher_text.append(key.get(i))
    return ''.join(cipher_text)
        

# #decrypt cipher text using stored key
def decryptor(cipher_text, key):
    plain_text = []
    for i in cipher_text:
        if i in key.values():
            plain_text.append(list(key.keys())[list(key.values()).index(i)])
    print(''.join(plain_text))

if __name__ == "__main__":
    main()
