import socket
import ssl

# SET VARIABLES
packet, reply = "Here's my message", ""
HOST, PORT = '127.0.0.1', 9999

# CREATE SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

# WRAP SOCKET
wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")

# CONNECT AND PRINT REPLY
wrappedSocket.connect((HOST, PORT))
wrappedSocket.send(packet)
print ( wrappedSocket.recv(1280) )

# CLOSE SOCKET CONNECTION
wrappedSocket.close()
