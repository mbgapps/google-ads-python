# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/feed_mapping_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import feed_mapping_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_feed__mapping__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/feed_mapping_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nAgoogle/ads/googleads_v0/proto/services/feed_mapping_service.proto\x12 google.ads.googleads.v0.services\x1a:google/ads/googleads_v0/proto/resources/feed_mapping.proto\x1a\x1cgoogle/api/annotations.proto\".\n\x15GetFeedMappingRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"|\n\x19MutateFeedMappingsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12J\n\noperations\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v0.services.FeedMappingOperation\"w\n\x14\x46\x65\x65\x64MappingOperation\x12@\n\x06\x63reate\x18\x01 \x01(\x0b\x32..google.ads.googleads.v0.resources.FeedMappingH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"h\n\x1aMutateFeedMappingsResponse\x12J\n\x07results\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v0.services.MutateFeedMappingResult\"0\n\x17MutateFeedMappingResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x98\x03\n\x12\x46\x65\x65\x64MappingService\x12\xb1\x01\n\x0eGetFeedMapping\x12\x37.google.ads.googleads.v0.services.GetFeedMappingRequest\x1a..google.ads.googleads.v0.resources.FeedMapping\"6\x82\xd3\xe4\x93\x02\x30\x12./v0/{resource_name=customers/*/feedMappings/*}\x12\xcd\x01\n\x12MutateFeedMappings\x12;.google.ads.googleads.v0.services.MutateFeedMappingsRequest\x1a<.google.ads.googleads.v0.services.MutateFeedMappingsResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/v0/customers/{customer_id=*}/feedMappings:mutate:\x01*B\xd7\x01\n$com.google.ads.googleads.v0.servicesB\x17\x46\x65\x65\x64MappingServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_feed__mapping__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETFEEDMAPPINGREQUEST = _descriptor.Descriptor(
  name='GetFeedMappingRequest',
  full_name='google.ads.googleads.v0.services.GetFeedMappingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetFeedMappingRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=239,
)


_MUTATEFEEDMAPPINGSREQUEST = _descriptor.Descriptor(
  name='MutateFeedMappingsRequest',
  full_name='google.ads.googleads.v0.services.MutateFeedMappingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateFeedMappingsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateFeedMappingsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=365,
)


_FEEDMAPPINGOPERATION = _descriptor.Descriptor(
  name='FeedMappingOperation',
  full_name='google.ads.googleads.v0.services.FeedMappingOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.FeedMappingOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.FeedMappingOperation.remove', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.FeedMappingOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=367,
  serialized_end=486,
)


_MUTATEFEEDMAPPINGSRESPONSE = _descriptor.Descriptor(
  name='MutateFeedMappingsResponse',
  full_name='google.ads.googleads.v0.services.MutateFeedMappingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateFeedMappingsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=592,
)


_MUTATEFEEDMAPPINGRESULT = _descriptor.Descriptor(
  name='MutateFeedMappingResult',
  full_name='google.ads.googleads.v0.services.MutateFeedMappingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateFeedMappingResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=642,
)

