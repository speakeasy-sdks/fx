<!-- Start SDK Example Usage [usage] -->
```python
import fx

s = fx.Fx()


res = s.client_settings.client_details("<YOUR_API_KEY_HERE>", client_hash_id='{{clientHashId}}', x_request_id='{{$guid}}')

if res.client_detail_response_dto2 is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->