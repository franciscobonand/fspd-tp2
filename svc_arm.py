#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
import sys

# define 'database'
data = {}
# variable used for terminating the server
quit = 0


# insert receives key, description and value and adds it
# to the database and returns 0, if the key doesn't exist.
# doesn't add/update the key if it already exists, and returns -1
def insert(key, desc, val):
    if key in data:
        return -1

    data[key] = {"desc": desc, "val": val}
    return 0


# get returns description and value associated with the given key, if
# it exists. Returns -1 otherwise
def get(key):
    if key not in data:
        return -1

    return (data[key].get("desc"), data[key].get("val"))


# terminate closes the server
def terminate():
    global quit
    quit = 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid arguments to run server")
        print("should be './svc_arm <port>")
        sys.exit(1)

    try:
        server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])))
    except:
        print("invalid port")
        sys.exit(2)

    server.register_function(insert)
    server.register_function(get)
    server.register_function(terminate)

    # Run the server's main loop
    while not quit:
        server.handle_request()
