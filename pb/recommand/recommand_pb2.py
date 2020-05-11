# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/recommand/recommand.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pb.common import common_pb2 as pb_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb/recommand/recommand.proto',
  package='recommand',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1cpb/recommand/recommand.proto\x12\trecommand\x1a\x16pb/common/common.proto\"*\n\x04Item\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x11\n\titem_type\x18\x02 \x01(\t\"\x0e\n\x0c\x45mptyMessage\"D\n\x10RecommandRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\x11\n\tpage_size\x18\x03 \x01(\r\"U\n\x0eRecommandReply\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.recommand.Item\x12#\n\tpage_info\x18\x02 \x01(\x0b\x32\x10.common.PageInfo\"3\n\x1fSetDefaultRecommandItemsRequest\x12\x10\n\x08item_ids\x18\x01 \x03(\t2\xbc\x01\n\x10RecommandService\x12\x45\n\tRecommand\x12\x1b.recommand.RecommandRequest\x1a\x19.recommand.RecommandReply\"\x00\x12\x61\n\x18SetDefaultRecommandItems\x12*.recommand.SetDefaultRecommandItemsRequest\x1a\x17.recommand.EmptyMessage\"\x00\x62\x06proto3'
  ,
  dependencies=[pb_dot_common_dot_common__pb2.DESCRIPTOR,])




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='recommand.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='recommand.Item.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_type', full_name='recommand.Item.item_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=67,
  serialized_end=109,
)


_EMPTYMESSAGE = _descriptor.Descriptor(
  name='EmptyMessage',
  full_name='recommand.EmptyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=111,
  serialized_end=125,
)


_RECOMMANDREQUEST = _descriptor.Descriptor(
  name='RecommandRequest',
  full_name='recommand.RecommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='recommand.RecommandRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='recommand.RecommandRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='recommand.RecommandRequest.page_size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=127,
  serialized_end=195,
)


_RECOMMANDREPLY = _descriptor.Descriptor(
  name='RecommandReply',
  full_name='recommand.RecommandReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='recommand.RecommandReply.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_info', full_name='recommand.RecommandReply.page_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=282,
)


_SETDEFAULTRECOMMANDITEMSREQUEST = _descriptor.Descriptor(
  name='SetDefaultRecommandItemsRequest',
  full_name='recommand.SetDefaultRecommandItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='recommand.SetDefaultRecommandItemsRequest.item_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=284,
  serialized_end=335,
)

_RECOMMANDREPLY.fields_by_name['items'].message_type = _ITEM
_RECOMMANDREPLY.fields_by_name['page_info'].message_type = pb_dot_common_dot_common__pb2._PAGEINFO
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['EmptyMessage'] = _EMPTYMESSAGE
DESCRIPTOR.message_types_by_name['RecommandRequest'] = _RECOMMANDREQUEST
DESCRIPTOR.message_types_by_name['RecommandReply'] = _RECOMMANDREPLY
DESCRIPTOR.message_types_by_name['SetDefaultRecommandItemsRequest'] = _SETDEFAULTRECOMMANDITEMSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'pb.recommand.recommand_pb2'
  # @@protoc_insertion_point(class_scope:recommand.Item)
  })
_sym_db.RegisterMessage(Item)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'pb.recommand.recommand_pb2'
  # @@protoc_insertion_point(class_scope:recommand.EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

RecommandRequest = _reflection.GeneratedProtocolMessageType('RecommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMANDREQUEST,
  '__module__' : 'pb.recommand.recommand_pb2'
  # @@protoc_insertion_point(class_scope:recommand.RecommandRequest)
  })
_sym_db.RegisterMessage(RecommandRequest)

RecommandReply = _reflection.GeneratedProtocolMessageType('RecommandReply', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMANDREPLY,
  '__module__' : 'pb.recommand.recommand_pb2'
  # @@protoc_insertion_point(class_scope:recommand.RecommandReply)
  })
_sym_db.RegisterMessage(RecommandReply)

SetDefaultRecommandItemsRequest = _reflection.GeneratedProtocolMessageType('SetDefaultRecommandItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETDEFAULTRECOMMANDITEMSREQUEST,
  '__module__' : 'pb.recommand.recommand_pb2'
  # @@protoc_insertion_point(class_scope:recommand.SetDefaultRecommandItemsRequest)
  })
_sym_db.RegisterMessage(SetDefaultRecommandItemsRequest)



_RECOMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='RecommandService',
  full_name='recommand.RecommandService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=338,
  serialized_end=526,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recommand',
    full_name='recommand.RecommandService.Recommand',
    index=0,
    containing_service=None,
    input_type=_RECOMMANDREQUEST,
    output_type=_RECOMMANDREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetDefaultRecommandItems',
    full_name='recommand.RecommandService.SetDefaultRecommandItems',
    index=1,
    containing_service=None,
    input_type=_SETDEFAULTRECOMMANDITEMSREQUEST,
    output_type=_EMPTYMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMANDSERVICE)

DESCRIPTOR.services_by_name['RecommandService'] = _RECOMMANDSERVICE

# @@protoc_insertion_point(module_scope)
