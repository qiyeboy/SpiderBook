import socket
import struct
import json
import socket
import logging
import signal
import os
import time
from multiprocessing import Process, Queue

keys_word_json = b''
def handle(client_socket, client_address):
    global keys_word_json
    try:
        client_socket.sendall(bytes(keys_word_json, encoding = "utf-8"))
    finally:
        client_socket.close()


def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return
    return 
            
def target_server(**kwargs):
    print("target_server start")
    global keys_word_json
    keys_word_json = json.dumps(kwargs)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = ("0.0.0.0", 2007)
    try:
        server.bind(server_host)
        server.listen(50)
    except Exception as e:
        logging.error("bind listen error")
        logging.info("error message：{}".format(e))

    #signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        connection, client_address = server.accept()
        logging.info("connection:{} client_address:{}".format(connection, client_address))
        #print "connection", connection
        print( "%s connect. " %str(client_address) )
        handle(connection, client_address)
        logging.info("child connection field id:{}".format(connection))
        connection.close()

if __name__ == '__main__':
    keywords = {'url_fiter_keys':["dxy"]}
    server_proc = Process(target=target_server, kwargs=keywords)
    server_proc.start()


