# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: conf.proto

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
  name='conf.proto',
  package='imcl',
  serialized_pb=_b('\n\nconf.proto\x12\x04imcl\"_\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x12\n\ngold_label\x18\x02 \x01(\x05\x12\x12\n\ngold_score\x18\x03 \x01(\x02\x12\x0c\n\x04pred\x18\x04 \x01(\x05\x12\x13\n\x0bprobability\x18\x05 \x01(\x02\"2\n\x08\x46ileList\x12\x0c\n\x04root\x18\x01 \x01(\x0c\x12\x18\n\x04\x66ile\x18\x02 \x03(\x0b\x32\n.imcl.File\"$\n\x06\x46older\x12\x0b\n\x03\x64ir\x18\x01 \x01(\x0c\x12\r\n\x05label\x18\x02 \x01(\x05\"8\n\nFolderList\x12\x0c\n\x04root\x18\x01 \x01(\x0c\x12\x1c\n\x06\x66older\x18\x02 \x03(\x0b\x32\x0c.imcl.Folder\"\x9b\x02\n\tAppConfig\x12\x0c\n\x04root\x18\x01 \x01(\x0c\x12$\n\nfolderlist\x18\x02 \x01(\x0b\x32\x10.imcl.FolderList\x12 \n\x08\x66ilelist\x18\x03 \x01(\x0b\x32\x0e.imcl.FileList\x12\x11\n\tcore_file\x18\x04 \x01(\x0c\x12\x0e\n\x06repeat\x18\x05 \x01(\x05\x12\x13\n\x0bvideo_begin\x18\x06 \x01(\x05\x12\x11\n\tvideo_num\x18\x07 \x01(\x05\x12\x12\n\nvideo_step\x18\x08 \x01(\x05\x12\x11\n\tvideo_dir\x18\t \x01(\x0c\x12\x11\n\timage_dir\x18\n \x01(\x0c\x12\x0b\n\x03\x61pp\x18\x0b \x01(\x05\x12\x11\n\tgold_file\x18\x0c \x01(\x0c\x12\x13\n\x0bresult_file\x18\r \x01(\x0c\"_\n\nCoreConfig\x12\r\n\x05model\x18\x02 \x01(\x0c\x12\x11\n\tparameter\x18\x03 \x01(\x0c\x12\x12\n\nmean_image\x18\x04 \x01(\x0c\x12\r\n\x05scale\x18\x01 \x01(\x08\x12\x0c\n\x04\x63rop\x18\x05 \x01(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FILE = _descriptor.Descriptor(
  name='File',
  full_name='imcl.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='imcl.File.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_label', full_name='imcl.File.gold_label', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_score', full_name='imcl.File.gold_score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pred', full_name='imcl.File.pred', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probability', full_name='imcl.File.probability', index=4,
      number=5, type=2, cpp_type=6, label=1,
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
  serialized_start=20,
  serialized_end=115,
)


_FILELIST = _descriptor.Descriptor(
  name='FileList',
  full_name='imcl.FileList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='imcl.FileList.root', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='imcl.FileList.file', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=117,
  serialized_end=167,
)


_FOLDER = _descriptor.Descriptor(
  name='Folder',
  full_name='imcl.Folder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dir', full_name='imcl.Folder.dir', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='imcl.Folder.label', index=1,
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
  serialized_start=169,
  serialized_end=205,
)


_FOLDERLIST = _descriptor.Descriptor(
  name='FolderList',
  full_name='imcl.FolderList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='imcl.FolderList.root', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='folder', full_name='imcl.FolderList.folder', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=207,
  serialized_end=263,
)


_APPCONFIG = _descriptor.Descriptor(
  name='AppConfig',
  full_name='imcl.AppConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='imcl.AppConfig.root', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='folderlist', full_name='imcl.AppConfig.folderlist', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filelist', full_name='imcl.AppConfig.filelist', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='core_file', full_name='imcl.AppConfig.core_file', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat', full_name='imcl.AppConfig.repeat', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_begin', full_name='imcl.AppConfig.video_begin', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_num', full_name='imcl.AppConfig.video_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_step', full_name='imcl.AppConfig.video_step', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_dir', full_name='imcl.AppConfig.video_dir', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_dir', full_name='imcl.AppConfig.image_dir', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app', full_name='imcl.AppConfig.app', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_file', full_name='imcl.AppConfig.gold_file', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_file', full_name='imcl.AppConfig.result_file', index=12,
      number=13, type=12, cpp_type=9, label=1,
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
  serialized_start=266,
  serialized_end=549,
)


_CORECONFIG = _descriptor.Descriptor(
  name='CoreConfig',
  full_name='imcl.CoreConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='imcl.CoreConfig.model', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='imcl.CoreConfig.parameter', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_image', full_name='imcl.CoreConfig.mean_image', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='imcl.CoreConfig.scale', index=3,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop', full_name='imcl.CoreConfig.crop', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=551,
  serialized_end=646,
)

_FILELIST.fields_by_name['file'].message_type = _FILE
_FOLDERLIST.fields_by_name['folder'].message_type = _FOLDER
_APPCONFIG.fields_by_name['folderlist'].message_type = _FOLDERLIST
_APPCONFIG.fields_by_name['filelist'].message_type = _FILELIST
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['FileList'] = _FILELIST
DESCRIPTOR.message_types_by_name['Folder'] = _FOLDER
DESCRIPTOR.message_types_by_name['FolderList'] = _FOLDERLIST
DESCRIPTOR.message_types_by_name['AppConfig'] = _APPCONFIG
DESCRIPTOR.message_types_by_name['CoreConfig'] = _CORECONFIG

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'conf_pb2'
  # @@protoc_insertion_point(class_scope:imcl.File)
  ))
_sym_db.RegisterMessage(File)

FileList = _reflection.GeneratedProtocolMessageType('FileList', (_message.Message,), dict(
  DESCRIPTOR = _FILELIST,
  __module__ = 'conf_pb2'
  # @@protoc_insertion_point(class_scope:imcl.FileList)
  ))
_sym_db.RegisterMessage(FileList)

Folder = _reflection.GeneratedProtocolMessageType('Folder', (_message.Message,), dict(
  DESCRIPTOR = _FOLDER,
  __module__ = 'conf_pb2'
  # @@protoc_insertion_point(class_scope:imcl.Folder)
  ))
_sym_db.RegisterMessage(Folder)

FolderList = _reflection.GeneratedProtocolMessageType('FolderList', (_message.Message,), dict(
  DESCRIPTOR = _FOLDERLIST,
  __module__ = 'conf_pb2'
  # @@protoc_insertion_point(class_scope:imcl.FolderList)
  ))
_sym_db.RegisterMessage(FolderList)

AppConfig = _reflection.GeneratedProtocolMessageType('AppConfig', (_message.Message,), dict(
  DESCRIPTOR = _APPCONFIG,
  __module__ = 'conf_pb2'
  # @@protoc_insertion_point(class_scope:imcl.AppConfig)
  ))
_sym_db.RegisterMessage(AppConfig)

CoreConfig = _reflection.GeneratedProtocolMessageType('CoreConfig', (_message.Message,), dict(
  DESCRIPTOR = _CORECONFIG,
  __module__ = 'conf_pb2'
  # @@protoc_insertion_point(class_scope:imcl.CoreConfig)
  ))
_sym_db.RegisterMessage(CoreConfig)


# @@protoc_insertion_point(module_scope)
