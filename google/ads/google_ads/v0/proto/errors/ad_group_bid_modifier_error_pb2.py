# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/ad_group_bid_modifier_error.proto

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
  name='google/ads/googleads_v0/proto/errors/ad_group_bid_modifier_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\nFgoogle/ads/googleads_v0/proto/errors/ad_group_bid_modifier_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xb6\x01\n\x1b\x41\x64GroupBidModifierErrorEnum\"\x96\x01\n\x17\x41\x64GroupBidModifierError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1e\n\x1a\x43RITERION_ID_NOT_SUPPORTED\x10\x02\x12=\n9CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER\x10\x03\x42\xd2\x01\n\"com.google.ads.googleads.v0.errorsB\x1c\x41\x64GroupBidModifierErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR = _descriptor.EnumDescriptor(
  name='AdGroupBidModifierError',
  full_name='google.ads.googleads.v0.errors.AdGroupBidModifierErrorEnum.AdGroupBidModifierError',
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
      name='CRITERION_ID_NOT_SUPPORTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=139,
  serialized_end=289,
)
_sym_db.RegisterEnumDescriptor(_ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR)


_ADGROUPBIDMODIFIERERRORENUM = _descriptor.Descriptor(
  name='AdGroupBidModifierErrorEnum',
  full_name='google.ads.googleads.v0.errors.AdGroupBidModifierErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=289,
)

_ADGROUPBIDMODIFIERERRORENUM_ADGROUPBIDMODIFIERERROR.containing_type = _ADGROUPBIDMODIFIERERRORENUM
DESCRIPTOR.message_types_by_name['AdGroupBidModifierErrorEnum'] = _ADGROUPBIDMODIFIERERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupBidModifierErrorEnum = _reflection.GeneratedProtocolMessageType('AdGroupBidModifierErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPBIDMODIFIERERRORENUM,
  __module__ = 'google.ads.google_ads.v0.proto.errors.ad_group_bid_modifier_error_pb2'
  ,
  __doc__ = """Container for enum describing possible ad group bid modifier errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.AdGroupBidModifierErrorEnum)
  ))
_sym_db.RegisterMessage(AdGroupBidModifierErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\034AdGroupBidModifierErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
