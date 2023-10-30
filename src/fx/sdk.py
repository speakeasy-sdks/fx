"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .client_prefund_account import ClientPrefundAccount
from .client_settings import ClientSettings
from .client_transactions import ClientTransactions
from .sdkconfiguration import SDKConfiguration
from fx import utils
from fx.models import shared
from typing import Dict

class Fx:
    r"""NIUM Platform: NIUM Platform"""
    client_prefund_account: ClientPrefundAccount
    r"""REST API's for Client Prefund Account"""
    client_settings: ClientSettings
    r"""REST API's for Client Settings"""
    client_transactions: ClientTransactions
    r"""REST API's for Client Prefund Account"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 default: str,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param default: The default required for authentication
        :type default: str
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        
        security_client = utils.configure_security_client(client, shared.Security(default = default))
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.client_prefund_account = ClientPrefundAccount(self.sdk_configuration)
        self.client_settings = ClientSettings(self.sdk_configuration)
        self.client_transactions = ClientTransactions(self.sdk_configuration)
    