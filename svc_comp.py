#!/usr/bin/env python3

from concurrent import futures
import grpc
import comp_pb2
import comp_pb2_grpc
import arm_pb2_grpc
import arm_pb2
import sys

# variable used for closing server when terminate command is received
quit_main = 0


# close closes the given channel
def close(channel):
    channel.close()


class MainListener(comp_pb2_grpc.MainServiceServicer):
    def __init__(self, siga_addr, matr_addr) -> None:
        self.siga_addr = siga_addr
        self.matr_addr = matr_addr

    # Get returns nome, matr, curso and cred associated with the given key, if
    # all of it exists. Returns the partial existant data otherwise
    def Get(self, request, context):
        with grpc.insecure_channel(self.siga_addr) as channel:
            siga_stub = arm_pb2_grpc.StoreDataServiceStub(channel)
            siga_response = siga_stub.Get(
                arm_pb2.GetRequest(key=int(request.key)))
            channel.unsubscribe(close)

        if not siga_response.description:
            return comp_pb2.MainResponse(nome="", matr=0, curso="", cred=0)

        with grpc.insecure_channel(self.matr_addr) as channel:
            matr_stub = arm_pb2_grpc.StoreDataServiceStub(channel)
            matr_response = matr_stub.Get(
                arm_pb2.GetRequest(key=siga_response.value))
            channel.unsubscribe(close)

        if not matr_response.description:
            return comp_pb2.MainResponse(nome=siga_response.description, matr=siga_response.value, curso="N/M", cred=0)

        return comp_pb2.MainResponse(nome=siga_response.description,
                                     matr=siga_response.value,
                                     curso=matr_response.description,
                                     cred=matr_response.value)

    def Terminate(self, request, context):
        with grpc.insecure_channel(self.siga_addr) as channel:
            siga_stub = arm_pb2_grpc.StoreDataServiceStub(channel)
            siga_req = siga_stub.Terminate(arm_pb2.TerminateRequest())
            channel.unsubscribe(close)

        with grpc.insecure_channel(self.matr_addr) as channel:
            matr_stub = arm_pb2_grpc.StoreDataServiceStub(channel)
            matr_req = matr_stub.Terminate(arm_pb2.TerminateRequest())
            channel.unsubscribe(close)

        global quit_main
        quit_main = 1

        return comp_pb2.CompServerResponse(response=(siga_req.response + matr_req.response))


# serve runs the server in 'localhost' on the given port
def serve(port, siga_addr, matr_addr):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    comp_pb2_grpc.add_MainServiceServicer_to_server(
        MainListener(siga_addr, matr_addr), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    try:
        # print(f"server listening on port {port}")
        while not quit_main:
            continue
    except KeyboardInterrupt:
        pass
        # closes server when user ctrl+c
        # print("closing server...")

    server.stop(0)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("invalid arguments to run server")
        print("should be './svc_comp <port> <siga_addr> <matr_addr>")
        sys.exit(1)

    serve(sys.argv[1], sys.argv[2], sys.argv[3])
