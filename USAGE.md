<!-- Start SDK Example Usage [usage] -->
```python
import fx

s = fx.Fx(
    default="<YOUR_API_KEY_HERE>",
)


res = s.client_settings.client_details(client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.client_detail_response_dto2 is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->