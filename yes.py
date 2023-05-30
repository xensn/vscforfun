# Key = Assign
# Plain Text = Secretiscode

# A s s i g n
# - - - - - -
# 1 4 5 3 2 6
# - - - - - -
# S e c r e t
# - - - - - -
# i s c o d e

# Cipher text = SI ED  RO ES CC TE
            #   06 110 
#plaintext = input("Please enter the Plaintext: ")
#key = input("Please enter the key: ")

plaintext = "Secretiscode"
key = "Assign"

x = {}
column = ''


def trans(plaintext,key,column):
    plaintext.lower()
    key = key.upper()
    new_key_list = list(key)
    key_list = []
    
    # Check for repeats
    for i in new_key_list:
        if i not in key_list:
            key_list.append(i)
        else:
            continue

    
    print(key_list)
    print(new_key_list)
    
    for i in range(len(key_list)):
        if new_key_list[i] != key_list[i]:
            value = ord(new_key_list[i])
            letter = chr(value+1)
            key_list.append(letter)
            break
        else:
            continue
    
    key_list.sort()
    print(key_list)
    count = 0
    
    # Add into dictionary
    
    for i in key_list:
        print(i)
        for j in range(0,len(plaintext),len(key)):
            column += plaintext[j+count]  
            print(column)
            
        
        x[i] = column
        print(x)
        column = ''
        count += 1
    answer = ''
    for i in key_list:
        answer += x[i] + ' '

    print(answer.upper())
trans(plaintext,key,column)
