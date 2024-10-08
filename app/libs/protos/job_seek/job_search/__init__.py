# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: job-search.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class SalaryType(betterproto.Enum):
    ANNUAL = 0
    MONTHLY = 1
    HOURLY = 2


class WorkType(betterproto.Enum):
    FULL_TIME = 0
    PART_TIME = 1
    CASUAL = 2
    CONTRACT = 3
    TEMPORARY = 4
    INTERNSHIP = 5
    VOLUNTEER = 6
    APPRENTICESHIP = 7


class CompanySize(betterproto.Enum):
    SIZE_A = 0
    SIZE_B = 1
    SIZE_C = 2
    SIZE_D = 3
    SIZE_E = 4
    SIZE_F = 5
    SIZE_G = 6
    SIZE_H = 7


@dataclass(eq=False, repr=False)
class JobSearchRequest(betterproto.Message):
    user_id: str = betterproto.string_field(1)
    salary_type: Optional["SalaryType"] = betterproto.enum_field(
        2, optional=True, group="_salary_type"
    )
    min_salary: Optional[int] = betterproto.int32_field(
        3, optional=True, group="_min_salary"
    )
    max_salary: Optional[int] = betterproto.int32_field(
        4, optional=True, group="_max_salary"
    )
    work_type: Optional["WorkType"] = betterproto.enum_field(
        5, optional=True, group="_work_type"
    )
    classification: Optional[int] = betterproto.int32_field(
        6, optional=True, group="_classification"
    )
    company_size: Optional["CompanySize"] = betterproto.enum_field(
        7, optional=True, group="_company_size"
    )
    work_locale: Optional[str] = betterproto.string_field(
        8, optional=True, group="_work_locale"
    )
    post_id: Optional[str] = betterproto.string_field(
        9, optional=True, group="_post_id"
    )
    company_id: Optional[str] = betterproto.string_field(
        10, optional=True, group="_company_id"
    )
    keywords: List[str] = betterproto.string_field(11)
    total_count: Optional[int] = betterproto.int32_field(
        12, optional=True, group="_total_count"
    )
    page_number: Optional[int] = betterproto.int32_field(
        13, optional=True, group="_page_number"
    )
    page_size: Optional[int] = betterproto.int32_field(
        14, optional=True, group="_page_size"
    )
    cache_ref: Optional[str] = betterproto.string_field(
        15, optional=True, group="_cache_ref"
    )
    allow_mix_cache: Optional[bool] = betterproto.bool_field(
        16, optional=True, group="_allow_mix_cache"
    )


@dataclass(eq=False, repr=False)
class JobSearchResponse(betterproto.Message):
    job: List["Job"] = betterproto.message_field(1)
    total_count: Optional[int] = betterproto.int32_field(
        2, optional=True, group="_total_count"
    )
    page_number: Optional[int] = betterproto.int32_field(
        3, optional=True, group="_page_number"
    )
    total_page: Optional[int] = betterproto.int32_field(
        4, optional=True, group="_total_page"
    )
    message: Optional[str] = betterproto.string_field(
        5, optional=True, group="_message"
    )
    cache_ref: Optional[str] = betterproto.string_field(
        6, optional=True, group="_cache_ref"
    )


@dataclass(eq=False, repr=False)
class Job(betterproto.Message):
    post_id: str = betterproto.string_field(1)
    post_title: str = betterproto.string_field(2)
    post_url: str = betterproto.string_field(3)
    pay_range: str = betterproto.string_field(4)
    debug_text: str = betterproto.string_field(5)
    hitted_keywords: List[str] = betterproto.string_field(6)
    score: Optional[int] = betterproto.int32_field(7, optional=True, group="_score")
    role: str = betterproto.string_field(8)
    work_type: str = betterproto.string_field(9)
    company_detail: Optional["CompanyDetail"] = betterproto.message_field(
        10, optional=True, group="_company_detail"
    )
    locations: str = betterproto.string_field(11)
    expiring_date: str = betterproto.string_field(12)


@dataclass(eq=False, repr=False)
class CompanyDetail(betterproto.Message):
    reference_id: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)
    url: str = betterproto.string_field(3)
    linkedin: str = betterproto.string_field(4)
    description: str = betterproto.string_field(5)
    industry: str = betterproto.string_field(6)
    job_posted: int = betterproto.int32_field(7)
    group_size: "CompanySize" = betterproto.enum_field(8)
    head_quarters: str = betterproto.string_field(9)
    specialties: List[str] = betterproto.string_field(10)
    locations: str = betterproto.string_field(11)
    last_update: str = betterproto.string_field(12)


@dataclass(eq=False, repr=False)
class CompanyDetailRequest(betterproto.Message):
    reference_id: Optional[str] = betterproto.string_field(
        1, optional=True, group="_reference_id"
    )
    name: Optional[str] = betterproto.string_field(2, optional=True, group="_name")
    industry: Optional[str] = betterproto.string_field(
        3, optional=True, group="_industry"
    )
    location: Optional[str] = betterproto.string_field(
        4, optional=True, group="_location"
    )
    group_size: List["CompanySize"] = betterproto.enum_field(5)
    specialties: List[str] = betterproto.string_field(6)
    cache_ref: Optional[str] = betterproto.string_field(
        7, optional=True, group="_cache_ref"
    )
    page_number: Optional[int] = betterproto.int32_field(
        8, optional=True, group="_page_number"
    )
    page_size: Optional[int] = betterproto.int32_field(
        9, optional=True, group="_page_size"
    )


