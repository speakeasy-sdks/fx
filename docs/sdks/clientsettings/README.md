# ClientSettings
(*client_settings*)

## Overview

REST API's for Client Settings

### Available Operations

* [client_details](#client_details) - Client Details
* [fee_details](#fee_details) - Fee Details

## client_details

This API will help you to fetch the configuration details of a client.

### Example Usage

```python
import fx
from fx.models import operations

s = fx.Fx()


res = s.client_settings.client_details("<YOUR_API_KEY_HERE>", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.client_detail_response_dto2 is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.ClientDetailsSecurity](../../models/operations/clientdetailssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |                                                                                      |
| `client_hash_id`                                                                     | *str*                                                                                | :heavy_check_mark:                                                                   | Unique client identifier generated and shared before API handshake.                  | {{clientHashId}}                                                                     |
| `x_request_id`                                                                       | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Enter a unique UUID value                                                            | {{$guid}}                                                                            |


### Response

**[operations.ClientDetailsResponse](../../models/operations/clientdetailsresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ProductAPIError | 400,404,500            | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## fee_details

This API provides all the fees that have been set at the client level by NIUM.
Refer to the following [Fees User Guide](doc:fees) for the Glossary of Fees for pre-defined fees supported on the system

### Example Usage

```python
import fx
from fx.models import operations

s = fx.Fx()


res = s.client_settings.fee_details("<YOUR_API_KEY_HERE>", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.FeeDetailsSecurity](../../models/operations/feedetailssecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |                                                                                |
| `client_hash_id`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | Unique client identifier generated and shared before API handshake.            | {{clientHashId}}                                                               |
| `x_request_id`                                                                 | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Enter a unique UUID value                                                      | {{$guid}}                                                                      |


### Response

**[operations.FeeDetailsResponse](../../models/operations/feedetailsresponse.md)**
### Errors

| Error Object          | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.WalletAPIError | 400,404,500           | application/json      |
| errors.SDKError       | 4x-5xx                | */*                   |
