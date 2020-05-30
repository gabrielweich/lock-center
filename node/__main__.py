import xmlrpc.client
import sys
import time


def parse_args():
    if len(sys.argv) != 3:
        print("Usage: python3 -m node <coordinator_address> <resource_address>")
        exit(1)

    coord_host, res_host = sys.argv[1:]
    return coord_host, res_host


COORD_HOST, RES_HOST = parse_args()

ITERATIONS = 5


try:
    coordinator = xmlrpc.client.ServerProxy(COORD_HOST)
    resource = xmlrpc.client.ServerProxy(RES_HOST)
    while True:
        if coordinator.lock():
            for i in range(ITERATIONS):
                value = resource.read()
                resource.write(value + 100)
            coordinator.unlock()
        time.sleep(1)

except KeyboardInterrupt:
    print("closed")



