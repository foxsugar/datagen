# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: static_data_proto.proto

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
  name='static_data_proto.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x17static_data_proto.proto\"\xa3\x05\n\x0b\x44\x61taManager\x12\x38\n\x0epaijiuCardData\x18\x01 \x03(\x0b\x32 .DataManager.PaijiuCardDataEntry\x12\x42\n\x13paijiuCardGroupData\x18\x02 \x03(\x0b\x32%.DataManager.PaijiuCardGroupDataEntry\x12L\n\x18paijiuCardGroupScoreData\x18\x03 \x03(\x0b\x32*.DataManager.PaijiuCardGroupScoreDataEntry\x12,\n\x08roomData\x18\x04 \x03(\x0b\x32\x1a.DataManager.RoomDataEntry\x12,\n\x08testData\x18\x05 \x03(\x0b\x32\x1a.DataManager.TestDataEntry\x1a\x46\n\x13PaijiuCardDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.PaijiuCardData:\x02\x38\x01\x1aP\n\x18PaijiuCardGroupDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.PaijiuCardGroupData:\x02\x38\x01\x1aZ\n\x1dPaijiuCardGroupScoreDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.PaijiuCardGroupScoreData:\x02\x38\x01\x1a:\n\rRoomDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.RoomData:\x02\x38\x01\x1a:\n\rTestDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.TestData:\x02\x38\x01\"*\n\x0ePaijiuCardData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63\x61rd\x18\x02 \x01(\x05\"/\n\x13PaijiuCardGroupData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"5\n\x18PaijiuCardGroupScoreData\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"\xdb\x01\n\x08RoomData\x12\n\n\x02id\x18\x01 \x01(\x05\x12#\n\x05money\x18\x02 \x03(\x0b\x32\x14.RoomData.MoneyEntry\x12+\n\teachMoney\x18\x03 \x03(\x0b\x32\x18.RoomData.EachMoneyEntry\x12\x11\n\tisAddGold\x18\x04 \x01(\x05\x1a,\n\nMoneyEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x30\n\x0e\x45\x61\x63hMoneyEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xbd\x02\n\x08TestData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x04 \x03(\x05\x12%\n\x06weapon\x18\x05 \x03(\x0b\x32\x15.TestData.WeaponEntry\x12\x10\n\x08testLong\x18\x06 \x01(\x03\x12\x12\n\ntestDouble\x18\x07 \x01(\x01\x12\x16\n\x0etestListDouble\x18\x08 \x03(\x01\x12\x33\n\rtestMapDouble\x18\t \x03(\x0b\x32\x1c.TestData.TestMapDoubleEntry\x1a-\n\x0bWeaponEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12TestMapDoubleEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x42?\n\x1d\x63om.code.server.constant.dataB\x0fStaticDataProto\xaa\x02\x0c\x63om.bsl.datab\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DATAMANAGER_PAIJIUCARDDATAENTRY = _descriptor.Descriptor(
  name='PaijiuCardDataEntry',
  full_name='DataManager.PaijiuCardDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataManager.PaijiuCardDataEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataManager.PaijiuCardDataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=409,
)

_DATAMANAGER_PAIJIUCARDGROUPDATAENTRY = _descriptor.Descriptor(
  name='PaijiuCardGroupDataEntry',
  full_name='DataManager.PaijiuCardGroupDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataManager.PaijiuCardGroupDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataManager.PaijiuCardGroupDataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=491,
)

_DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY = _descriptor.Descriptor(
  name='PaijiuCardGroupScoreDataEntry',
  full_name='DataManager.PaijiuCardGroupScoreDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataManager.PaijiuCardGroupScoreDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataManager.PaijiuCardGroupScoreDataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=583,
)

_DATAMANAGER_ROOMDATAENTRY = _descriptor.Descriptor(
  name='RoomDataEntry',
  full_name='DataManager.RoomDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataManager.RoomDataEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataManager.RoomDataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=643,
)

_DATAMANAGER_TESTDATAENTRY = _descriptor.Descriptor(
  name='TestDataEntry',
  full_name='DataManager.TestDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataManager.TestDataEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataManager.TestDataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=645,
  serialized_end=703,
)

