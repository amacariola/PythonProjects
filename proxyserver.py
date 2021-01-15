# Python3 Proxy server
# using socket libraries

from time import sleep
import socket
import signal
import threading

# initialize 
def __init__(self,config):
    signal.signal(signal.SIGINIT,self.shutdown)
    self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.serverSocket.setsockopt(socket.SOL_SOCKET,socket.SOCK_REUSEADDR,1)
    self.serverSocket.bind(config['HOST_NAME'],config['BIND_PORT'])
    self.serverSocket.listen(10)
    self.__clients = {}
    while True:
        (clientSocket,client_address) = self.serverSocket.accept()
        d = threading.Thread(name=self._getClientName(client_address))
        target = self.proxy_thread, args = (clientSocket, client_address)
        d.setDaemon(True)
        d.start
        request = conn.recv(config['MAX_REQUEST_LEN'])
        first_line = request.split('\n')[0]
        url = first_line.split('')[1]

        http_pos = url.find('://')
        if (http_pos == -1):
            temp = url
        else:
            temp = url[(http_pos + 3):]
        port_pos = temp.find(':')

        webserver_pos = temp.find('/')
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1
        if (port_pos == -1 or webserver_pos < port_pos):git
            webserver = temp[:webserver_pos]
        else:
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(config['CONNECTION_TIMEOUT'])
 s.connect((webserver,port))
        s.sendall(request)
        while 1:
            data = s.recv(config['MAX_REQUEST_LEN'])
            if (len(data) > 0):
                conn.send(data)
            else:
                break