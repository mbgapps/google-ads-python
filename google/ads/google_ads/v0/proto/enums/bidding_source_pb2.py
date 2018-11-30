# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/bidding_source.proto

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
  name='google/ads/googleads_v0/proto/enums/bidding_source.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n8google/ads/googleads_v0/proto/enums/bidding_source.proto\x12\x1dgoogle.ads.googleads.v0.enums\"}\n\x11\x42iddingSourceEnum\"h\n\rBiddingSource\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x41\x44GROUP\x10\x02\x12\r\n\tCRITERION\x10\x03\x12\x1d\n\x19\x43\x41MPAIGN_BIDDING_STRATEGY\x10\x05\x42\xc3\x01\n!com.google.ads.googleads.v0.enumsB\x12\x42iddingSourceProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_BIDDINGSOURCEENUM_BIDDINGSOURCE = _descriptor.EnumDescriptor(
  name='BiddingSource',
  full_name='google.ads.googleads.v0.enums.BiddingSourceEnum.BiddingSource',
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
      name='ADGROUP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITERION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BIDDING_STRATEGY', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=112,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_BIDDINGSOURCEENUM_BIDDINGSOURCE)


_BIDDINGSOURCEENUM = _descriptor.Descriptor(
  name='BiddingSourceEnum',
  full_name='google.ads.googleads.v0.enums.BiddingSourceEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDDINGSOURCEENUM_BIDDINGSOURCE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=216,
)

_BIDDINGSOURCEENUM_BIDDINGSOURCE.containing_type = _BIDDINGSOURCEENUM
DESCRIPTOR.message_types_by_name['BiddingSourceEnum'] = _BIDDINGSOURCEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingSourceEnum = _reflection.GeneratedProtocolMessageType('BiddingSourceEnum', (_message.Message,), dict(
  DESCRIPTOR = _BIDDINGSOURCEENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.bidding_source_pb2'
  ,
  __doc__ = """Container for enum describing possible bidding sources.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.BiddingSourceEnum)
  ))
_sym_db.RegisterMessage(BiddingSourceEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\022BiddingSourceProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
