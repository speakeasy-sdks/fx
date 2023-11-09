"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientprefundresponsedto as shared_clientprefundresponsedto
from ...models.shared import prefundrequestdto as shared_prefundrequestdto
from typing import Optional


@dataclasses.dataclass
class ClientPrefundRequestSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    



@dataclasses.dataclass
class ClientPrefundRequestRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique client identifier generated and shared before API handshake."""
    prefund_request_dto: shared_prefundrequestdto.PrefundRequestDTO = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""prefundRequestDTO"""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    



@dataclasses.dataclass
class ClientPrefundRequestResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_prefund_response_dto: Optional[shared_clientprefundresponsedto.ClientPrefundResponseDTO] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
