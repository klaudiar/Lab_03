import unittest
import socket


class TestServerMoreLess(unittest.TestCase):
    # firstly run ServerMoreLess

    def testServerMoreLess(self):
        port = 50001
        host = 'localhost'
        server_address = (host, port)
        print('connecting to %s port %s' % server_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        message = '0.1'
        sock.sendto(message, server_address)
        response = sock.recv(1024)
        sock.recv(1024)
        sock.recv(1024)
        sock.close()
        assert response == 'You chose 0.1', "Not right response"

if __name__ == "__main__":
    unittest.main()