_MUTATEFEEDMAPPINGSREQUEST.fields_by_name['operations'].message_type = _FEEDMAPPINGOPERATION
_FEEDMAPPINGOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_feed__mapping__pb2._FEEDMAPPING
_FEEDMAPPINGOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDMAPPINGOPERATION.fields_by_name['create'])
_FEEDMAPPINGOPERATION.fields_by_name['create'].containing_oneof = _FEEDMAPPINGOPERATION.oneofs_by_name['operation']
_FEEDMAPPINGOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDMAPPINGOPERATION.fields_by_name['remove'])
_FEEDMAPPINGOPERATION.fields_by_name['remove'].containing_oneof = _FEEDMAPPINGOPERATION.oneofs_by_name['operation']
_MUTATEFEEDMAPPINGSRESPONSE.fields_by_name['results'].message_type = _MUTATEFEEDMAPPINGRESULT
DESCRIPTOR.message_types_by_name['GetFeedMappingRequest'] = _GETFEEDMAPPINGREQUEST
DESCRIPTOR.message_types_by_name['MutateFeedMappingsRequest'] = _MUTATEFEEDMAPPINGSREQUEST
DESCRIPTOR.message_types_by_name['FeedMappingOperation'] = _FEEDMAPPINGOPERATION
DESCRIPTOR.message_types_by_name['MutateFeedMappingsResponse'] = _MUTATEFEEDMAPPINGSRESPONSE
DESCRIPTOR.message_types_by_name['MutateFeedMappingResult'] = _MUTATEFEEDMAPPINGRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeedMappingRequest = _reflection.GeneratedProtocolMessageType('GetFeedMappingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEEDMAPPINGREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedMappingService.GetFeedMapping][google.ads.googleads.v0.services.FeedMappingService.GetFeedMapping].
  
  
  Attributes:
      resource_name:
          The resource name of the feed mapping to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetFeedMappingRequest)
  ))
_sym_db.RegisterMessage(GetFeedMappingRequest)

MutateFeedMappingsRequest = _reflection.GeneratedProtocolMessageType('MutateFeedMappingsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDMAPPINGSREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedMappingService.MutateFeedMappings][google.ads.googleads.v0.services.FeedMappingService.MutateFeedMappings].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose feed mappings are being modified.
      operations:
          The list of operations to perform on individual feed mappings.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateFeedMappingsRequest)
  ))
_sym_db.RegisterMessage(MutateFeedMappingsRequest)

FeedMappingOperation = _reflection.GeneratedProtocolMessageType('FeedMappingOperation', (_message.Message,), dict(
  DESCRIPTOR = _FEEDMAPPINGOPERATION,
  __module__ = 'google.ads.google_ads.v0.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """A single operation (create, remove) on a feed mapping.
  
  
  Attributes:
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          feed mapping.
      remove:
          Remove operation: A resource name for the removed feed mapping
          is expected, in this format:  ``customers/{customer_id}/feedMa
          ppings/{feed_id}_{feed_mapping_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.FeedMappingOperation)
  ))
_sym_db.RegisterMessage(FeedMappingOperation)

MutateFeedMappingsResponse = _reflection.GeneratedProtocolMessageType('MutateFeedMappingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDMAPPINGSRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """Response message for a feed mapping mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateFeedMappingsResponse)
  ))
_sym_db.RegisterMessage(MutateFeedMappingsResponse)

MutateFeedMappingResult = _reflection.GeneratedProtocolMessageType('MutateFeedMappingResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDMAPPINGRESULT,
  __module__ = 'google.ads.google_ads.v0.proto.services.feed_mapping_service_pb2'
  ,
  __doc__ = """The result for the feed mapping mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateFeedMappingResult)
  ))
_sym_db.RegisterMessage(MutateFeedMappingResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\027FeedMappingServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_FEEDMAPPINGSERVICE = _descriptor.ServiceDescriptor(
  name='FeedMappingService',
  full_name='google.ads.googleads.v0.services.FeedMappingService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=645,
  serialized_end=1053,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeedMapping',
    full_name='google.ads.googleads.v0.services.FeedMappingService.GetFeedMapping',
    index=0,
    containing_service=None,
    input_type=_GETFEEDMAPPINGREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_feed__mapping__pb2._FEEDMAPPING,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0020\022./v0/{resource_name=customers/*/feedMappings/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateFeedMappings',
    full_name='google.ads.googleads.v0.services.FeedMappingService.MutateFeedMappings',
    index=1,
    containing_service=None,
    input_type=_MUTATEFEEDMAPPINGSREQUEST,
    output_type=_MUTATEFEEDMAPPINGSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0026\"1/v0/customers/{customer_id=*}/feedMappings:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_FEEDMAPPINGSERVICE)

DESCRIPTOR.services_by_name['FeedMappingService'] = _FEEDMAPPINGSERVICE

# @@protoc_insertion_point(module_scope)
