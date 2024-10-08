# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import job_search_pb2 as job__search__pb2
import user_management_pb2 as user__management__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10prediction.proto\x12\x13job_seek.prediction\x1a\x10job-search.proto\x1a\x15user-management.proto\"\x94\x02\n\rJobMatchScore\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x15\n\rpredict_score\x18\x03 \x01(\x02\x12\x44\n\x0fhitted_keywords\x18\x04 \x03(\x0b\x32+.job_seek.user_management.PreferenceKeyword\x12*\n\x03job\x18\x05 \x01(\x0b\x32\x18.job_seek.job_search.JobH\x00\x88\x01\x01\x12@\n\x0cuser_profile\x18\x06 \x01(\x0b\x32%.job_seek.user_management.UserProfileH\x01\x88\x01\x01\x42\x06\n\x04_jobB\x0f\n\r_user_profile\"~\n\x19SurveyUserPerfenceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tsurvey_id\x18\x02 \x01(\t\x12=\n\x08keywords\x18\x03 \x03(\x0b\x32+.job_seek.user_management.PreferenceKeyword\"u\n\x18SurveyJobPerfenceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tsurvey_id\x18\x02 \x01(\t\x12\x35\n\tjob_score\x18\x03 \x03(\x0b\x32\".job_seek.prediction.JobMatchScore\"\xbd\x01\n\x0f\x45xtractKeywords\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12@\n\x0cuser_profile\x18\x03 \x01(\x0b\x32%.job_seek.user_management.UserProfileH\x00\x88\x01\x01\x12*\n\x03job\x18\x04 \x01(\x0b\x32\x18.job_seek.job_search.JobH\x01\x88\x01\x01\x42\x0f\n\r_user_profileB\x06\n\x04_job\"\xd8\x01\n\x1aGenerateCoverLetterRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12@\n\x0cuser_profile\x18\x04 \x01(\x0b\x32%.job_seek.user_management.UserProfileH\x00\x88\x01\x01\x12*\n\x03job\x18\x05 \x01(\x0b\x32\x18.job_seek.job_search.JobH\x01\x88\x01\x01\x42\x0f\n\r_user_profileB\x06\n\x04_job\"c\n\x1bGenerateCoverLetterResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"9\n\x13GetSurveyJobRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tsurvey_id\x18\x02 \x01(\t\"v\n\x0cSurveyJobSet\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x1d\n\x15user_preference_score\x18\x02 \x01(\x02\x12\x37\n\x08\x66\x65\x61tures\x18\x03 \x01(\x0b\x32%.job_seek.prediction.SurveyJobFeature\"\x85\x03\n\x10SurveyJobFeature\x12%\n\x1d\x61\x64justed_job_title_similarity\x18\x01 \x01(\x02\x12(\n adjusted_job_industry_similarity\x18\x02 \x01(\x02\x12\x1d\n\x15\x61\x64justed_company_size\x18\x03 \x01(\x02\x12\x1b\n\x13\x61\x64justed_job_sector\x18\x04 \x01(\x02\x12 \n\x18\x61\x64justed_company_culture\x18\x05 \x01(\x02\x12\x1b\n\x13\x61\x64justed_work_model\x18\x06 \x01(\x02\x12#\n\x1b\x61\x64justed_salary_expectation\x18\x07 \x01(\x02\x12\x1a\n\x12\x61\x64justed_role_type\x18\x08 \x01(\x02\x12\x1f\n\x17\x61\x64justed_distance_score\x18\t \x01(\x02\x12\x18\n\x10pay_average_norm\x18\n \x01(\x02\x12)\n!descriptions_similarity_to_resume\x18\x0b \x01(\x02\"\xee\x01\n\x14SurveyJobQuestionSet\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12\x30\n\x05job_a\x18\x02 \x01(\x0b\x32!.job_seek.prediction.SurveyJobSet\x12\x30\n\x05job_b\x18\x03 \x01(\x0b\x32!.job_seek.prediction.SurveyJobSet\x12\x14\n\x0csimilarities\x18\x04 \x03(\t\x12\x13\n\x0b\x64ifferences\x18\x05 \x03(\t\x12\x1f\n\x12overall_similarity\x18\x06 \x01(\x02H\x00\x88\x01\x01\x42\x15\n\x13_overall_similarity\"\xab\x01\n\x14GetSurveyJobResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tsurvey_id\x18\x02 \x01(\t\x12&\n\x04jobs\x18\x03 \x03(\x0b\x32\x18.job_seek.job_search.Job\x12G\n\x14survey_job_questions\x18\x04 \x03(\x0b\x32).job_seek.prediction.SurveyJobQuestionSet2\xe9\x06\n\x11PredictionService\x12l\n\x12SurveyUserPerfence\x12..job_seek.prediction.SurveyUserPerfenceRequest\x1a&.job_seek.user_management.UserResponse\x12\x63\n\x0cGetSurveyJob\x12(.job_seek.prediction.GetSurveyJobRequest\x1a).job_seek.prediction.GetSurveyJobResponse\x12j\n\x11SurveyJobPerfence\x12-.job_seek.prediction.SurveyJobPerfenceRequest\x1a&.job_seek.user_management.UserResponse\x12^\n\x14PredictJobMatchScore\x12\".job_seek.prediction.JobMatchScore\x1a\".job_seek.prediction.JobMatchScore\x12`\n\x12\x45xtractJobKeywords\x12$.job_seek.prediction.ExtractKeywords\x1a$.job_seek.prediction.ExtractKeywords\x12h\n\x1a\x45xtractUserProfileKeywords\x12$.job_seek.prediction.ExtractKeywords\x1a$.job_seek.prediction.ExtractKeywords\x12x\n\x13GenerateCoverLetter\x12/.job_seek.prediction.GenerateCoverLetterRequest\x1a\x30.job_seek.prediction.GenerateCoverLetterResponse\x12o\n\nGenerateCV\x12/.job_seek.prediction.GenerateCoverLetterRequest\x1a\x30.job_seek.prediction.GenerateCoverLetterResponseB\x15Z\x13job-seek/pkg/protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prediction_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\023job-seek/pkg/protos'
  _globals['_JOBMATCHSCORE']._serialized_start=83
  _globals['_JOBMATCHSCORE']._serialized_end=359
  _globals['_SURVEYUSERPERFENCEREQUEST']._serialized_start=361
  _globals['_SURVEYUSERPERFENCEREQUEST']._serialized_end=487
  _globals['_SURVEYJOBPERFENCEREQUEST']._serialized_start=489
  _globals['_SURVEYJOBPERFENCEREQUEST']._serialized_end=606
  _globals['_EXTRACTKEYWORDS']._serialized_start=609
  _globals['_EXTRACTKEYWORDS']._serialized_end=798
  _globals['_GENERATECOVERLETTERREQUEST']._serialized_start=801
  _globals['_GENERATECOVERLETTERREQUEST']._serialized_end=1017
  _globals['_GENERATECOVERLETTERRESPONSE']._serialized_start=1019
  _globals['_GENERATECOVERLETTERRESPONSE']._serialized_end=1118
  _globals['_GETSURVEYJOBREQUEST']._serialized_start=1120
  _globals['_GETSURVEYJOBREQUEST']._serialized_end=1177
  _globals['_SURVEYJOBSET']._serialized_start=1179
  _globals['_SURVEYJOBSET']._serialized_end=1297
  _globals['_SURVEYJOBFEATURE']._serialized_start=1300
  _globals['_SURVEYJOBFEATURE']._serialized_end=1689
  _globals['_SURVEYJOBQUESTIONSET']._serialized_start=1692
  _globals['_SURVEYJOBQUESTIONSET']._serialized_end=1930
  _globals['_GETSURVEYJOBRESPONSE']._serialized_start=1933
  _globals['_GETSURVEYJOBRESPONSE']._serialized_end=2104
  _globals['_PREDICTIONSERVICE']._serialized_start=2107
  _globals['_PREDICTIONSERVICE']._serialized_end=2980
# @@protoc_insertion_point(module_scope)
