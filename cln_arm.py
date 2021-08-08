#!/usr/bin/env python3

import arm_pb2_grpc
import arm_pb2
import grpc
import sys


def run(addr):
    # establishes communication with server running on address 'addr'
    with grpc.insecure_channel(addr) as channel:
        # gets stub structure defined in protobuf file
        stub = arm_pb2_grpc.StoreDataServiceStub(channel)
        # endless loop that takes user commands
        while True:
            try:
                cmd = input().split(",")

                # handles insert command
                if cmd[0] == "I" and len(cmd) == 4:
                    request = stub.Insert(arm_pb2.InsertRequest(
                        key=int(cmd[1]),
                        description=cmd[2],
                        value=int(cmd[3])
                    ))
                    print(request.response)
                # handles get/consult command
                elif cmd[0] == "C" and len(cmd) == 2:
                    request = stub.Get(arm_pb2.GetRequest(
                        key=int(cmd[1])
                    ))
                    # prints key's description and value, if key exists in database
                    if request.value != -1:
                        print(f"{request.description}, {request.value}")
                        continue
                    # prints -1 otherwise
                    print(request.value)
                # handles terminate command and closes client
                elif cmd[0] == "T" and len(cmd) == 1:
                    request = stub.Terminate(arm_pb2.TerminateRequest())
                    print(request.response)
                    break
                else:
                    eprint("invalid command")
            except:
                # closes client when user ctrl+c
                print("error while sending request, closing client...")
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
        print("should be './cln_arm <server_host>:<server_port>")
        sys.exit(1)

    run(sys.argv[1])
