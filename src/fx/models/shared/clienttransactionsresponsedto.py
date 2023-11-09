"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .transactionresponsedto import TransactionResponseDTO
from dataclasses_json import Undefined, dataclass_json
from fx import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientTransactionsResponseDTO:
    content: Optional[List[TransactionResponseDTO]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    r"""This field contains an array that holds additional data."""
    total_elements: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalElements'), 'exclude': lambda f: f is None }})
    r"""This field contains the number of elements in the response body."""
    total_pages: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalPages'), 'exclude': lambda f: f is None }})
    r"""This field contains the number of pages in response body."""
    
