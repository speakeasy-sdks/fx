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