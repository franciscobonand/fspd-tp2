# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arm.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tarm.proto\"@\n\rInsertRequest\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x05\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\x05\"\x12\n\x10TerminateRequest\"\"\n\x0eServerResponse\x12\x10\n\x08response\x18\x01 \x01(\x05\"7\n\x11ServerGetResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\x32\x96\x01\n\x10StoreDataService\x12)\n\x06Insert\x12\x0e.InsertRequest\x1a\x0f.ServerResponse\x12&\n\x03Get\x12\x0b.GetRequest\x1a\x12.ServerGetResponse\x12/\n\tTerminate\x12\x11.TerminateRequest\x1a\x0f.ServerResponseb\x06proto3'
)




_INSERTREQUEST = _descriptor.Descriptor(
  name='InsertRequest',
  full_name='InsertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='InsertRequest.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='InsertRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='InsertRequest.value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=77,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='GetRequest.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=104,
)


_TERMINATEREQUEST = _descriptor.Descriptor(
  name='TerminateRequest',
  full_name='TerminateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=124,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='ServerResponse.response', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=160,
)


_SERVERGETRESPONSE = _descriptor.Descriptor(
  name='ServerGetResponse',
  full_name='ServerGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='ServerGetResponse.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ServerGetResponse.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['InsertRequest'] = _INSERTREQUEST
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['TerminateRequest'] = _TERMINATEREQUEST
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['ServerGetResponse'] = _SERVERGETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InsertRequest = _reflection.GeneratedProtocolMessageType('InsertRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSERTREQUEST,
  '__module__' : 'arm_pb2'
  # @@protoc_insertion_point(class_scope:InsertRequest)
  })
_sym_db.RegisterMessage(InsertRequest)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'arm_pb2'
  # @@protoc_insertion_point(class_scope:GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

TerminateRequest = _reflection.GeneratedProtocolMessageType('TerminateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TERMINATEREQUEST,
  '__module__' : 'arm_pb2'
  # @@protoc_insertion_point(class_scope:TerminateRequest)
  })
_sym_db.RegisterMessage(TerminateRequest)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'arm_pb2'
  # @@protoc_insertion_point(class_scope:ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)

ServerGetResponse = _reflection.GeneratedProtocolMessageType('ServerGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERGETRESPONSE,
  '__module__' : 'arm_pb2'
  # @@protoc_insertion_point(class_scope:ServerGetResponse)
  })
_sym_db.RegisterMessage(ServerGetResponse)



_STOREDATASERVICE = _descriptor.ServiceDescriptor(
  name='StoreDataService',
  full_name='StoreDataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=220,
  serialized_end=370,
  methods=[
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='StoreDataService.Insert',
    index=0,
    containing_service=None,
    input_type=_INSERTREQUEST,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='StoreDataService.Get',
    index=1,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_SERVERGETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Terminate',
    full_name='StoreDataService.Terminate',
    index=2,
    containing_service=None,
    input_type=_TERMINATEREQUEST,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOREDATASERVICE)

DESCRIPTOR.services_by_name['StoreDataService'] = _STOREDATASERVICE

# @@protoc_insertion_point(module_scope)
