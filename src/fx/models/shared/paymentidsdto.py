"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fx import utils
from typing import Optional

class PaymentIdsDTOAccountType(str, Enum):
    r"""This field contains the type of an account."""
    LOCAL = 'LOCAL'
    GLOBAL = 'GLOBAL'
    LOCAL_PLUS_GLOBAL = 'LOCAL+GLOBAL'

class PaymentIdsDTOBankName(str, Enum):
    r"""This field contains the bank name.The possible values are:"""
    BOL_LT = 'BOL_LT'
    MONOOVA_AU = 'MONOOVA_AU'
    DBS_HK = 'DBS_HK'
    DBS_SG = 'DBS_SG'
    JPM_AU = 'JPM_AU'
    JPM_SG = 'JPM_SG'
    CB_GB = 'CB_GB'
    CFSB_US = 'CFSB_US'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentIdsDTO:
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName'), 'exclude': lambda f: f is None }})
    r"""This field contains the name of the account."""
    account_type: Optional[PaymentIdsDTOAccountType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountType'), 'exclude': lambda f: f is None }})
    r"""This field contains the type of an account."""
    bank_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankAddress'), 'exclude': lambda f: f is None }})
    r"""This field contains the full address of the bank."""
    bank_name: Optional[PaymentIdsDTOBankName] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankName'), 'exclude': lambda f: f is None }})
    r"""This field contains the bank name.The possible values are:"""
    bank_name_full: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankNameFull'), 'exclude': lambda f: f is None }})
    r"""This field contains the full name of the bank."""
    currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyCode'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 currency code](doc:currency-and-country-codes)."""
    routing_code_type1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingCodeType1'), 'exclude': lambda f: f is None }})
    r"""This field contains the routing code type 1."""
    routing_code_type2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingCodeType2'), 'exclude': lambda f: f is None }})
    r"""This field contains the routing code type 2."""
    routing_code_value1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingCodeValue1'), 'exclude': lambda f: f is None }})
    r"""This field contains the routing code type 1 value."""
    routing_code_value2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingCodeValue2'), 'exclude': lambda f: f is None }})
    r"""This field contains the routing code type 2 value."""
    unique_payer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uniquePayerId'), 'exclude': lambda f: f is None }})
    r"""This is a unique email Id provided to the customer in addition to uniquePaymentId for supported regions and configuration, or else it will be null, for example, abc12_ca@nium.com."""
    unique_payment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uniquePaymentId'), 'exclude': lambda f: f is None }})
    r"""This field is the virtual account number per currency provided to customers for supported regions and configuration, for example, IBAN in EU, virtual account number from Moonova in AU, or else, it will be null."""
    

