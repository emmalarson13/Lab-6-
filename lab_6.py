# Emma Larson

def encoder(data):
    password=''
    for i in data:
        if int(i)==0:
            password+='3'
        if int(i) == 1:
            password+='4'
        if int(i) == 2:
            password+='5'
        if int(i) == 3:
            password+='6'
        if int(i) == 4:
            password+='7'
        if int(i) == 5:
            password+='8'
        if int(i) == 6:
            password+='9'
        if int(i) == 7:
            password+='0'
        if int(i) == 8:
            password+='1'
        if int(i) == 9:
            password+='2'
    return password

def decode(password):
    decoded = ''
    for i in password:
        if int(i) >= 3:
            decoded += str(int(i) - 3)
        else:
            decoded += str(int(i) + 7)
    return decoded


if __name__=='__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option= int(input('Please enter an option: '))
        if option==1:
            temp= encoder((input('Please enter your password to encode: ')))
            print('Your password has been encoded and stored!\n')
        if option == 2:
            print(f"The encoded password is {temp}, and the original password is {decode(temp)}.\n")

        if option==3:
            break


