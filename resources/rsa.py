import math
import string 


main=string.ascii_lowercase

def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True

def co_prime_check(e,p,q):
    phi=(p-1)*(q-1)
    g=math.gcd(e,phi)
    if g==1:
        return True
    else:
        return False


def multiplicative_inverse(a, m):
    a=a%m; 
    for x in range(1,m) : 
        if((a*x)%m==1) : 
            return x 
    return 1

def generate_keypair(p, q ,e):
    n=p*q
    phi = (p-1)*(q-1)

    d = multiplicative_inverse(e, phi)
    return (e,n),(d,n)

def encrypt_helper(public_key, to_encrypt):
    key, n = public_key

    cipher=pow(to_encrypt,key)%n
    return cipher


def decrypt_helper(private_key, to_decrypt):
    key, n = private_key

    decrypted=pow(to_decrypt,key)%n
    return decrypted


def Encrypt(p,q,e,message):
    public, private = generate_keypair(p, q, e)
    message=message.replace(" ","")
    message=message.lower()
    arr=[]
    cipher_text=[]
    for i in message:
        if i in main:
            arr.append(main.index(i))
    for i in arr:
        cipher_text.append(encrypt_helper(public,i))

    return cipher_text

def Decrypt(p,q,e,cipher_text):

    cipher_text = cipher_text.replace(",","")
    cipher_text = cipher_text.replace("[","")
    cipher_text = cipher_text.replace("]","")
    cipher_text = cipher_text.split(" ")
    cipher_text = [int(i) for i in cipher_text]

    public, private = generate_keypair(p, q, e)
    plain=[]
    for i in cipher_text:
        plain.append(decrypt_helper(private,i))
    plain_text=''
    for i in plain:
        plain_text=plain_text+main[i]
    return plain_text
