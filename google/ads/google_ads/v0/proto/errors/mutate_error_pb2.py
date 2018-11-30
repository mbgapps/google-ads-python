# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/mutate_error.proto

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
  name='google/ads/googleads_v0/proto/errors/mutate_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n7google/ads/googleads_v0/proto/errors/mutate_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xb1\x01\n\x0fMutateErrorEnum\"\x9d\x01\n\x0bMutateError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12RESOURCE_NOT_FOUND\x10\x03\x12!\n\x1dID_EXISTS_IN_MULTIPLE_MUTATES\x10\x07\x12\x1d\n\x19INCONSISTENT_FIELD_VALUES\x10\x08\x12\x16\n\x12MUTATE_NOT_ALLOWED\x10\tB\xc6\x01\n\"com.google.ads.googleads.v0.errorsB\x10MutateErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_MUTATEERRORENUM_MUTATEERROR = _descriptor.EnumDescriptor(
  name='MutateError',
  full_name='google.ads.googleads.v0.errors.MutateErrorEnum.MutateError',
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
      name='RESOURCE_NOT_FOUND', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_EXISTS_IN_MULTIPLE_MUTATES', index=3, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_FIELD_VALUES', index=4, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUTATE_NOT_ALLOWED', index=5, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=112,
  serialized_end=269,
)
_sym_db.RegisterEnumDescriptor(_MUTATEERRORENUM_MUTATEERROR)


_MUTATEERRORENUM = _descriptor.Descriptor(
  name='MutateErrorEnum',
  full_name='google.ads.googleads.v0.errors.MutateErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MUTATEERRORENUM_MUTATEERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=269,
)

_MUTATEERRORENUM_MUTATEERROR.containing_type = _MUTATEERRORENUM
DESCRIPTOR.message_types_by_name['MutateErrorEnum'] = _MUTATEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MutateErrorEnum = _reflection.GeneratedProtocolMessageType('MutateErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEERRORENUM,
  __module__ = 'google.ads.google_ads.v0.proto.errors.mutate_error_pb2'
  ,
  __doc__ = """Container for enum describing possible mutate errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.MutateErrorEnum)
  ))
_sym_db.RegisterMessage(MutateErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\020MutateErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
