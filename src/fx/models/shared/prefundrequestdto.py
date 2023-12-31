"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fx import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PrefundRequestDTO:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""This field accepts the amount transferred to account"""
    currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyCode') }})
    r"""This field accepts the 3-letter [ISO-4217 currency code](doc:currency-and-country-codes)."""
    bank_reference_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankReferenceNumber'), 'exclude': lambda f: f is None }})
    r"""This field accepts the reference number provided by the bank during fund transfer"""
    bene_account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('beneAccountNumber'), 'exclude': lambda f: f is None }})
    r"""This field accepts the virtual account number"""
    client_account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientAccountNumber'), 'exclude': lambda f: f is None }})
    r"""This field accepts the client's bank account number for reference from which the client has transferred money."""
    comments: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comments'), 'exclude': lambda f: f is None }})
    r"""This field accepts the comments which need to be passed, if any."""
    date_of_transfer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dateOfTransfer'), 'exclude': lambda f: f is None }})
    r"""This field accepts the date of the client's prefund transfer to the NIUM bank account. This request can be raised for a transfer within 30 days."""
    nium_account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('niumAccountNumber'), 'exclude': lambda f: f is None }})
    r"""This field accepts the NIUM account number to which the client has transferred the money."""
    requester_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requesterId'), 'exclude': lambda f: f is None }})
    r"""This field accepts the client's unique requester ID."""
    

