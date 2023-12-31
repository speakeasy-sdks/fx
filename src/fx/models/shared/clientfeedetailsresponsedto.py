"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .feeresponsedto import FeeResponseDTO
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fx import utils
from typing import List, Optional

class Status(str, Enum):
    r"""This field contains the status and the possible values are:
    Active
    Inactive
    """
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    BLOCKED = 'BLOCKED'
    SUSPENDED = 'SUSPENDED'
    UPLOADED = 'UPLOADED'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'
    PARTIALLY_SUCCESS = 'PARTIALLY SUCCESS'
    SYNC = 'SYNC'
    NOT_SYNC = 'NOT SYNC'
    PENDING = 'PENDING'
    REQUIRES_ACTION = 'REQUIRES_ACTION'
    CLEAR = 'CLEAR'
    DECLINED = 'DECLINED'
    ACCOUNT_BLOCKED = 'ACCOUNT_BLOCKED'
    AMOUNT_BLOCKED = 'AMOUNT_BLOCKED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFeeDetailsResponseDTO:
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    fees: Optional[List[FeeResponseDTO]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fees'), 'exclude': lambda f: f is None }})
    r"""This is an array which contains the fees details."""
    segment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segment'), 'exclude': lambda f: f is None }})
    r"""This field contains the fee segment associated with a client."""
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""This field contains the status and the possible values are:
    Active
    Inactive
    """
    