_DATAMANAGER = _descriptor.Descriptor(
  name='DataManager',
  full_name='DataManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paijiuCardData', full_name='DataManager.paijiuCardData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paijiuCardGroupData', full_name='DataManager.paijiuCardGroupData', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paijiuCardGroupScoreData', full_name='DataManager.paijiuCardGroupScoreData', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roomData', full_name='DataManager.roomData', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testData', full_name='DataManager.testData', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATAMANAGER_PAIJIUCARDDATAENTRY, _DATAMANAGER_PAIJIUCARDGROUPDATAENTRY, _DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY, _DATAMANAGER_ROOMDATAENTRY, _DATAMANAGER_TESTDATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=703,
)


_PAIJIUCARDDATA = _descriptor.Descriptor(
  name='PaijiuCardData',
  full_name='PaijiuCardData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PaijiuCardData.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card', full_name='PaijiuCardData.card', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=747,
)


_PAIJIUCARDGROUPDATA = _descriptor.Descriptor(
  name='PaijiuCardGroupData',
  full_name='PaijiuCardGroupData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PaijiuCardGroupData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='PaijiuCardGroupData.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=749,
  serialized_end=796,
)


_PAIJIUCARDGROUPSCOREDATA = _descriptor.Descriptor(
  name='PaijiuCardGroupScoreData',
  full_name='PaijiuCardGroupScoreData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PaijiuCardGroupScoreData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='PaijiuCardGroupScoreData.score', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=798,
  serialized_end=851,
)


_ROOMDATA_MONEYENTRY = _descriptor.Descriptor(
  name='MoneyEntry',
  full_name='RoomData.MoneyEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='RoomData.MoneyEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='RoomData.MoneyEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=979,
  serialized_end=1023,
)

_ROOMDATA_EACHMONEYENTRY = _descriptor.Descriptor(
  name='EachMoneyEntry',
  full_name='RoomData.EachMoneyEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='RoomData.EachMoneyEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='RoomData.EachMoneyEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1025,
  serialized_end=1073,
)

_ROOMDATA = _descriptor.Descriptor(
  name='RoomData',
  full_name='RoomData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RoomData.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money', full_name='RoomData.money', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eachMoney', full_name='RoomData.eachMoney', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isAddGold', full_name='RoomData.isAddGold', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROOMDATA_MONEYENTRY, _ROOMDATA_EACHMONEYENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=1073,
)


_TESTDATA_WEAPONENTRY = _descriptor.Descriptor(
  name='WeaponEntry',
  full_name='TestData.WeaponEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TestData.WeaponEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='TestData.WeaponEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1294,
  serialized_end=1339,
)

_TESTDATA_TESTMAPDOUBLEENTRY = _descriptor.Descriptor(
  name='TestMapDoubleEntry',
  full_name='TestData.TestMapDoubleEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TestData.TestMapDoubleEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='TestData.TestMapDoubleEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1341,
  serialized_end=1393,
)

_TESTDATA = _descriptor.Descriptor(
  name='TestData',
  full_name='TestData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TestData.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='TestData.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age', full_name='TestData.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='TestData.exp', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weapon', full_name='TestData.weapon', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testLong', full_name='TestData.testLong', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testDouble', full_name='TestData.testDouble', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testListDouble', full_name='TestData.testListDouble', index=7,
      number=8, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testMapDouble', full_name='TestData.testMapDouble', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTDATA_WEAPONENTRY, _TESTDATA_TESTMAPDOUBLEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1393,
)

