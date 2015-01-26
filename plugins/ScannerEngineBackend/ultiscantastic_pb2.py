# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ultiscantastic.proto

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
  name='ultiscantastic.proto',
  package='ScannerBuff',
  serialized_pb=_b('\n\x14ultiscantastic.proto\x12\x0bScannerBuff\"F\n\x15PointCloudWithNormals\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\x12\x0f\n\x07normals\x18\x03 \x01(\x0c\"8\n\x18PointCloudWithoutNormals\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\"1\n\x15PointCloudPointNormal\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"2\n\x0eProgressUpdate\x12\x10\n\x08objectId\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"F\n\x04Mesh\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\x12\x0f\n\x07normals\x18\x03 \x01(\x0c\x12\x0f\n\x07indices\x18\x04 \x01(\x0c\"y\n\x10StartCalibration\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.ScannerBuff.StartCalibration.CalibrationType\"(\n\x0f\x43\x61librationType\x12\n\n\x06\x43ORNER\x10\x00\x12\t\n\x05\x42OARD\x10\x01\"[\n\tStartScan\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.ScannerBuff.StartScan.ScanType\"\x1f\n\x08ScanType\x12\x08\n\x04GREY\x10\x00\x12\t\n\x05PHASE\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STARTCALIBRATION_CALIBRATIONTYPE = _descriptor.EnumDescriptor(
  name='CalibrationType',
  full_name='ScannerBuff.StartCalibration.CalibrationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CORNER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOARD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=423,
  serialized_end=463,
)
_sym_db.RegisterEnumDescriptor(_STARTCALIBRATION_CALIBRATIONTYPE)

_STARTSCAN_SCANTYPE = _descriptor.EnumDescriptor(
  name='ScanType',
  full_name='ScannerBuff.StartScan.ScanType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GREY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHASE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=525,
  serialized_end=556,
)
_sym_db.RegisterEnumDescriptor(_STARTSCAN_SCANTYPE)


_POINTCLOUDWITHNORMALS = _descriptor.Descriptor(
  name='PointCloudWithNormals',
  full_name='ScannerBuff.PointCloudWithNormals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.PointCloudWithNormals.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='ScannerBuff.PointCloudWithNormals.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normals', full_name='ScannerBuff.PointCloudWithNormals.normals', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=37,
  serialized_end=107,
)


_POINTCLOUDWITHOUTNORMALS = _descriptor.Descriptor(
  name='PointCloudWithoutNormals',
  full_name='ScannerBuff.PointCloudWithoutNormals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.PointCloudWithoutNormals.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='ScannerBuff.PointCloudWithoutNormals.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=109,
  serialized_end=165,
)


_POINTCLOUDPOINTNORMAL = _descriptor.Descriptor(
  name='PointCloudPointNormal',
  full_name='ScannerBuff.PointCloudPointNormal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.PointCloudPointNormal.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='ScannerBuff.PointCloudPointNormal.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=167,
  serialized_end=216,
)


_PROGRESSUPDATE = _descriptor.Descriptor(
  name='ProgressUpdate',
  full_name='ScannerBuff.ProgressUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='ScannerBuff.ProgressUpdate.objectId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ScannerBuff.ProgressUpdate.amount', index=1,
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
  serialized_start=218,
  serialized_end=268,
)


_MESH = _descriptor.Descriptor(
  name='Mesh',
  full_name='ScannerBuff.Mesh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.Mesh.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='ScannerBuff.Mesh.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normals', full_name='ScannerBuff.Mesh.normals', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indices', full_name='ScannerBuff.Mesh.indices', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=270,
  serialized_end=340,
)


_STARTCALIBRATION = _descriptor.Descriptor(
  name='StartCalibration',
  full_name='ScannerBuff.StartCalibration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ScannerBuff.StartCalibration.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STARTCALIBRATION_CALIBRATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=463,
)


_STARTSCAN = _descriptor.Descriptor(
  name='StartScan',
  full_name='ScannerBuff.StartScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ScannerBuff.StartScan.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STARTSCAN_SCANTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=556,
)

_STARTCALIBRATION.fields_by_name['type'].enum_type = _STARTCALIBRATION_CALIBRATIONTYPE
_STARTCALIBRATION_CALIBRATIONTYPE.containing_type = _STARTCALIBRATION
_STARTSCAN.fields_by_name['type'].enum_type = _STARTSCAN_SCANTYPE
_STARTSCAN_SCANTYPE.containing_type = _STARTSCAN
DESCRIPTOR.message_types_by_name['PointCloudWithNormals'] = _POINTCLOUDWITHNORMALS
DESCRIPTOR.message_types_by_name['PointCloudWithoutNormals'] = _POINTCLOUDWITHOUTNORMALS
DESCRIPTOR.message_types_by_name['PointCloudPointNormal'] = _POINTCLOUDPOINTNORMAL
DESCRIPTOR.message_types_by_name['ProgressUpdate'] = _PROGRESSUPDATE
DESCRIPTOR.message_types_by_name['Mesh'] = _MESH
DESCRIPTOR.message_types_by_name['StartCalibration'] = _STARTCALIBRATION
DESCRIPTOR.message_types_by_name['StartScan'] = _STARTSCAN

PointCloudWithNormals = _reflection.GeneratedProtocolMessageType('PointCloudWithNormals', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDWITHNORMALS,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.PointCloudWithNormals)
  ))
_sym_db.RegisterMessage(PointCloudWithNormals)

PointCloudWithoutNormals = _reflection.GeneratedProtocolMessageType('PointCloudWithoutNormals', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDWITHOUTNORMALS,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.PointCloudWithoutNormals)
  ))
_sym_db.RegisterMessage(PointCloudWithoutNormals)

PointCloudPointNormal = _reflection.GeneratedProtocolMessageType('PointCloudPointNormal', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDPOINTNORMAL,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.PointCloudPointNormal)
  ))
_sym_db.RegisterMessage(PointCloudPointNormal)

ProgressUpdate = _reflection.GeneratedProtocolMessageType('ProgressUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PROGRESSUPDATE,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.ProgressUpdate)
  ))
_sym_db.RegisterMessage(ProgressUpdate)

Mesh = _reflection.GeneratedProtocolMessageType('Mesh', (_message.Message,), dict(
  DESCRIPTOR = _MESH,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.Mesh)
  ))
_sym_db.RegisterMessage(Mesh)

StartCalibration = _reflection.GeneratedProtocolMessageType('StartCalibration', (_message.Message,), dict(
  DESCRIPTOR = _STARTCALIBRATION,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.StartCalibration)
  ))
_sym_db.RegisterMessage(StartCalibration)

StartScan = _reflection.GeneratedProtocolMessageType('StartScan', (_message.Message,), dict(
  DESCRIPTOR = _STARTSCAN,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.StartScan)
  ))
_sym_db.RegisterMessage(StartScan)


# @@protoc_insertion_point(module_scope)
