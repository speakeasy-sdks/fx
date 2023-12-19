# ClientTransactions
(*client_transactions*)

## Overview

REST API's for Client Prefund Account

### Available Operations

* [client_transactions](#client_transactions) - Client Transactions

## client_transactions

This API allows you to fetch transaction details at the client level.

### Example Usage

```python
import fx
from fx.models import operations

s = fx.Fx()

req = operations.ClientTransactionsRequest(
    client_hash_id='{{clientHashId}}',
    x_request_id='{{$guid}}',
)

res = s.client_transactions.client_transactions(req, "<YOUR_API_KEY_HERE>")

if res.client_transactions_response_dto is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ClientTransactionsRequest](../../models/operations/clienttransactionsrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ClientTransactionsSecurity](../../models/operations/clienttransactionssecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ClientTransactionsResponse](../../models/operations/clienttransactionsresponse.md)**
### Errors

| Error Object          | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.WalletAPIError | 400,404,500           | application/json      |
| errors.SDKError       | 4x-5xx                | */*                   |
