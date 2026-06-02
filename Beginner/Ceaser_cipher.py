alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    cipher = [""]

    def encrypt(plain_text , forward):
        for val in range(0,len(plain_text)):
            if plain_text[val] not in alphabet:
                cipher.append((plain_text[val]))
            else:
                a = alphabet.index(plain_text[val])
                b = a+forward
                if b > 25:
                    b = b%26
                cipher.append(alphabet[b])
        print("".join(cipher))

    def decrypt(cipher_text , backward):
        for val in range(0,len(cipher_text)):
            if cipher_text[val] not in alphabet:
                cipher.append(cipher_text[val])
            else:
                a = alphabet.index(cipher_text[val])
                b = a-backward
                if b > 0:
                    b-=26
                cipher.append(alphabet[b])
        print("".join(cipher))
        
    
    if direction == "encode":
        encrypt(text,shift)
    if direction == "decode":
        decrypt(text,shift)
    Again = input('You want to try again?? "yes" to again "no" to stop\n').lower()
    if Again == "yes":
        start()
    else:
        pass

start()