_DATAMANAGER_PAIJIUCARDDATAENTRY.fields_by_name['value'].message_type = _PAIJIUCARDDATA
_DATAMANAGER_PAIJIUCARDDATAENTRY.containing_type = _DATAMANAGER
_DATAMANAGER_PAIJIUCARDGROUPDATAENTRY.fields_by_name['value'].message_type = _PAIJIUCARDGROUPDATA
_DATAMANAGER_PAIJIUCARDGROUPDATAENTRY.containing_type = _DATAMANAGER
_DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY.fields_by_name['value'].message_type = _PAIJIUCARDGROUPSCOREDATA
_DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY.containing_type = _DATAMANAGER
_DATAMANAGER_ROOMDATAENTRY.fields_by_name['value'].message_type = _ROOMDATA
_DATAMANAGER_ROOMDATAENTRY.containing_type = _DATAMANAGER
_DATAMANAGER_TESTDATAENTRY.fields_by_name['value'].message_type = _TESTDATA
_DATAMANAGER_TESTDATAENTRY.containing_type = _DATAMANAGER
_DATAMANAGER.fields_by_name['paijiuCardData'].message_type = _DATAMANAGER_PAIJIUCARDDATAENTRY
_DATAMANAGER.fields_by_name['paijiuCardGroupData'].message_type = _DATAMANAGER_PAIJIUCARDGROUPDATAENTRY
_DATAMANAGER.fields_by_name['paijiuCardGroupScoreData'].message_type = _DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY
_DATAMANAGER.fields_by_name['roomData'].message_type = _DATAMANAGER_ROOMDATAENTRY
_DATAMANAGER.fields_by_name['testData'].message_type = _DATAMANAGER_TESTDATAENTRY
_ROOMDATA_MONEYENTRY.containing_type = _ROOMDATA
_ROOMDATA_EACHMONEYENTRY.containing_type = _ROOMDATA
_ROOMDATA.fields_by_name['money'].message_type = _ROOMDATA_MONEYENTRY
_ROOMDATA.fields_by_name['eachMoney'].message_type = _ROOMDATA_EACHMONEYENTRY
_TESTDATA_WEAPONENTRY.containing_type = _TESTDATA
_TESTDATA_TESTMAPDOUBLEENTRY.containing_type = _TESTDATA
_TESTDATA.fields_by_name['weapon'].message_type = _TESTDATA_WEAPONENTRY
_TESTDATA.fields_by_name['testMapDouble'].message_type = _TESTDATA_TESTMAPDOUBLEENTRY
DESCRIPTOR.message_types_by_name['DataManager'] = _DATAMANAGER
DESCRIPTOR.message_types_by_name['PaijiuCardData'] = _PAIJIUCARDDATA
DESCRIPTOR.message_types_by_name['PaijiuCardGroupData'] = _PAIJIUCARDGROUPDATA
DESCRIPTOR.message_types_by_name['PaijiuCardGroupScoreData'] = _PAIJIUCARDGROUPSCOREDATA
DESCRIPTOR.message_types_by_name['RoomData'] = _ROOMDATA
DESCRIPTOR.message_types_by_name['TestData'] = _TESTDATA

DataManager = _reflection.GeneratedProtocolMessageType('DataManager', (_message.Message,), dict(

  PaijiuCardDataEntry = _reflection.GeneratedProtocolMessageType('PaijiuCardDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAMANAGER_PAIJIUCARDDATAENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:DataManager.PaijiuCardDataEntry)
    ))
  ,

  PaijiuCardGroupDataEntry = _reflection.GeneratedProtocolMessageType('PaijiuCardGroupDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAMANAGER_PAIJIUCARDGROUPDATAENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:DataManager.PaijiuCardGroupDataEntry)
    ))
  ,

  PaijiuCardGroupScoreDataEntry = _reflection.GeneratedProtocolMessageType('PaijiuCardGroupScoreDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:DataManager.PaijiuCardGroupScoreDataEntry)
    ))
  ,

  RoomDataEntry = _reflection.GeneratedProtocolMessageType('RoomDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAMANAGER_ROOMDATAENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:DataManager.RoomDataEntry)
    ))
  ,

  TestDataEntry = _reflection.GeneratedProtocolMessageType('TestDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAMANAGER_TESTDATAENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:DataManager.TestDataEntry)
    ))
  ,
  DESCRIPTOR = _DATAMANAGER,
  __module__ = 'static_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:DataManager)
  ))
_sym_db.RegisterMessage(DataManager)
_sym_db.RegisterMessage(DataManager.PaijiuCardDataEntry)
_sym_db.RegisterMessage(DataManager.PaijiuCardGroupDataEntry)
_sym_db.RegisterMessage(DataManager.PaijiuCardGroupScoreDataEntry)
_sym_db.RegisterMessage(DataManager.RoomDataEntry)
_sym_db.RegisterMessage(DataManager.TestDataEntry)

