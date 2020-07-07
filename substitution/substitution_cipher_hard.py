import secrets
import string
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", help = "Encrpyt plain text", action="store_true")
    group.add_argument("-d", "--decrypt", help ="Decrypt cipher text", action="store_true")
    parser.add_argument("-t", "--text", help="Add the text you want to encrypt")
    args = parser.parse_args()
    
   #add output/input file name
   #create folders to store keys, cipher,plain text
    if args.encrypt:
        key = generate_key()  
        plain_text = args.text
        
        #store key in a file 
        with open('key.json', 'w') as f:
            json.dump(key,f)

        cipher_text = encryptor(plain_text, key)
        with open('cipher_text.txt', 'w') as f:
            f.write(cipher_text)



    elif args.decrypt:
        cipher_text = args.text
        #read key from a file 
        with open('key.json') as f:
            key = json.load(f)

        with open('cipher_text.txt') as f:
            cipher_text = f.read()
        plain_text = decryptor(cipher_text,key)
        print(plain_text)
   
   
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
    return ''.join(plain_text)

if __name__ == "__main__":    
    main()
