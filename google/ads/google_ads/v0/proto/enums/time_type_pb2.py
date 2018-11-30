# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/time_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/time_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n3google/ads/googleads_v0/proto/enums/time_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"N\n\x0cTimeTypeEnum\">\n\x08TimeType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03NOW\x10\x02\x12\x0b\n\x07\x46OREVER\x10\x03\x42\xbe\x01\n!com.google.ads.googleads.v0.enumsB\rTimeTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_TIMETYPEENUM_TIMETYPE = _descriptor.EnumDescriptor(
  name='TimeType',
  full_name='google.ads.googleads.v0.enums.TimeTypeEnum.TimeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOREVER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=102,
  serialized_end=164,
)
_sym_db.RegisterEnumDescriptor(_TIMETYPEENUM_TIMETYPE)


_TIMETYPEENUM = _descriptor.Descriptor(
  name='TimeTypeEnum',
  full_name='google.ads.googleads.v0.enums.TimeTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TIMETYPEENUM_TIMETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=164,
)

_TIMETYPEENUM_TIMETYPE.containing_type = _TIMETYPEENUM
DESCRIPTOR.message_types_by_name['TimeTypeEnum'] = _TIMETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeTypeEnum = _reflection.GeneratedProtocolMessageType('TimeTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _TIMETYPEENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.time_type_pb2'
  ,
  __doc__ = """Message describing time types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.TimeTypeEnum)
  ))
_sym_db.RegisterMessage(TimeTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\rTimeTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
