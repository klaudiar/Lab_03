from moreOrLess import *

class Server:
    my_choice = 0

    def __init__(self, address, port):
        self.server(address, port)

    def server(self, address, port):
        connection = runSocket(address, port)

        answer = 100
        while answer == 100:
            while True:
                try:
                    self.choice = float(connection.recv(1024))    # data size - 1024
                    break
                except ValueError:
                    text = 'You must write a number'
                    print(text)
                    connection.send(text)
            text, answer = yourChoice(self.choice)
            connection.send(text)

        my_choice, text = serverChoice()
        connection.send(text)
        if abs(self.choice - my_choice) <= 0.5:
            print("Client won")
            text = '!! WINNER !!'
        elif abs(self.choice - my_choice) > 0.5:
            print("Server won")
            text = 'LOOSER'

        connection.send(text)
        connection.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = Server(host, port)
