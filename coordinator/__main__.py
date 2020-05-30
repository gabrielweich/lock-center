import sys
from xmlrpc.server import SimpleXMLRPCServer


def parse_args():
    if len(sys.argv) != 2:
        print("Usage: python3 -m coordinator <coordinator_port>")
        exit(1)

    coord_port = sys.argv[1]
    return int(coord_port)


SERVER_PORT = parse_args()
SERVER_HOST = '127.0.0.1'


class Coordinator:
    def __init__(self):
        self.resource_is_locked = False

    def lock(self):
        if self.resource_is_locked:
            return False
        else:
            self.resource_is_locked = True
            return True

    def unlock(self):
        self.resource_is_locked = False
        return True


try:
    with SimpleXMLRPCServer((SERVER_HOST, SERVER_PORT)) as server:
        server.register_instance(Coordinator())
        print('coordinator listening in {} port {}'.format(SERVER_HOST, SERVER_PORT))
        server.serve_forever()
except KeyboardInterrupt:
    print("closed")
