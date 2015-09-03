# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commons.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commons.proto',
  package='org.midonet.cluster.models',
  serialized_pb=_b('\n\rcommons.proto\x12\x1aorg.midonet.cluster.models\" \n\x04UUID\x12\x0b\n\x03msb\x18\x01 \x02(\x04\x12\x0b\n\x03lsb\x18\x02 \x02(\x04\"T\n\tIPAddress\x12\x36\n\x07version\x18\x01 \x02(\x0e\x32%.org.midonet.cluster.models.IPVersion\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\t\"j\n\x08IPSubnet\x12\x36\n\x07version\x18\x01 \x02(\x0e\x32%.org.midonet.cluster.models.IPVersion\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x15\n\rprefix_length\x18\x03 \x01(\r\"(\n\nInt32Range\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"\xb8\n\n\tCondition\x12\x17\n\x0f\x63onjunction_inv\x18\x01 \x01(\x08\x12\x1a\n\x12match_forward_flow\x18\x02 \x01(\x08\x12\x19\n\x11match_return_flow\x18\x03 \x01(\x08\x12\x35\n\x0bin_port_ids\x18\x04 \x03(\x0b\x32 .org.midonet.cluster.models.UUID\x12\x13\n\x0bin_port_inv\x18\x05 \x01(\x08\x12\x36\n\x0cout_port_ids\x18\x06 \x03(\x0b\x32 .org.midonet.cluster.models.UUID\x12\x14\n\x0cout_port_inv\x18\x07 \x01(\x08\x12\x37\n\rport_group_id\x18\x08 \x01(\x0b\x32 .org.midonet.cluster.models.UUID\x12\x16\n\x0einv_port_group\x18\t \x01(\x08\x12>\n\x14ip_addr_group_id_src\x18\n \x01(\x0b\x32 .org.midonet.cluster.models.UUID\x12 \n\x18inv_ip_addr_group_id_src\x18\x0b \x01(\x08\x12>\n\x14ip_addr_group_id_dst\x18\x0c \x01(\x0b\x32 .org.midonet.cluster.models.UUID\x12 \n\x18inv_ip_addr_group_id_dst\x18\r \x01(\x08\x12\x0f\n\x07\x64l_type\x18\x0e \x01(\x05\x12\x13\n\x0binv_dl_type\x18\x0f \x01(\x08\x12\x0e\n\x06\x64l_src\x18\x10 \x01(\t\x12\x17\n\x0b\x64l_src_mask\x18\x11 \x01(\x03:\x02-1\x12\x12\n\ninv_dl_src\x18\x12 \x01(\x08\x12\x0e\n\x06\x64l_dst\x18\x13 \x01(\t\x12\x17\n\x0b\x64l_dst_mask\x18\x14 \x01(\x03:\x02-1\x12\x12\n\ninv_dl_dst\x18\x15 \x01(\x08\x12\x0e\n\x06nw_tos\x18\x16 \x01(\x05\x12\x12\n\nnw_tos_inv\x18\x17 \x01(\x08\x12\x10\n\x08nw_proto\x18\x18 \x01(\x05\x12\x14\n\x0cnw_proto_inv\x18\x19 \x01(\x08\x12\x37\n\tnw_src_ip\x18\x1a \x01(\x0b\x32$.org.midonet.cluster.models.IPSubnet\x12\x37\n\tnw_dst_ip\x18\x1b \x01(\x0b\x32$.org.midonet.cluster.models.IPSubnet\x12\x36\n\x06tp_src\x18\x1c \x01(\x0b\x32&.org.midonet.cluster.models.Int32Range\x12\x36\n\x06tp_dst\x18\x1d \x01(\x0b\x32&.org.midonet.cluster.models.Int32Range\x12\x12\n\nnw_src_inv\x18\x1e \x01(\x08\x12\x12\n\nnw_dst_inv\x18\x1f \x01(\x08\x12\x12\n\ntp_src_inv\x18  \x01(\x08\x12\x12\n\ntp_dst_inv\x18! \x01(\x08\x12:\n\x10traversed_device\x18\" \x01(\x0b\x32 .org.midonet.cluster.models.UUID\x12\x1c\n\x14traversed_device_inv\x18# \x01(\x08\x12M\n\x0f\x66ragment_policy\x18$ \x01(\x0e\x32\x34.org.midonet.cluster.models.Condition.FragmentPolicy\x12\x0f\n\x07no_vlan\x18< \x01(\x08\x12\x0c\n\x04vlan\x18= \x01(\r\"F\n\x0e\x46ragmentPolicy\x12\x07\n\x03\x41NY\x10\x01\x12\r\n\tNONHEADER\x10\x02\x12\n\n\x06HEADER\x10\x03\x12\x10\n\x0cUNFRAGMENTED\x10\x04*\x1b\n\tIPVersion\x12\x06\n\x02V4\x10\x01\x12\x06\n\x02V6\x10\x02*(\n\rRuleDirection\x12\n\n\x06\x45GRESS\x10\x00\x12\x0b\n\x07INGRESS\x10\x01*,\n\tEtherType\x12\x08\n\x03\x41RP\x10\x86\x10\x12\t\n\x04IPV4\x10\x80\x10\x12\n\n\x04IPV6\x10\xdd\x8d\x02*2\n\x08Protocol\x12\x07\n\x03TCP\x10\x06\x12\x07\n\x03UDP\x10\x11\x12\x08\n\x04ICMP\x10\x01\x12\n\n\x06ICMPV6\x10:*$\n\x08LBStatus\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x42%\n\x1aorg.midonet.cluster.modelsB\x07\x43ommons')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_IPVERSION = _descriptor.EnumDescriptor(
  name='IPVersion',
  full_name='org.midonet.cluster.models.IPVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V4', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V6', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1654,
  serialized_end=1681,
)
_sym_db.RegisterEnumDescriptor(_IPVERSION)

