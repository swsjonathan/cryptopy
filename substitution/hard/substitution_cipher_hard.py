import secrets
import random
import string
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    method_group = parser.add_mutually_exclusive_group()
    input_group = parser.add_mutually_exclusive_group()
    method_group.add_argument("-e", "--encrypt", help = "Encrpyt plain text", action="store_true")
    method_group.add_argument("-d", "--decrypt", help ="Decrypt cipher text", action="store_true")
    parser.add_argument("-k", "--keyfile", help="Provide the key to be used in decryption")
    input_group.add_argument("-i", "--input", help="Provide the file you want to encrypt/decrypt")
    input_group.add_argument("-t", "--text", help="Add the text you want to encrypt/decrypt")
    parser.add_argument("-o", "--output", help="Provide the file you want to output the results to")
    
    args = parser.parse_args()
    
   #add output/input file name
   #create folders to store keys, cipher,plain text
    if args.encrypt:
        key = generate_key()
        rnd_key = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

        if args.input:
            with open(args.input) as f:
                plain_text = f.read()

        else:
            plain_text = args.text
        
        #store key in a file 
        with open('keys/' + rnd_key + '.json', 'w') as f:
            json.dump(key,f)

        cipher_text = encryptor(plain_text, key)

        if args.output:
            with open('cipher/'+ args.output, 'w') as f:
                f.write(cipher_text)
        else:
            print(cipher_text)
        print(f'Key File Name: {rnd_key}.json')

    elif args.decrypt:
        if args.input:
            with open(args.input) as f:
                cipher_text = f.read()
            
        else:
            cipher_text = args.text
        #read key from a file 
        with open(args.key) as f:
            key = json.load(f)

        plain_text = decryptor(cipher_text,key)

        if args.output:
            with open('plain/'+ args.output, 'w') as f:
                f.write(plain_text)
        else:
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
        

#decrypt cipher text using stored key
def decryptor(cipher_text, key):
    plain_text = []
    for i in cipher_text:
        if i in key.values():
            plain_text.append(list(key.keys())[list(key.values()).index(i)])
    return ''.join(plain_text)

if __name__ == "__main__":    
    main()
