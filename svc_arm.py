#!/usr/bin/env python3

from concurrent import futures
import grpc
import arm_pb2
import arm_pb2_grpc
import sys

# variable used for closing server when terminate command is received
quit = 0


class Listener(arm_pb2_grpc.StoreDataServiceServicer):
    def __init__(self) -> None:
        self.data = {}

    # Insert receives key, description and value and adds it
    # to the database and returns 0, if the key doesn't exist.
    # doesn't add/update the key if it already exists, and returns -1
    def Insert(self, request, context):
        if request.key in self.data:
            return -1

        self.data[request.key] = {
            "desc": request.description, "val": request.value}
        return arm_pb2.ServerResponse(response=0)

    # Get returns description and value associated with the given key, if
    # it exists. Returns -1 otherwise

    def Get(self, request, context):
        if request.key not in self.data:
            return arm_pb2.ServerGetResponse(value=-1, description="")

        return arm_pb2.ServerGetResponse(value=self.data[request.key].get("val"),
                                         description=self.data[request.key].get("desc"))

    # Terminate closes the server

    def Terminate(self, request, context):
        global quit
        quit = 1
        return arm_pb2.ServerResponse(response=0)

# serve runs the server in 'localhost' on the given port


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    arm_pb2_grpc.add_StoreDataServiceServicer_to_server(Listener(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    try:
        while not quit:
            continue
    except KeyboardInterrupt:
        # closes server when user ctrl+c
        # print("keyboard interrupt, closing server...")
        pass

    server.stop(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid arguments to run server")
        print("should be './svc_arm <port>")
        sys.exit(1)

    serve(sys.argv[1])
