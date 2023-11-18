"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from fx import utils
from fx.models import errors, operations, shared
from typing import List, Optional

class ClientPrefundAccount:
    r"""REST API's for Client Prefund Account"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def client_prefund_balances(self, security: operations.ClientPrefundBalancesSecurity, client_hash_id: str, x_request_id: Optional[str] = None) -> operations.ClientPrefundBalancesResponse:
        r"""Client Prefund Balances
        This API allows you to fetch the available prefund balance for a client.
        """
        request = operations.ClientPrefundBalancesRequest(
            client_hash_id=client_hash_id,
            x_request_id=x_request_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ClientPrefundBalancesRequest, base_url, '/api/v1/client/{clientHashId}/balances', request)
        headers = utils.get_headers(request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ClientPrefundBalancesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.AccountResponseDTO]])
                res.classes = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.WalletAPIError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code == 403 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def client_prefund_request(self, security: operations.ClientPrefundRequestSecurity, prefund_request_dto: shared.PrefundRequestDTO, client_hash_id: str, x_request_id: Optional[str] = None) -> operations.ClientPrefundRequestResponse:
        r"""Client Prefund Request
        This API allows our clients to raise a prefund request in the system.
        """
        request = operations.ClientPrefundRequestRequest(
            prefund_request_dto=prefund_request_dto,
            client_hash_id=client_hash_id,
            x_request_id=x_request_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ClientPrefundRequestRequest, base_url, '/api/v1/client/{clientHashId}/prefund', request)
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "prefund_request_dto", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ClientPrefundRequestResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ClientPrefundResponseDTO])
                res.client_prefund_response_dto = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.PayinAPIError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code == 403 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def fetch_client_prefund_request(self, request: operations.FetchClientPrefundRequestRequest, security: operations.FetchClientPrefundRequestSecurity) -> operations.FetchClientPrefundRequestResponse:
        r"""Fetch Client Prefund Request
        This API allows you to fetch the details of client prefund requests.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.FetchClientPrefundRequestRequest, base_url, '/api/v1/client/{clientHashId}/prefundList', request)
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.FetchClientPrefundRequestRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.FetchClientPrefundRequestResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.FetchClientPrefundRequestResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.PayinAPIError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code == 403 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    