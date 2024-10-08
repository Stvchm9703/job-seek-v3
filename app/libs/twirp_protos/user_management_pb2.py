# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user-management.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import job_search_pb2 as job__search__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15user-management.proto\x12\x18job_seek.user_management\x1a\x10job-search.proto\"\x82\x02\n\x0eGetUserRequest\x12\x19\n\x0creference_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tuser_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nuser_email\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x17\n\nuser_phone\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1a\n\ruser_password\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x0f\n\r_reference_idB\n\n\x08_user_idB\x0c\n\n_user_nameB\r\n\x0b_user_emailB\r\n\x0b_user_phoneB\x10\n\x0e_user_password\"@\n\x0cUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"\x81\x01\n\x0bUserAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x15\n\ruser_password\x18\x03 \x01(\t\x12\x12\n\nuser_email\x18\x04 \x01(\t\x12\x12\n\nuser_phone\x18\x05 \x01(\t\x12\x14\n\x0cuser_address\x18\x06 \x01(\t\"\x82\x01\n\rUserCVProfile\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05\x63v_id\x18\x02 \x01(\t\x12\x0f\n\x07\x63v_data\x18\x03 \x01(\x0c\x12@\n\x0b\x63v_keywords\x18\x04 \x03(\x0b\x32+.job_seek.user_management.PreferenceKeyword\"\x85\x03\n\x0bUserProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08position\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0e\n\x06salary\x18\x06 \x01(\t\x12\x10\n\x08location\x18\x07 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x08 \x01(\t\x12\x37\n\x04type\x18\t \x01(\x0e\x32).job_seek.user_management.UserProfileType\x12=\n\x08keywords\x18\n \x03(\x0b\x32+.job_seek.user_management.PreferenceKeyword\x12\x12\n\nstart_date\x18\x0b \x01(\t\x12\x10\n\x08\x65nd_date\x18\x0c \x01(\t\x12?\n\x0e\x63ompany_detail\x18\r \x01(\x0b\x32\".job_seek.job_search.CompanyDetailH\x00\x88\x01\x01\x42\x11\n\x0f_company_detail\"v\n\x11PreferenceKeyword\x12\r\n\x05kw_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0f\n\x07keyword\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x13\n\x0bis_positive\x18\x06 \x01(\x08\"\x84\x01\n\x17ListUserProfileResponse\x12\x37\n\x08profiles\x18\x01 \x03(\x0b\x32%.job_seek.user_management.UserProfile\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t*w\n\x0fUserProfileType\x12\x0b\n\x07STUDENT\x10\x00\x12\x0c\n\x08\x45MPLOYEE\x10\x01\x12\x0f\n\x0b\x43\x45RTIFICATE\x10\x02\x12\x16\n\x12PART_TIME_EMPLOYEE\x10\x03\x12\x15\n\x11\x43ONTRACT_EMPLOYEE\x10\x04\x12\t\n\x05OTHER\x10\x05\x32\xfc\x08\n\x15UserManagementService\x12\x62\n\x11\x43reateUserAccount\x12%.job_seek.user_management.UserAccount\x1a&.job_seek.user_management.UserResponse\x12\x61\n\x0eGetUserAccount\x12(.job_seek.user_management.GetUserRequest\x1a%.job_seek.user_management.UserAccount\x12\x62\n\x11UpdateUserAccount\x12%.job_seek.user_management.UserAccount\x1a&.job_seek.user_management.UserResponse\x12\x62\n\x11\x43reateUserProfile\x12%.job_seek.user_management.UserProfile\x1a&.job_seek.user_management.UserResponse\x12^\n\x0eGetUserProfile\x12%.job_seek.user_management.UserProfile\x1a%.job_seek.user_management.UserProfile\x12n\n\x0fListUserProfile\x12(.job_seek.user_management.GetUserRequest\x1a\x31.job_seek.user_management.ListUserProfileResponse\x12\x62\n\x11UpdateUserProfile\x12%.job_seek.user_management.UserProfile\x1a&.job_seek.user_management.UserResponse\x12\x65\n\x11\x44\x65leteUserProfile\x12(.job_seek.user_management.GetUserRequest\x1a&.job_seek.user_management.UserResponse\x12j\n\x17ImportUserProfileFromCV\x12\'.job_seek.user_management.UserCVProfile\x1a&.job_seek.user_management.UserResponse\x12\x66\n\x13\x43reateUserCVProfile\x12\'.job_seek.user_management.UserCVProfile\x1a&.job_seek.user_management.UserResponse\x12\x65\n\x10GetUserCVProfile\x12(.job_seek.user_management.GetUserRequest\x1a\'.job_seek.user_management.UserCVProfileB\x15Z\x13job-seek/pkg/protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_management_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\023job-seek/pkg/protos'
  _globals['_USERPROFILETYPE']._serialized_start=1308
  _globals['_USERPROFILETYPE']._serialized_end=1427
  _globals['_GETUSERREQUEST']._serialized_start=70
  _globals['_GETUSERREQUEST']._serialized_end=328
  _globals['_USERRESPONSE']._serialized_start=330
  _globals['_USERRESPONSE']._serialized_end=394
  _globals['_USERACCOUNT']._serialized_start=397
  _globals['_USERACCOUNT']._serialized_end=526
  _globals['_USERCVPROFILE']._serialized_start=529
  _globals['_USERCVPROFILE']._serialized_end=659
  _globals['_USERPROFILE']._serialized_start=662
  _globals['_USERPROFILE']._serialized_end=1051
  _globals['_PREFERENCEKEYWORD']._serialized_start=1053
  _globals['_PREFERENCEKEYWORD']._serialized_end=1171
  _globals['_LISTUSERPROFILERESPONSE']._serialized_start=1174
  _globals['_LISTUSERPROFILERESPONSE']._serialized_end=1306
  _globals['_USERMANAGEMENTSERVICE']._serialized_start=1430
  _globals['_USERMANAGEMENTSERVICE']._serialized_end=2578
# @@protoc_insertion_point(module_scope)
