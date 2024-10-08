# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job-apply.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import job_search_pb2 as job__search__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fjob-apply.proto\x12\x12job_seek.job_apply\x1a\x10job-search.proto\"\x1e\n\x0bJobResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xae\x03\n\x08JobApply\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x32\n\x06status\x18\x03 \x01(\x0e\x32\x1d.job_seek.job_apply.JobStatusH\x00\x88\x01\x01\x12\x17\n\ncreated_at\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nupdated_at\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0c\x63over_letter\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x17\n\ncv_content\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07\x63v_file\x18\x08 \x01(\x0cH\x05\x88\x01\x01\x12*\n\x03job\x18\t \x01(\x0b\x32\x18.job_seek.job_search.JobH\x06\x88\x01\x01\x12\x17\n\ndeleted_at\x18\n \x01(\tH\x07\x88\x01\x01\x12\x14\n\x07message\x18\x0b \x01(\tH\x08\x88\x01\x01\x42\t\n\x07_statusB\r\n\x0b_created_atB\r\n\x0b_updated_atB\x0f\n\r_cover_letterB\r\n\x0b_cv_contentB\n\n\x08_cv_fileB\x06\n\x04_jobB\r\n\x0b_deleted_atB\n\n\x08_message\"\xd5\x01\n\x12GetJobApplyRequest\x12\x13\n\x06job_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12-\n\x06status\x18\x03 \x03(\x0e\x32\x1d.job_seek.job_apply.JobStatus\x12\x18\n\x0bpage_number\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x16\n\tpage_size\x18\x05 \x01(\x05H\x03\x88\x01\x01\x42\t\n\x07_job_idB\n\n\x08_user_idB\x0e\n\x0c_page_numberB\x0c\n\n_page_size\"\x96\x02\n\x13GetJobApplyResponse\x12\x31\n\x0bjob_applies\x18\x01 \x03(\x0b\x32\x1c.job_seek.job_apply.JobApply\x12\x18\n\x0btotal_count\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bpage_number\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x17\n\ntotal_page\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x14\n\x07message\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0erequest_status\x18\x06 \x01(\tH\x04\x88\x01\x01\x42\x0e\n\x0c_total_countB\x0e\n\x0c_page_numberB\r\n\x0b_total_pageB\n\n\x08_messageB\x11\n\x0f_request_status\"\xda\x01\n\x0bJobBookmark\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x17\n\ncreated_at\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nupdated_at\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ndeleted_at\x18\x05 \x01(\tH\x02\x88\x01\x01\x12*\n\x03job\x18\x06 \x01(\x0b\x32\x18.job_seek.job_search.JobH\x03\x88\x01\x01\x42\r\n\x0b_created_atB\r\n\x0b_updated_atB\r\n\x0b_deleted_atB\x06\n\x04_job\"\xb0\x01\n\x12JobBookmarkRequest\x12\x13\n\x06job_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nis_deleted\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x1c\n\x0fshould_show_all\x18\x04 \x01(\x08H\x03\x88\x01\x01\x42\t\n\x07_job_idB\n\n\x08_user_idB\r\n\x0b_is_deletedB\x12\n\x10_should_show_all\"&\n\x13JobBookmarkResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xa1\x02\n\x17ListJobBookmarkResponse\x12\x38\n\x0f\x62ookmarked_jobs\x18\x01 \x03(\x0b\x32\x1f.job_seek.job_apply.JobBookmark\x12\x18\n\x0btotal_count\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bpage_number\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x17\n\ntotal_page\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x14\n\x07message\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0erequest_status\x18\x06 \x01(\tH\x04\x88\x01\x01\x42\x0e\n\x0c_total_countB\x0e\n\x0c_page_numberB\r\n\x0b_total_pageB\n\n\x08_messageB\x11\n\x0f_request_status*M\n\tJobStatus\x12\x0b\n\x07PENDING\x10\x00\x12\x08\n\x04SENT\x10\x01\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x02\x12\x0c\n\x08REJECTED\x10\x03\x12\r\n\tCANCELLED\x10\x04\x32\x96\x05\n\x14JobExtendsionService\x12I\n\x08\x41pplyJob\x12\x1c.job_seek.job_apply.JobApply\x1a\x1f.job_seek.job_apply.JobResponse\x12O\n\x0eUpdateJobApply\x12\x1c.job_seek.job_apply.JobApply\x1a\x1f.job_seek.job_apply.JobResponse\x12_\n\x0cListJobApply\x12&.job_seek.job_apply.GetJobApplyRequest\x1a\'.job_seek.job_apply.GetJobApplyResponse\x12S\n\x0bGetJobApply\x12&.job_seek.job_apply.GetJobApplyRequest\x1a\x1c.job_seek.job_apply.JobApply\x12^\n\x0bJobBookmark\x12&.job_seek.job_apply.JobBookmarkRequest\x1a\'.job_seek.job_apply.JobBookmarkResponse\x12\x66\n\x0fListJobBookmark\x12&.job_seek.job_apply.JobBookmarkRequest\x1a+.job_seek.job_apply.ListJobBookmarkResponse\x12\x64\n\x11\x44\x65leteJobBookmark\x12&.job_seek.job_apply.JobBookmarkRequest\x1a\'.job_seek.job_apply.JobBookmarkResponseB\x15Z\x13job-seek/pkg/protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'job_apply_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\023job-seek/pkg/protos'
  _globals['_JOBSTATUS']._serialized_start=1751
  _globals['_JOBSTATUS']._serialized_end=1828
  _globals['_JOBRESPONSE']._serialized_start=57
  _globals['_JOBRESPONSE']._serialized_end=87
  _globals['_JOBAPPLY']._serialized_start=90
  _globals['_JOBAPPLY']._serialized_end=520
  _globals['_GETJOBAPPLYREQUEST']._serialized_start=523
  _globals['_GETJOBAPPLYREQUEST']._serialized_end=736
  _globals['_GETJOBAPPLYRESPONSE']._serialized_start=739
  _globals['_GETJOBAPPLYRESPONSE']._serialized_end=1017
  _globals['_JOBBOOKMARK']._serialized_start=1020
  _globals['_JOBBOOKMARK']._serialized_end=1238
  _globals['_JOBBOOKMARKREQUEST']._serialized_start=1241
  _globals['_JOBBOOKMARKREQUEST']._serialized_end=1417
  _globals['_JOBBOOKMARKRESPONSE']._serialized_start=1419
  _globals['_JOBBOOKMARKRESPONSE']._serialized_end=1457
  _globals['_LISTJOBBOOKMARKRESPONSE']._serialized_start=1460
  _globals['_LISTJOBBOOKMARKRESPONSE']._serialized_end=1749
  _globals['_JOBEXTENDSIONSERVICE']._serialized_start=1831
  _globals['_JOBEXTENDSIONSERVICE']._serialized_end=2493
# @@protoc_insertion_point(module_scope)
