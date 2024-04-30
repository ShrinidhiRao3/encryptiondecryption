def encrypt(text):
    encrypted_text=""
    for char in text:
        if char.isupper():
            encrypted_text+=chr(((ord(char)-ord('A')+2)%26)+ord('A'))
        elif char.islower():
            encrypted_text+=chr(((ord(char)-ord('a')+2)%26)+ord('a'))
        else:
            encrypted_text+=char

    return encrypted_text

def decrypt(text):
    decrypted_text=""
    for char in text:
        if char.isupper():
            decrypted_text +=chr(((ord(char)-ord('A')-2)%26)+ord('A'))
        elif char.islower():
            decrypted_text +=chr(((ord(char)-ord('a')-2)%26)+ord('a'))
        else:
            decrypted_text +=char

    return decrypted_text

def main():
    choice=input("Enter E for encryption and D for decryption:")
    if choice =='E':
        text=input("Enter text to encrypt:")
        encrypted_text=encrypt(text)
        print("Encrypted text:",encrypted_text)
    
    elif choice =='D':
        dtext=input("Enter text to decrypt:")
        decrypted_text=decrypt(dtext)
        print("Decrypted text:",decrypted_text)

    else:
        print("Invalid choice")
        

if __name__ =="__main__":
    main()
