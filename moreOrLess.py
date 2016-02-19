import socket
from random import uniform


def yourChoice(choice):
    if choice >= -1 and choice <= 1:
        print('You chose %s' % choice)
        text = 'You chose %s' % choice

    else:
        text = 'You chose wrong number'
        print(text)
        choice = 100
    return text, choice

def menu():
    print('--> Lets play More or Less <--')
    print('_'*40)
    print('If difference between your number and mine will be less than 0.5 you\'ll win')
    print('Choose one number from -1 to 1: \n')

def runSocket(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (address, port)
    menu()
    print('bind to %s port %s' % server_address)
    sock.bind(server_address)
    sock.listen(1)
    connection, client_address = sock.accept()
    return connection


def serverChoice():
    my_choice = uniform(-1, 1)
    text = ('Server chose %f' % my_choice)
    print(text)
    return my_choice, text
