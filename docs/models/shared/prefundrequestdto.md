# PrefundRequestDTO


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      | Example                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `amount`                                                                                                                                         | *float*                                                                                                                                          | :heavy_check_mark:                                                                                                                               | This field accepts the amount transferred to account                                                                                             | 1000                                                                                                                                             |
| `bank_reference_number`                                                                                                                          | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the reference number provided by the bank during fund transfer                                                                | 712347512376                                                                                                                                     |
| `bene_account_number`                                                                                                                            | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the virtual account number                                                                                                    | 800207849                                                                                                                                        |
| `client_account_number`                                                                                                                          | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the client's bank account number for reference from which the client has transferred money.                                   | 615234671328                                                                                                                                     |
| `comments`                                                                                                                                       | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the comments which need to be passed, if any.                                                                                 | Client Prefund                                                                                                                                   |
| `currency_code`                                                                                                                                  | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | This field accepts the 3-letter [ISO-4217 currency code](doc:currency-and-country-codes).                                                        | SGD                                                                                                                                              |
| `date_of_transfer`                                                                                                                               | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the date of the client's prefund transfer to the NIUM bank account. This request can be raised for a transfer within 30 days. | 2019-11-24                                                                                                                                       |
| `nium_account_number`                                                                                                                            | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the NIUM account number to which the client has transferred the money.                                                        | 133876812367                                                                                                                                     |
| `requester_id`                                                                                                                                   | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | This field accepts the client's unique requester ID.                                                                                             | 8123768123                                                                                                                                       |