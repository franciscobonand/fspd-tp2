# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import arm_pb2 as arm__pb2


class StoreDataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Insert = channel.unary_unary(
                '/StoreDataService/Insert',
                request_serializer=arm__pb2.InsertRequest.SerializeToString,
                response_deserializer=arm__pb2.ServerResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/StoreDataService/Get',
                request_serializer=arm__pb2.GetRequest.SerializeToString,
                response_deserializer=arm__pb2.ServerGetResponse.FromString,
                )
        self.Terminate = channel.unary_unary(
                '/StoreDataService/Terminate',
                request_serializer=arm__pb2.TerminateRequest.SerializeToString,
                response_deserializer=arm__pb2.ServerResponse.FromString,
                )


class StoreDataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Terminate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StoreDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=arm__pb2.InsertRequest.FromString,
                    response_serializer=arm__pb2.ServerResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=arm__pb2.GetRequest.FromString,
                    response_serializer=arm__pb2.ServerGetResponse.SerializeToString,
            ),
            'Terminate': grpc.unary_unary_rpc_method_handler(
                    servicer.Terminate,
                    request_deserializer=arm__pb2.TerminateRequest.FromString,
                    response_serializer=arm__pb2.ServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StoreDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StoreDataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StoreDataService/Insert',
            arm__pb2.InsertRequest.SerializeToString,
            arm__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StoreDataService/Get',
            arm__pb2.GetRequest.SerializeToString,
            arm__pb2.ServerGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Terminate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StoreDataService/Terminate',
            arm__pb2.TerminateRequest.SerializeToString,
            arm__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)