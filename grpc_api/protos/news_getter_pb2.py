# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: news_getter.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11news_getter.proto\x12\x0bnews_getter\x1a\x1egoogle/protobuf/wrappers.proto\"\\\n\x11SearchNewsRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12 \n\x05sites\x18\x02 \x03(\x0e\x32\x11.news_getter.Site\x12\x16\n\x0emax_site_links\x18\x03 \x01(\x05\"#\n\x12SearchNewsResponse\x12\r\n\x05links\x18\x01 \x03(\t\"H\n\x15GetNewsContentRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\"\n\x07scraper\x18\x02 \x01(\x0e\x32\x11.news_getter.Site\"\xa1\x01\n\x16GetNewsContentResponse\x12\x12\n\nis_success\x18\x01 \x01(\x08\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0e\n\x06images\x18\x05 \x03(\t\x12\x0e\n\x06videos\x18\x06 \x03(\t\x12&\n\x0bsource_type\x18\x07 \x01(\x0e\x32\x11.news_getter.Site\"J\n\x12GetListNewsRequest\x12&\n\x0bsource_type\x18\x01 \x01(\x0e\x32\x11.news_getter.Site\x12\x0c\n\x04page\x18\x02 \x01(\x03\";\n\x13GetListNewsResponse\x12$\n\x04news\x18\x01 \x03(\x0b\x32\x16.news_getter.ShortNews\"\x83\x01\n\tShortNews\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12+\n\x05title\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05image\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue*`\n\x04Site\x12\x0e\n\nAutoDetect\x10\x00\x12\x0b\n\x07LentaRu\x10\x01\x12\x08\n\x04IzRu\x10\x02\x12\x07\n\x03Ria\x10\x03\x12\x0c\n\x08Interfax\x10\x04\x12\x08\n\x04Tass\x10\x05\x12\x07\n\x03\x42\x42\x43\x10\x06\x12\x07\n\x03\x43NN\x10\x07\x32\x88\x02\n\nNewsGetter\x12M\n\nSearchNews\x12\x1e.news_getter.SearchNewsRequest\x1a\x1f.news_getter.SearchNewsResponse\x12Y\n\x0eGetNewsContent\x12\".news_getter.GetNewsContentRequest\x1a#.news_getter.GetNewsContentResponse\x12P\n\x0bGetListNews\x12\x1f.news_getter.GetListNewsRequest\x1a .news_getter.GetListNewsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'news_getter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SITE']._serialized_start=706
  _globals['_SITE']._serialized_end=802
  _globals['_SEARCHNEWSREQUEST']._serialized_start=66
  _globals['_SEARCHNEWSREQUEST']._serialized_end=158
  _globals['_SEARCHNEWSRESPONSE']._serialized_start=160
  _globals['_SEARCHNEWSRESPONSE']._serialized_end=195
  _globals['_GETNEWSCONTENTREQUEST']._serialized_start=197
  _globals['_GETNEWSCONTENTREQUEST']._serialized_end=269
  _globals['_GETNEWSCONTENTRESPONSE']._serialized_start=272
  _globals['_GETNEWSCONTENTRESPONSE']._serialized_end=433
  _globals['_GETLISTNEWSREQUEST']._serialized_start=435
  _globals['_GETLISTNEWSREQUEST']._serialized_end=509
  _globals['_GETLISTNEWSRESPONSE']._serialized_start=511
  _globals['_GETLISTNEWSRESPONSE']._serialized_end=570
  _globals['_SHORTNEWS']._serialized_start=573
  _globals['_SHORTNEWS']._serialized_end=704
  _globals['_NEWSGETTER']._serialized_start=805
  _globals['_NEWSGETTER']._serialized_end=1069
# @@protoc_insertion_point(module_scope)