# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/campaign_budget.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import budget_delivery_method_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_budget__delivery__method__pb2
from google.ads.google_ads.v0.proto.enums import budget_status_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_budget__status__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/campaign_budget.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/resources/campaign_budget.proto\x12!google.ads.googleads.v0.resources\x1a@google/ads/googleads_v0/proto/enums/budget_delivery_method.proto\x1a\x37google/ads/googleads_v0/proto/enums/budget_status.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x8c\x04\n\x0e\x43\x61mpaignBudget\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\ramount_micros\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13total_amount_micros\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12L\n\x06status\x18\x06 \x01(\x0e\x32<.google.ads.googleads.v0.enums.BudgetStatusEnum.BudgetStatus\x12\x65\n\x0f\x64\x65livery_method\x18\x07 \x01(\x0e\x32L.google.ads.googleads.v0.enums.BudgetDeliveryMethodEnum.BudgetDeliveryMethod\x12\x35\n\x11\x65xplicitly_shared\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x0freference_count\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\xd8\x01\n%com.google.ads.googleads.v0.resourcesB\x13\x43\x61mpaignBudgetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_budget__delivery__method__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_budget__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CAMPAIGNBUDGET = _descriptor.Descriptor(
  name='CampaignBudget',
  full_name='google.ads.googleads.v0.resources.CampaignBudget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.CampaignBudget.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v0.resources.CampaignBudget.id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v0.resources.CampaignBudget.name', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_micros', full_name='google.ads.googleads.v0.resources.CampaignBudget.amount_micros', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_amount_micros', full_name='google.ads.googleads.v0.resources.CampaignBudget.total_amount_micros', index=4,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v0.resources.CampaignBudget.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delivery_method', full_name='google.ads.googleads.v0.resources.CampaignBudget.delivery_method', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='explicitly_shared', full_name='google.ads.googleads.v0.resources.CampaignBudget.explicitly_shared', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_count', full_name='google.ads.googleads.v0.resources.CampaignBudget.reference_count', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=256,
  serialized_end=780,
)

_CAMPAIGNBUDGET.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNBUDGET.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNBUDGET.fields_by_name['amount_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNBUDGET.fields_by_name['total_amount_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNBUDGET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_budget__status__pb2._BUDGETSTATUSENUM_BUDGETSTATUS
_CAMPAIGNBUDGET.fields_by_name['delivery_method'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_budget__delivery__method__pb2._BUDGETDELIVERYMETHODENUM_BUDGETDELIVERYMETHOD
_CAMPAIGNBUDGET.fields_by_name['explicitly_shared'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CAMPAIGNBUDGET.fields_by_name['reference_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['CampaignBudget'] = _CAMPAIGNBUDGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignBudget = _reflection.GeneratedProtocolMessageType('CampaignBudget', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNBUDGET,
  __module__ = 'google.ads.google_ads.v0.proto.resources.campaign_budget_pb2'
  ,
  __doc__ = """A campaign budget.
  
  
  Attributes:
      resource_name:
          The resource name of the campaign budget. Campaign budget
          resource names have the form:
          ``customers/{customer_id}/campaignBudgets/{budget_id}``
      id:
          The ID of the campaign budget.  A campaign budget is created
          using the CampaignBudgetService create operation and is
          assigned a budget ID. A budget ID can be shared across
          different campaigns; the system will then allocate the
          campaign budget among different campaigns to get optimum
          results.
      name:
          The name of the campaign budget.  When creating a campaign
          budget through CampaignBudgetService, every explicitly shared
          campaign budget must have a non-null, non-empty name. Campaign
          budgets that are not explicitly shared derive their name from
          the attached campaign's name.  The length of this string must
          be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed).
      amount_micros:
          The amount of the budget, in the local currency for the
          account. Amount is specified in micros, where one million is
          equivalent to one currency unit.
      total_amount_micros:
          The lifetime amount of the budget, in the local currency for
          the account. Amount is specified in micros, where one million
          is equivalent to one currency unit.
      status:
          The status of this campaign budget. This field is read-only.
      delivery_method:
          The delivery method that determines the rate at which the
          campaign budget is spent.  Defaults to STANDARD if unspecified
          in a create operation.
      explicitly_shared:
          Whether the budget is explicitly shared. This field is set to
          false by default.  If true, the budget was created with the
          purpose of sharing across one or more campaigns.  If false,
          the budget was created with the intention of only being used
          with a single campaign. The budget's name and status will stay
          in sync with the campaign's name and status. Attempting to
          share the budget with a second campaign will result in an
          error.  A non-shared budget can become an explicitly shared.
          The same operation must also assign the budget a name.  A
          shared campaign budget can never become non-shared.
      reference_count:
          The number of campaigns actively using the budget.  This field
          is read-only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.CampaignBudget)
  ))
_sym_db.RegisterMessage(CampaignBudget)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\023CampaignBudgetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)