IPVersion = enum_type_wrapper.EnumTypeWrapper(_IPVERSION)
_RULEDIRECTION = _descriptor.EnumDescriptor(
  name='RuleDirection',
  full_name='org.midonet.cluster.models.RuleDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EGRESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INGRESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1683,
  serialized_end=1723,
)
_sym_db.RegisterEnumDescriptor(_RULEDIRECTION)

RuleDirection = enum_type_wrapper.EnumTypeWrapper(_RULEDIRECTION)
_ETHERTYPE = _descriptor.EnumDescriptor(
  name='EtherType',
  full_name='org.midonet.cluster.models.EtherType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARP', index=0, number=2054,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV4', index=1, number=2048,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=2, number=34525,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1725,
  serialized_end=1769,
)
_sym_db.RegisterEnumDescriptor(_ETHERTYPE)

EtherType = enum_type_wrapper.EnumTypeWrapper(_ETHERTYPE)
_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='org.midonet.cluster.models.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TCP', index=0, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=1, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICMP', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICMPV6', index=3, number=58,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1771,
  serialized_end=1821,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOL)

Protocol = enum_type_wrapper.EnumTypeWrapper(_PROTOCOL)
_LBSTATUS = _descriptor.EnumDescriptor(
  name='LBStatus',
  full_name='org.midonet.cluster.models.LBStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1823,
  serialized_end=1859,
)
_sym_db.RegisterEnumDescriptor(_LBSTATUS)

LBStatus = enum_type_wrapper.EnumTypeWrapper(_LBSTATUS)
V4 = 1
V6 = 2
EGRESS = 0
INGRESS = 1
ARP = 2054
IPV4 = 2048
IPV6 = 34525
TCP = 6
UDP = 17
ICMP = 1
ICMPV6 = 58
ACTIVE = 1
INACTIVE = 2


_CONDITION_FRAGMENTPOLICY = _descriptor.EnumDescriptor(
  name='FragmentPolicy',
  full_name='org.midonet.cluster.models.Condition.FragmentPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONHEADER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNFRAGMENTED', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1582,
  serialized_end=1652,
)
_sym_db.RegisterEnumDescriptor(_CONDITION_FRAGMENTPOLICY)


