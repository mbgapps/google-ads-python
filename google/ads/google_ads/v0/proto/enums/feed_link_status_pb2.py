# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/feed_link_status.proto

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
  name='google/ads/googleads_v0/proto/enums/feed_link_status.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n:google/ads/googleads_v0/proto/enums/feed_link_status.proto\x12\x1dgoogle.ads.googleads.v0.enums\"^\n\x12\x46\x65\x65\x64LinkStatusEnum\"H\n\x0e\x46\x65\x65\x64LinkStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x45NABLED\x10\x02\x12\x0b\n\x07REMOVED\x10\x03\x42\xc4\x01\n!com.google.ads.googleads.v0.enumsB\x13\x46\x65\x65\x64LinkStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_FEEDLINKSTATUSENUM_FEEDLINKSTATUS = _descriptor.EnumDescriptor(
  name='FeedLinkStatus',
  full_name='google.ads.googleads.v0.enums.FeedLinkStatusEnum.FeedLinkStatus',
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
      name='ENABLED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=115,
  serialized_end=187,
)
_sym_db.RegisterEnumDescriptor(_FEEDLINKSTATUSENUM_FEEDLINKSTATUS)


_FEEDLINKSTATUSENUM = _descriptor.Descriptor(
  name='FeedLinkStatusEnum',
  full_name='google.ads.googleads.v0.enums.FeedLinkStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDLINKSTATUSENUM_FEEDLINKSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=187,
)

_FEEDLINKSTATUSENUM_FEEDLINKSTATUS.containing_type = _FEEDLINKSTATUSENUM
DESCRIPTOR.message_types_by_name['FeedLinkStatusEnum'] = _FEEDLINKSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedLinkStatusEnum = _reflection.GeneratedProtocolMessageType('FeedLinkStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDLINKSTATUSENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.feed_link_status_pb2'
  ,
  __doc__ = """Container for an enum describing possible statuses of a feed link.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.FeedLinkStatusEnum)
  ))
_sym_db.RegisterMessage(FeedLinkStatusEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\023FeedLinkStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
