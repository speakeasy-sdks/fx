# fx

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/fx.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/fx/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation -->
# SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/fx.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import fx
from fx.models import operations

s = fx.Fx()


res = s.client_prefund_account.client_prefund_balances("", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.account_response_dtos is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
# Available Resources and Operations


## [client_prefund_account](docs/sdks/clientprefundaccount/README.md)

* [client_prefund_balances](docs/sdks/clientprefundaccount/README.md#client_prefund_balances) - Client Prefund Balances
* [client_prefund_request](docs/sdks/clientprefundaccount/README.md#client_prefund_request) - Client Prefund Request
* [fetch_client_prefund_request](docs/sdks/clientprefundaccount/README.md#fetch_client_prefund_request) - Fetch Client Prefund Request

## [client_settings](docs/sdks/clientsettings/README.md)

* [client_details](docs/sdks/clientsettings/README.md#client_details) - Client Details
* [fee_details](docs/sdks/clientsettings/README.md#fee_details) - Fee Details

## [client_transactions](docs/sdks/clienttransactions/README.md)

* [client_transactions](docs/sdks/clienttransactions/README.md#client_transactions) - Client Transactions
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->



<!-- End Dev Containers -->

<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


## Example

```python
import fx
from fx.models import operations

s = fx.Fx()


res = None
try:
    res = s.client_prefund_account.client_prefund_balances("", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

except (WalletApiError) as e:
    print(e) # handle exception


if res.account_response_dtos is not None:
    # handle response
    pass
```
<!-- End Error Handling -->

<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://gatewaysandbox.nium.com/` | None |

For example:


```python
import fx
from fx.models import operations

s = fx.Fx(
    server_idx=0
)


res = s.client_prefund_account.client_prefund_balances("", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.account_response_dtos is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import fx
from fx.models import operations

s = fx.Fx(
    server_url="https://gatewaysandbox.nium.com/"
)


res = s.client_prefund_account.client_prefund_balances("", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.account_response_dtos is not None:
    # handle response
    pass
```
<!-- End Server Selection -->

<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import fx
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = fx.Fx(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
