"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientdetailresponsedto2 as shared_clientdetailresponsedto2
from typing import Optional


@dataclasses.dataclass
class ClientDetailsSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    



@dataclasses.dataclass
class ClientDetailsRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique client identifier generated and shared before API handshake."""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    



@dataclasses.dataclass
class ClientDetailsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_detail_response_dto2: Optional[shared_clientdetailresponsedto2.ClientDetailResponseDto2] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

