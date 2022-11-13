import string

def key_generation(key):
    main=string.ascii_lowercase.replace('j','.')
    key=key.lower()
    
    key_matrix=['' for i in range(5)]
    i=0;j=0
    for c in key:
        if c in main:
            key_matrix[i]+=c
            main=main.replace(c,'.')
            j+=1
            if(j>4):
                i+=1
                j=0
    for c in main:
        if c!='.':
            key_matrix[i]+=c

            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)

def conversion_enc(key_matrix,plain_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.lower()

    i=0
    while i<len(plain_text):
        a=plain_text[i]
        b=''

        if((i+1)==len(plain_text)):
            b='x'
        else:
            b=plain_text[i+1]

        if(a!=b):
            plain_text_pairs.append(a+b)
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            i+=1

    for pair in plain_text_pairs:
        flag=False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                # find will return index of a letter in string
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue
                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
        cipher_text_pairs.append(cipher_text_pair)
        
    cipher = "".join(cipher_text_pairs)
    return cipher


def conversion_dec(key_matrix,cipher_text):
    
    plain_text_pairs=[]
    cipher_text_pairs=[]

   
    cipiher_text=cipher_text.lower()

    i=0
    while i<len(cipher_text):
        # i=0,1,2,3
        a=cipher_text[i]
        b=cipher_text[i+1]

        cipher_text_pairs.append(a+b)
        # else dont leave the next letter and put x
        # in place of repeated letter and conitnue with the next letter
        # which is repeated (according to algo)
        i+=2

    for pair in cipher_text_pairs:
        # RULE2: if the letters are in the same row, replace them with
        # letters to their immediate right respectively
        flag=False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                # find will return index of a letter in string
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                # same as reverse
                # instead of -1 we are doing +4 as it is modulo 5
                plain_text_pair=row[(j0+4)%5]+row[(j1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue

        # RULE3: if the letters are in the same column, replace them with
        # letters to their immediate below respectively
                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                # find will return index of a letter in string
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                # same as reverse
                # instead of -1 we are doing +4 as it is modulo 5
                plain_text_pair=col[(i0+4)%5]+col[(i1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue
        #RULE:4 if letters are not on the same row or column,
        # replace with the letters on the same row respectively but
        # at the other pair of corners of rectangle,
        # which is defined by the original pair

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        plain_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
        plain_text_pairs.append(plain_text_pair)
        
   
    res = "".join(plain_text_pairs)
    return res

def encrypt(key,plain_text):
    key_matrix=key_generation(key)
    return conversion_enc(key_matrix,plain_text)


def decrypt(key,cipher_text):
    key_matrix=key_generation(key)
    return conversion_dec(key_matrix,cipher_text)
