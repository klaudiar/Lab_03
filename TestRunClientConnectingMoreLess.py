from ClientMoreLess import *


class TestRunClientConnectingMoreLess:
    # This test is connected with TestClientConnectingMoreLess, firstly run TestClientConnectingMoreLess
    # and then TestRunClientConnectingMoreLess in another terminal
    def __init__(self):
        message = '500'
        ClientMoreLess(message)

if __name__ == "__main__":
    TestRunClientConnectingMoreLess()