_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='org.midonet.cluster.models.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msb', full_name='org.midonet.cluster.models.UUID.msb', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsb', full_name='org.midonet.cluster.models.UUID.lsb', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=77,
)


_IPADDRESS = _descriptor.Descriptor(
  name='IPAddress',
  full_name='org.midonet.cluster.models.IPAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='org.midonet.cluster.models.IPAddress.version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='org.midonet.cluster.models.IPAddress.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=163,
)


_IPSUBNET = _descriptor.Descriptor(
  name='IPSubnet',
  full_name='org.midonet.cluster.models.IPSubnet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='org.midonet.cluster.models.IPSubnet.version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='org.midonet.cluster.models.IPSubnet.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefix_length', full_name='org.midonet.cluster.models.IPSubnet.prefix_length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=271,
)


_INT32RANGE = _descriptor.Descriptor(
  name='Int32Range',
  full_name='org.midonet.cluster.models.Int32Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='org.midonet.cluster.models.Int32Range.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='org.midonet.cluster.models.Int32Range.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=313,
)


_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='org.midonet.cluster.models.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conjunction_inv', full_name='org.midonet.cluster.models.Condition.conjunction_inv', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_forward_flow', full_name='org.midonet.cluster.models.Condition.match_forward_flow', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_return_flow', full_name='org.midonet.cluster.models.Condition.match_return_flow', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_port_ids', full_name='org.midonet.cluster.models.Condition.in_port_ids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_port_inv', full_name='org.midonet.cluster.models.Condition.in_port_inv', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_port_ids', full_name='org.midonet.cluster.models.Condition.out_port_ids', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_port_inv', full_name='org.midonet.cluster.models.Condition.out_port_inv', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_group_id', full_name='org.midonet.cluster.models.Condition.port_group_id', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inv_port_group', full_name='org.midonet.cluster.models.Condition.inv_port_group', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_addr_group_id_src', full_name='org.midonet.cluster.models.Condition.ip_addr_group_id_src', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inv_ip_addr_group_id_src', full_name='org.midonet.cluster.models.Condition.inv_ip_addr_group_id_src', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_addr_group_id_dst', full_name='org.midonet.cluster.models.Condition.ip_addr_group_id_dst', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inv_ip_addr_group_id_dst', full_name='org.midonet.cluster.models.Condition.inv_ip_addr_group_id_dst', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_type', full_name='org.midonet.cluster.models.Condition.dl_type', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inv_dl_type', full_name='org.midonet.cluster.models.Condition.inv_dl_type', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_src', full_name='org.midonet.cluster.models.Condition.dl_src', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_src_mask', full_name='org.midonet.cluster.models.Condition.dl_src_mask', index=16,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inv_dl_src', full_name='org.midonet.cluster.models.Condition.inv_dl_src', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_dst', full_name='org.midonet.cluster.models.Condition.dl_dst', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_dst_mask', full_name='org.midonet.cluster.models.Condition.dl_dst_mask', index=19,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inv_dl_dst', full_name='org.midonet.cluster.models.Condition.inv_dl_dst', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_tos', full_name='org.midonet.cluster.models.Condition.nw_tos', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_tos_inv', full_name='org.midonet.cluster.models.Condition.nw_tos_inv', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_proto', full_name='org.midonet.cluster.models.Condition.nw_proto', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_proto_inv', full_name='org.midonet.cluster.models.Condition.nw_proto_inv', index=24,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_src_ip', full_name='org.midonet.cluster.models.Condition.nw_src_ip', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_dst_ip', full_name='org.midonet.cluster.models.Condition.nw_dst_ip', index=26,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp_src', full_name='org.midonet.cluster.models.Condition.tp_src', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp_dst', full_name='org.midonet.cluster.models.Condition.tp_dst', index=28,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_src_inv', full_name='org.midonet.cluster.models.Condition.nw_src_inv', index=29,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nw_dst_inv', full_name='org.midonet.cluster.models.Condition.nw_dst_inv', index=30,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp_src_inv', full_name='org.midonet.cluster.models.Condition.tp_src_inv', index=31,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp_dst_inv', full_name='org.midonet.cluster.models.Condition.tp_dst_inv', index=32,
      number=33, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traversed_device', full_name='org.midonet.cluster.models.Condition.traversed_device', index=33,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traversed_device_inv', full_name='org.midonet.cluster.models.Condition.traversed_device_inv', index=34,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fragment_policy', full_name='org.midonet.cluster.models.Condition.fragment_policy', index=35,
      number=36, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_vlan', full_name='org.midonet.cluster.models.Condition.no_vlan', index=36,
      number=60, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vlan', full_name='org.midonet.cluster.models.Condition.vlan', index=37,
      number=61, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONDITION_FRAGMENTPOLICY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=1652,
)