@dataclass(eq=False, repr=False)
class CompanyDetailResponse(betterproto.Message):
    company_details: List["CompanyDetail"] = betterproto.message_field(1)
    total_count: Optional[int] = betterproto.int32_field(
        2, optional=True, group="_total_count"
    )
    page_number: Optional[int] = betterproto.int32_field(
        3, optional=True, group="_page_number"
    )
    total_page: Optional[int] = betterproto.int32_field(
        4, optional=True, group="_total_page"
    )
    message: Optional[str] = betterproto.string_field(
        5, optional=True, group="_message"
    )
    cache_ref: Optional[str] = betterproto.string_field(
        6, optional=True, group="_cache_ref"
    )


class JobSearchServiceStub(betterproto.ServiceStub):
    async def job_search(
        self,
        job_search_request: "JobSearchRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "JobSearchResponse":
        return await self._unary_unary(
            "/job_seek.job_search.JobSearchService/JobSearch",
            job_search_request,
            JobSearchResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def user_job_search(
        self,
        job_search_request: "JobSearchRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "JobSearchResponse":
        return await self._unary_unary(
            "/job_seek.job_search.JobSearchService/UserJobSearch",
            job_search_request,
            JobSearchResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_job_by_post_id(
        self,
        job_search_request: "JobSearchRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "JobSearchResponse":
        return await self._unary_unary(
            "/job_seek.job_search.JobSearchService/GetJobByPostId",
            job_search_request,
            JobSearchResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_job_by_company_id(
        self,
        job_search_request: "JobSearchRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "JobSearchResponse":
        return await self._unary_unary(
            "/job_seek.job_search.JobSearchService/GetJobByCompanyId",
            job_search_request,
            JobSearchResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def list_company_detail(
        self,
        company_detail_request: "CompanyDetailRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "CompanyDetailResponse":
        return await self._unary_unary(
            "/job_seek.job_search.JobSearchService/ListCompanyDetail",
            company_detail_request,
            CompanyDetailResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_company_detail(
        self,
        company_detail_request: "CompanyDetailRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "CompanyDetail":
        return await self._unary_unary(
            "/job_seek.job_search.JobSearchService/GetCompanyDetail",
            company_detail_request,
            CompanyDetail,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class JobSearchServiceBase(ServiceBase):

    async def job_search(
        self, job_search_request: "JobSearchRequest"
    ) -> "JobSearchResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def user_job_search(
        self, job_search_request: "JobSearchRequest"
    ) -> "JobSearchResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_job_by_post_id(
        self, job_search_request: "JobSearchRequest"
    ) -> "JobSearchResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_job_by_company_id(
        self, job_search_request: "JobSearchRequest"
    ) -> "JobSearchResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_company_detail(
        self, company_detail_request: "CompanyDetailRequest"
    ) -> "CompanyDetailResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_company_detail(
        self, company_detail_request: "CompanyDetailRequest"
    ) -> "CompanyDetail":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_job_search(
        self, stream: "grpclib.server.Stream[JobSearchRequest, JobSearchResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.job_search(request)
        await stream.send_message(response)

    async def __rpc_user_job_search(
        self, stream: "grpclib.server.Stream[JobSearchRequest, JobSearchResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.user_job_search(request)
        await stream.send_message(response)

    async def __rpc_get_job_by_post_id(
        self, stream: "grpclib.server.Stream[JobSearchRequest, JobSearchResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_job_by_post_id(request)
        await stream.send_message(response)

    async def __rpc_get_job_by_company_id(
        self, stream: "grpclib.server.Stream[JobSearchRequest, JobSearchResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_job_by_company_id(request)
        await stream.send_message(response)

    async def __rpc_list_company_detail(
        self,
        stream: "grpclib.server.Stream[CompanyDetailRequest, CompanyDetailResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.list_company_detail(request)
        await stream.send_message(response)

    async def __rpc_get_company_detail(
        self, stream: "grpclib.server.Stream[CompanyDetailRequest, CompanyDetail]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_company_detail(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/job_seek.job_search.JobSearchService/JobSearch": grpclib.const.Handler(
                self.__rpc_job_search,
                grpclib.const.Cardinality.UNARY_UNARY,
                JobSearchRequest,
                JobSearchResponse,
            ),
            "/job_seek.job_search.JobSearchService/UserJobSearch": grpclib.const.Handler(
                self.__rpc_user_job_search,
                grpclib.const.Cardinality.UNARY_UNARY,
                JobSearchRequest,
                JobSearchResponse,
            ),
            "/job_seek.job_search.JobSearchService/GetJobByPostId": grpclib.const.Handler(
                self.__rpc_get_job_by_post_id,
                grpclib.const.Cardinality.UNARY_UNARY,
                JobSearchRequest,
                JobSearchResponse,
            ),
            "/job_seek.job_search.JobSearchService/GetJobByCompanyId": grpclib.const.Handler(
                self.__rpc_get_job_by_company_id,
                grpclib.const.Cardinality.UNARY_UNARY,
                JobSearchRequest,
                JobSearchResponse,
            ),
            "/job_seek.job_search.JobSearchService/ListCompanyDetail": grpclib.const.Handler(
                self.__rpc_list_company_detail,
                grpclib.const.Cardinality.UNARY_UNARY,
                CompanyDetailRequest,
                CompanyDetailResponse,
            ),
            "/job_seek.job_search.JobSearchService/GetCompanyDetail": grpclib.const.Handler(
                self.__rpc_get_company_detail,
                grpclib.const.Cardinality.UNARY_UNARY,
                CompanyDetailRequest,
                CompanyDetail,
            ),
        }
