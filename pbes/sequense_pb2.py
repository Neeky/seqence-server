# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sequense.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sequense.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0esequense.proto\"1\n\x0fSequenceRequest\x12\x13\n\x06offset\x18\x01 \x01(\x03H\x00\x88\x01\x01\x42\t\n\x07_offset\"$\n\x10SequenceResponse\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x32>\n\x0eSequenceServer\x12,\n\x03get\x12\x10.SequenceRequest\x1a\x11.SequenceResponse\"\x00\x62\x06proto3'
)




_SEQUENCEREQUEST = _descriptor.Descriptor(
  name='SequenceRequest',
  full_name='SequenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='SequenceRequest.offset', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
    _descriptor.OneofDescriptor(
      name='_offset', full_name='SequenceRequest._offset',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=18,
  serialized_end=67,
)


_SEQUENCERESPONSE = _descriptor.Descriptor(
  name='SequenceResponse',
  full_name='SequenceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence', full_name='SequenceResponse.sequence', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=69,
  serialized_end=105,
)

_SEQUENCEREQUEST.oneofs_by_name['_offset'].fields.append(
  _SEQUENCEREQUEST.fields_by_name['offset'])
_SEQUENCEREQUEST.fields_by_name['offset'].containing_oneof = _SEQUENCEREQUEST.oneofs_by_name['_offset']
DESCRIPTOR.message_types_by_name['SequenceRequest'] = _SEQUENCEREQUEST
DESCRIPTOR.message_types_by_name['SequenceResponse'] = _SEQUENCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SequenceRequest = _reflection.GeneratedProtocolMessageType('SequenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCEREQUEST,
  '__module__' : 'sequense_pb2'
  # @@protoc_insertion_point(class_scope:SequenceRequest)
  })
_sym_db.RegisterMessage(SequenceRequest)

SequenceResponse = _reflection.GeneratedProtocolMessageType('SequenceResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCERESPONSE,
  '__module__' : 'sequense_pb2'
  # @@protoc_insertion_point(class_scope:SequenceResponse)
  })
_sym_db.RegisterMessage(SequenceResponse)



_SEQUENCESERVER = _descriptor.ServiceDescriptor(
  name='SequenceServer',
  full_name='SequenceServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=169,
  methods=[
  _descriptor.MethodDescriptor(
    name='get',
    full_name='SequenceServer.get',
    index=0,
    containing_service=None,
    input_type=_SEQUENCEREQUEST,
    output_type=_SEQUENCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEQUENCESERVER)

DESCRIPTOR.services_by_name['SequenceServer'] = _SEQUENCESERVER

# @@protoc_insertion_point(module_scope)