_IPADDRESS.fields_by_name['version'].enum_type = _IPVERSION
_IPSUBNET.fields_by_name['version'].enum_type = _IPVERSION
_CONDITION.fields_by_name['in_port_ids'].message_type = _UUID
_CONDITION.fields_by_name['out_port_ids'].message_type = _UUID
_CONDITION.fields_by_name['port_group_id'].message_type = _UUID
_CONDITION.fields_by_name['ip_addr_group_id_src'].message_type = _UUID
_CONDITION.fields_by_name['ip_addr_group_id_dst'].message_type = _UUID
_CONDITION.fields_by_name['nw_src_ip'].message_type = _IPSUBNET
_CONDITION.fields_by_name['nw_dst_ip'].message_type = _IPSUBNET
_CONDITION.fields_by_name['tp_src'].message_type = _INT32RANGE
_CONDITION.fields_by_name['tp_dst'].message_type = _INT32RANGE
_CONDITION.fields_by_name['traversed_device'].message_type = _UUID
_CONDITION.fields_by_name['fragment_policy'].enum_type = _CONDITION_FRAGMENTPOLICY
_CONDITION_FRAGMENTPOLICY.containing_type = _CONDITION
DESCRIPTOR.message_types_by_name['UUID'] = _UUID
DESCRIPTOR.message_types_by_name['IPAddress'] = _IPADDRESS
DESCRIPTOR.message_types_by_name['IPSubnet'] = _IPSUBNET
DESCRIPTOR.message_types_by_name['Int32Range'] = _INT32RANGE
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
DESCRIPTOR.enum_types_by_name['IPVersion'] = _IPVERSION
DESCRIPTOR.enum_types_by_name['RuleDirection'] = _RULEDIRECTION
DESCRIPTOR.enum_types_by_name['EtherType'] = _ETHERTYPE
DESCRIPTOR.enum_types_by_name['Protocol'] = _PROTOCOL
DESCRIPTOR.enum_types_by_name['LBStatus'] = _LBSTATUS

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), dict(
  DESCRIPTOR = _UUID,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:org.midonet.cluster.models.UUID)
  ))
_sym_db.RegisterMessage(UUID)

IPAddress = _reflection.GeneratedProtocolMessageType('IPAddress', (_message.Message,), dict(
  DESCRIPTOR = _IPADDRESS,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:org.midonet.cluster.models.IPAddress)
  ))
_sym_db.RegisterMessage(IPAddress)

IPSubnet = _reflection.GeneratedProtocolMessageType('IPSubnet', (_message.Message,), dict(
  DESCRIPTOR = _IPSUBNET,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:org.midonet.cluster.models.IPSubnet)
  ))
_sym_db.RegisterMessage(IPSubnet)

Int32Range = _reflection.GeneratedProtocolMessageType('Int32Range', (_message.Message,), dict(
  DESCRIPTOR = _INT32RANGE,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:org.midonet.cluster.models.Int32Range)
  ))
_sym_db.RegisterMessage(Int32Range)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), dict(
  DESCRIPTOR = _CONDITION,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:org.midonet.cluster.models.Condition)
  ))
_sym_db.RegisterMessage(Condition)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032org.midonet.cluster.modelsB\007Commons'))
# @@protoc_insertion_point(module_scope)