PaijiuCardData = _reflection.GeneratedProtocolMessageType('PaijiuCardData', (_message.Message,), dict(
  DESCRIPTOR = _PAIJIUCARDDATA,
  __module__ = 'static_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:PaijiuCardData)
  ))
_sym_db.RegisterMessage(PaijiuCardData)

PaijiuCardGroupData = _reflection.GeneratedProtocolMessageType('PaijiuCardGroupData', (_message.Message,), dict(
  DESCRIPTOR = _PAIJIUCARDGROUPDATA,
  __module__ = 'static_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:PaijiuCardGroupData)
  ))
_sym_db.RegisterMessage(PaijiuCardGroupData)

PaijiuCardGroupScoreData = _reflection.GeneratedProtocolMessageType('PaijiuCardGroupScoreData', (_message.Message,), dict(
  DESCRIPTOR = _PAIJIUCARDGROUPSCOREDATA,
  __module__ = 'static_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:PaijiuCardGroupScoreData)
  ))
_sym_db.RegisterMessage(PaijiuCardGroupScoreData)

RoomData = _reflection.GeneratedProtocolMessageType('RoomData', (_message.Message,), dict(

  MoneyEntry = _reflection.GeneratedProtocolMessageType('MoneyEntry', (_message.Message,), dict(
    DESCRIPTOR = _ROOMDATA_MONEYENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:RoomData.MoneyEntry)
    ))
  ,

  EachMoneyEntry = _reflection.GeneratedProtocolMessageType('EachMoneyEntry', (_message.Message,), dict(
    DESCRIPTOR = _ROOMDATA_EACHMONEYENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:RoomData.EachMoneyEntry)
    ))
  ,
  DESCRIPTOR = _ROOMDATA,
  __module__ = 'static_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:RoomData)
  ))
_sym_db.RegisterMessage(RoomData)
_sym_db.RegisterMessage(RoomData.MoneyEntry)
_sym_db.RegisterMessage(RoomData.EachMoneyEntry)

TestData = _reflection.GeneratedProtocolMessageType('TestData', (_message.Message,), dict(

  WeaponEntry = _reflection.GeneratedProtocolMessageType('WeaponEntry', (_message.Message,), dict(
    DESCRIPTOR = _TESTDATA_WEAPONENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:TestData.WeaponEntry)
    ))
  ,

  TestMapDoubleEntry = _reflection.GeneratedProtocolMessageType('TestMapDoubleEntry', (_message.Message,), dict(
    DESCRIPTOR = _TESTDATA_TESTMAPDOUBLEENTRY,
    __module__ = 'static_data_proto_pb2'
    # @@protoc_insertion_point(class_scope:TestData.TestMapDoubleEntry)
    ))
  ,
  DESCRIPTOR = _TESTDATA,
  __module__ = 'static_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:TestData)
  ))
_sym_db.RegisterMessage(TestData)
_sym_db.RegisterMessage(TestData.WeaponEntry)
_sym_db.RegisterMessage(TestData.TestMapDoubleEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035com.code.server.constant.dataB\017StaticDataProto\252\002\014com.bsl.data'))
_DATAMANAGER_PAIJIUCARDDATAENTRY.has_options = True
_DATAMANAGER_PAIJIUCARDDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAMANAGER_PAIJIUCARDGROUPDATAENTRY.has_options = True
_DATAMANAGER_PAIJIUCARDGROUPDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY.has_options = True
_DATAMANAGER_PAIJIUCARDGROUPSCOREDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAMANAGER_ROOMDATAENTRY.has_options = True
_DATAMANAGER_ROOMDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAMANAGER_TESTDATAENTRY.has_options = True
_DATAMANAGER_TESTDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ROOMDATA_MONEYENTRY.has_options = True
_ROOMDATA_MONEYENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ROOMDATA_EACHMONEYENTRY.has_options = True
_ROOMDATA_EACHMONEYENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_TESTDATA_WEAPONENTRY.has_options = True
_TESTDATA_WEAPONENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_TESTDATA_TESTMAPDOUBLEENTRY.has_options = True
_TESTDATA_TESTMAPDOUBLEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
