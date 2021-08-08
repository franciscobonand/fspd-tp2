#!/usr/bin/env python3

import grpc
import comp_pb2
import comp_pb2_grpc
import sys


def run(addr):
    # establishes communication with server running on address 'addr'
    with grpc.insecure_channel(addr) as channel:
        # gets stub structure defined in protobuf file
        stub = comp_pb2_grpc.MainServiceStub(channel)
        # endless loop that takes user commands
        while True:
            try:
                cmd = input().split(",")

                # handles get/consult command
                if cmd[0] == "C" and len(cmd) == 2:
                    response = stub.Get(comp_pb2.MainRequest(
                        key=int(cmd[1])
                    ))
                    print(f"{response.nome}, " +
                          f"{response.matr}, " +
                          f"{response.curso}, " +
                          f"{response.cred}")

                # handles terminate command and closes client
                elif cmd[0] == "T" and len(cmd) == 1:
                    req = stub.Terminate(comp_pb2.CompTerminateRequest())
                    print(req.response)
                    break
                else:
                    eprint("invalid command")
            except KeyboardInterrupt:
                # closes client when user ctrl+c
                print("closing client...")
                channel.unsubscribe(close)
                exit()


# close closes the client channel
def close(channel):
    channel.close()


# eprint prints in stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid arguments to run client")
        print("should be './cln_comp.py <server_host>:<server_port>")
        sys.exit(1)

    run(sys.argv[1])
