import socket
import struct
import json
import socket
import logging
import signal

class ReadRemoteCfg:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.dict_msg = {}
        self._get_server_cfg()

    def _get_server_cfg(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        socke_buffer = []
        while True:
            szBuf = sock.recv(4096)
            if szBuf:
                socke_buffer.append(szBuf)
            else:
                break
        logging.info("socke_buffer:{}".format(socke_buffer))
        self.dict_msg =json.loads(b''.join(socke_buffer).decode('utf-8'))
        sock.close()

    def get_cfg(self):
        return self.dict_msg


if __name__ == "__main__":
    readRemoteCfg = ReadRemoteCfg("0.0.0.0", 2007)
    print(readRemoteCfg.get_cfg())