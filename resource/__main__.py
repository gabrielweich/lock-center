import socket
import sys
import os
from xmlrpc.server import SimpleXMLRPCServer


def parse_args():
    if len(sys.argv) != 2:
        print("Usage: python3 -m resource <resource_port>")
        exit(1)

    res_port = sys.argv[1]
    return int(res_port)


RES_PORT = parse_args()
RES_HOST = '127.0.0.1'
RES_PATH = os.path.join('resource', 'resource.txt')


class Resource:
    @staticmethod
    def read():
        with open(RES_PATH, 'r') as f:
            lines = f.read().splitlines()
            print(lines)
            last_line = lines[-1]
            print(last_line)
            return int(last_line)

    @staticmethod
    def write(number):
        print(number)
        with open(RES_PATH, 'a') as f:
            f.write('\n' + str(number))

        return True


try:
    with SimpleXMLRPCServer((RES_HOST, RES_PORT)) as server:
        server.register_instance(Resource())
        print('resource listening in {} port {}'.format(RES_HOST, RES_PORT))
        server.serve_forever()
except KeyboardInterrupt:
    print("closed")
