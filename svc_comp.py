#!/usr/bin/env python3

from concurrent import futures
import grpc
import comp_pb2
import comp_pb2_grpc
import sys
import threading

# variables used for closing servers when terminate command is received
quit_main = 0
quit_siga = 0
quit_matr = 0


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
            siga_stub = comp_pb2_grpc.SigaServiceStub(channel)
            siga_response = siga_stub.Get(
                comp_pb2.SigaRequest(key=request.key))
            channel.unsubscribe(close)

        if not siga_response.matr:
            return comp_pb2.MainResponse(nome="", matr=0, curso="", cred=0)

        with grpc.insecure_channel(self.matr_addr) as channel:
            matr_stub = comp_pb2_grpc.MatriculaServiceStub(channel)
            matr_response = matr_stub.Get(
                comp_pb2.MatriculaRequest(matr=siga_response.matr))
            channel.unsubscribe(close)

        if not matr_response.cred:
            return comp_pb2.MainResponse(nome=siga_response.nome, matr=siga_response.matr, curso="N/M", cred=0)

        return comp_pb2.MainResponse(nome=siga_response.nome,
                                     matr=siga_response.matr,
                                     curso=matr_response.curso,
                                     cred=matr_response.cred)

    def Terminate(self, request, context):
        with grpc.insecure_channel(self.siga_addr) as channel:
            siga_stub = comp_pb2_grpc.SigaServiceStub(channel)
            siga_req = siga_stub.Terminate(comp_pb2.TerminateRequest())
            channel.unsubscribe(close)

        with grpc.insecure_channel(self.matr_addr) as channel:
            matr_stub = comp_pb2_grpc.MatriculaServiceStub(channel)
            matr_req = matr_stub.Terminate(comp_pb2.TerminateRequest())
            channel.unsubscribe(close)

        global quit_main
        quit_main = 1

        return comp_pb2.ServerResponse(response=(siga_req.response + matr_req.response))


class SigaListener(comp_pb2_grpc.SigaServiceServicer):
    def __init__(self) -> None:
        # sets fake data for testing purposes
        self.data = {
            1: {"nome": "estudante1", "matr": 2015089650},
            2: {"nome": "estudante2", "matr": 2018001337},
            3: {"nome": "estudante3", "matr": 2021042069}
        }

    # Get returns name and matr associated with the given key, if
    # it exists. Returns empty string and 0 otherwise
    def Get(self, request, context):
        if request.key not in self.data:
            return comp_pb2.SigaResponse(nome="", matr=0)

        return comp_pb2.SigaResponse(nome=self.data[request.key].get("nome"),
                                     matr=self.data[request.key].get("matr"))

    # Terminate closes the server
    def Terminate(self, request, context):
        global quit_siga
        quit_siga = 1
        return comp_pb2.ServerResponse(response=0)


class MatrListener(comp_pb2_grpc.MatriculaServiceServicer):
    def __init__(self) -> None:
        # sets fake data for testing purposes
        self.data = {
            2015089650: {"curso": "FDSP", "cred": 30},
            2018001337: {"curso": "Cybersec", "cred": 60}
        }

    # Get returns curso and cred associated with the given matr, if
    # it exists. Returns empty string and 0 otherwise
    def Get(self, request, context):
        if request.matr not in self.data:
            return comp_pb2.MatriculaResponse(curso="", cred=0)

        return comp_pb2.SigaResponse(nome=self.data[request.matr].get("curso"),
                                     matr=self.data[request.matr].get("cred"))

    # Terminate closes the server
    def Terminate(self, request, context):
        global quit_matr
        quit_matr = 1
        return comp_pb2.ServerResponse(response=0)


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
        global quit_matr
        global quit_siga
        quit_siga = 1
        quit_matr = 1
        # closes server when user ctrl+c
        # print("closing server...")

    server.stop(0)


def start_siga_server(addr):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    comp_pb2_grpc.add_SigaServiceServicer_to_server(SigaListener(), server)
    server.add_insecure_port(f"{addr}")
    server.start()
    try:
        # print(f"siga server listening on address {addr}")
        while not quit_siga:
            continue
    except KeyboardInterrupt:
        # closes server when user ctrl+c
        # print("keyboard interrupt, closing siga server...")
        pass

    server.stop(0)


def start_matr_server(addr):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    comp_pb2_grpc.add_MatriculaServiceServicer_to_server(
        MatrListener(), server)
    server.add_insecure_port(f"{addr}")
    server.start()
    try:
        # print(f"matr server listening on address {addr}")
        while not quit_matr:
            continue
    except KeyboardInterrupt:
        # closes server when user ctrl+c
        # print("keyboard interrupt, closing matr server...")
        pass

    server.stop(0)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("invalid arguments to run server")
        print("should be './svc_comp <port> <siga_addr> <matr_addr>")
        sys.exit(1)

    siga = threading.Thread(target=start_siga_server, args=(sys.argv[2],))
    matr = threading.Thread(target=start_matr_server, args=(sys.argv[3],))

    siga.start()
    matr.start()

    serve(sys.argv[1], sys.argv[2], sys.argv[3])

    siga.join()
    matr.join()
