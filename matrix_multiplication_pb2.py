# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: matrix_multiplication.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'matrix_multiplication.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmatrix_multiplication.proto\">\n\nMatrixPair\x12\x10\n\x08matrix_a\x18\x01 \x03(\x02\x12\x10\n\x08matrix_b\x18\x02 \x03(\x02\x12\x0c\n\x04size\x18\x03 \x01(\x05\"\x1e\n\x0cMatrixResult\x12\x0e\n\x06result\x18\x01 \x03(\x02\x32@\n\x14MatrixMultiplication\x12(\n\x08Multiply\x12\x0b.MatrixPair\x1a\r.MatrixResult\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'matrix_multiplication_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MATRIXPAIR']._serialized_start=31
  _globals['_MATRIXPAIR']._serialized_end=93
  _globals['_MATRIXRESULT']._serialized_start=95
  _globals['_MATRIXRESULT']._serialized_end=125
  _globals['_MATRIXMULTIPLICATION']._serialized_start=127
  _globals['_MATRIXMULTIPLICATION']._serialized_end=191
# @@protoc_insertion_point(module_scope)
