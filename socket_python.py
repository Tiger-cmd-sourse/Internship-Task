import socket
HOST = '127.0.0.1'
PORT = 7777


# Create a TCP socket
tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# af_inet is the ipv4 and sock_stream is the port

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect((HOST, PORT))



