"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fx import utils
from typing import Optional

class ClientPrefundResponseDTOStatus(str, Enum):
    r"""This field contains the status."""
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientPrefundResponseDTO:
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""This field contains the amount transferred to account."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""This field will return a success message if the prefund request added successfully"""
    status: Optional[ClientPrefundResponseDTOStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""This field contains the status."""
    system_reference_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemReferenceNumber'), 'exclude': lambda f: f is None }})
    r"""This field contains the transaction reference number or identifier generated by card issuance platform for the client prefund request."""
    unique_payer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uniquePayerId'), 'exclude': lambda f: f is None }})
    r"""This field contains the unique email ID provided to the customer in addition to uniquePaymentId for supported regions and configuration, or else it will be null, for example, abc12_ca@nium.com."""
    unique_payment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uniquePaymentId'), 'exclude': lambda f: f is None }})
    r"""This field contains the virtual account number per currency provided to customers for supported regions and configuration, for example, IBAN in EU, virtual account number from Moonova in AU, or else, it will be null."""
    

