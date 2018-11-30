# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/customer_client_link.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import manager_link_status_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_manager__link__status__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/customer_client_link.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\nBgoogle/ads/googleads_v0/proto/resources/customer_client_link.proto\x12!google.ads.googleads.v0.resources\x1a=google/ads/googleads_v0/proto/enums/manager_link_status.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x9c\x02\n\x12\x43ustomerClientLink\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x35\n\x0f\x63lient_customer\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0fmanager_link_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12V\n\x06status\x18\x05 \x01(\x0e\x32\x46.google.ads.googleads.v0.enums.ManagerLinkStatusEnum.ManagerLinkStatus\x12*\n\x06hidden\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\xdc\x01\n%com.google.ads.googleads.v0.resourcesB\x17\x43ustomerClientLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_manager__link__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CUSTOMERCLIENTLINK = _descriptor.Descriptor(
  name='CustomerClientLink',
  full_name='google.ads.googleads.v0.resources.CustomerClientLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.CustomerClientLink.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_customer', full_name='google.ads.googleads.v0.resources.CustomerClientLink.client_customer', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_link_id', full_name='google.ads.googleads.v0.resources.CustomerClientLink.manager_link_id', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v0.resources.CustomerClientLink.status', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='google.ads.googleads.v0.resources.CustomerClientLink.hidden', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=201,
  serialized_end=485,
)

_CUSTOMERCLIENTLINK.fields_by_name['client_customer'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERCLIENTLINK.fields_by_name['manager_link_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CUSTOMERCLIENTLINK.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_manager__link__status__pb2._MANAGERLINKSTATUSENUM_MANAGERLINKSTATUS
_CUSTOMERCLIENTLINK.fields_by_name['hidden'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['CustomerClientLink'] = _CUSTOMERCLIENTLINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerClientLink = _reflection.GeneratedProtocolMessageType('CustomerClientLink', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERCLIENTLINK,
  __module__ = 'google.ads.google_ads.v0.proto.resources.customer_client_link_pb2'
  ,
  __doc__ = """Represents customer client link relationship.
  
  
  Attributes:
      resource_name:
          Name of the resource. CustomerClientLink resource names have
          the form:  ``customers/{customer_id}/customerClientLinks/{clie
          nt_customer_id}_{manager_link_id}``
      client_customer:
          The client customer linked to this customer. Read only.
      manager_link_id:
          This is uniquely identifies a customer client link. Read only.
      status:
          This is the status of the link between client and manager.
      hidden:
          The visibility of the link. Users can choose whether or not to
          see hidden links in the AdWords UI. Default value is false
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.CustomerClientLink)
  ))
_sym_db.RegisterMessage(CustomerClientLink)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\027CustomerClientLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)
