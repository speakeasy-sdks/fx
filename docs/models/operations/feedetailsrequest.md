# FeeDetailsRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_hash_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Unique client identifier generated and shared before API handshake. | {{clientHashId}}                                                    |
| `x_request_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Enter a unique UUID value                                           | {{$guid}}                                                           |