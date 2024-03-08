# ClientPrefundAccount
(*client_prefund_account*)

## Overview

REST API's for Client Prefund Account

### Available Operations

* [client_prefund_balances](#client_prefund_balances) - Client Prefund Balances
* [client_prefund_request](#client_prefund_request) - Client Prefund Request
* [fetch_client_prefund_request](#fetch_client_prefund_request) - Fetch Client Prefund Request

## client_prefund_balances

This API allows you to fetch the available prefund balance for a client.

### Example Usage

```python
import fx

s = fx.Fx()


res = s.client_prefund_account.client_prefund_balances("<YOUR_API_KEY_HERE>", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.ClientPrefundBalancesSecurity](../../models/operations/clientprefundbalancessecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |                                                                                                      |
| `client_hash_id`                                                                                     | *str*                                                                                                | :heavy_check_mark:                                                                                   | Unique client identifier generated and shared before API handshake.                                  | {{clientHashId}}                                                                                     |
| `x_request_id`                                                                                       | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | Enter a unique UUID value                                                                            | {{$guid}}                                                                                            |


### Response

**[operations.ClientPrefundBalancesResponse](../../models/operations/clientprefundbalancesresponse.md)**
### Errors

| Error Object          | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.WalletAPIError | 400,404,500           | application/json      |
| errors.SDKError       | 4x-5xx                | */*                   |

## client_prefund_request

This API allows our clients to raise a prefund request in the system.

### Example Usage

```python
import fx
from fx.models import shared

s = fx.Fx()


res = s.client_prefund_account.client_prefund_request("<YOUR_API_KEY_HERE>", prefund_request_dto=shared.PrefundRequestDTO(
    amount=1000,
    currency_code='SGD',
    bank_reference_number='712347512376',
    bene_account_number='800207849',
    client_account_number='615234671328',
    comments='Client Prefund',
    date_of_transfer='2019-11-24',
    nium_account_number='133876812367',
    requester_id='8123768123',
), client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.client_prefund_response_dto is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `security`                                                                                         | [operations.ClientPrefundRequestSecurity](../../models/operations/clientprefundrequestsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |                                                                                                    |
| `prefund_request_dto`                                                                              | [shared.PrefundRequestDTO](../../models/shared/prefundrequestdto.md)                               | :heavy_check_mark:                                                                                 | prefundRequestDTO                                                                                  |                                                                                                    |
| `client_hash_id`                                                                                   | *str*                                                                                              | :heavy_check_mark:                                                                                 | Unique client identifier generated and shared before API handshake.                                | {{clientHashId}}                                                                                   |
| `x_request_id`                                                                                     | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Enter a unique UUID value                                                                          | {{$guid}}                                                                                          |


### Response

**[operations.ClientPrefundRequestResponse](../../models/operations/clientprefundrequestresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.PayinAPIError | 400,404,500          | application/json     |
| errors.SDKError      | 4x-5xx               | */*                  |

## fetch_client_prefund_request

This API allows you to fetch the details of client prefund requests.

### Example Usage

```python
import fx
from fx.models import operations

s = fx.Fx()

req = operations.FetchClientPrefundRequestRequest(
    client_hash_id='{{clientHashId}}',
    x_request_id='{{$guid}}',
)

res = s.client_prefund_account.fetch_client_prefund_request(req, "<YOUR_API_KEY_HERE>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.FetchClientPrefundRequestRequest](../../models/operations/fetchclientprefundrequestrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.FetchClientPrefundRequestSecurity](../../models/operations/fetchclientprefundrequestsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.FetchClientPrefundRequestResponse](../../models/operations/fetchclientprefundrequestresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.PayinAPIError | 400,404,500          | application/json     |
| errors.SDKError      | 4x-5xx               | */*                  |
