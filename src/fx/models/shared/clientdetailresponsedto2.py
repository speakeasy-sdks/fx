"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import autosweepbankdetails as shared_autosweepbankdetails
from ..shared import clientcurrencyresponsedto as shared_clientcurrencyresponsedto
from ..shared import paymentidsdto as shared_paymentidsdto
from ..shared import remitteraccountwhitelist as shared_remitteraccountwhitelist
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fx import utils
from typing import List, Optional

class ClientDetailResponseDto2CurrencyAuthorizationType(str, Enum):
    r"""This field denotes the authorization type of a client. The valid values are SINGLE, DUAL, MULTI, and AUTO_SWEEP."""
    SINGLE = 'SINGLE'
    DUAL = 'DUAL'
    MULTI = 'MULTI'
    AUTO_SWEEP = 'AUTO_SWEEP'

class ClientDetailResponseDto2FundingInstrumentType(str, Enum):
    r"""This field is used to define whether the customer is allowed to fund their wallet or not. If yes that is not RESTRICTED, then either using DEBIT CARD or both DEBIT and CREDIT cards."""
    RESTRICTED = 'RESTRICTED'
    ONLY_DEBIT = 'ONLY_DEBIT'
    CREDIT_AND_DEBIT = 'CREDIT_AND_DEBIT'

class ClientDetailResponseDto2LicenseEntity(str, Enum):
    r"""This field contains the license ownership for a client.The possible values are:"""
    NIUM = 'NIUM'
    THIRD_PARTY = 'THIRD_PARTY'

class ClientDetailResponseDto2RegulatoryRegion(str, Enum):
    r"""This field contains the regulatory region of the client."""
    SG = 'SG'
    EU = 'EU'
    AU = 'AU'
    HK = 'HK'
    UK = 'UK'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientDetailResponseDto2:
    account_validation: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountValidation'), 'exclude': lambda f: f is None }})
    r"""This is applicable to RHA clients. This field will ensure whether the account-validation transactions are forwarded to client or not"""
    allow_inter_client_wallet_transfer: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowInterClientWalletTransfer'), 'exclude': lambda f: f is None }})
    r"""This field indicates if inter client wallet transfer is enabled."""
    allow_third_party_funding: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowThirdPartyFunding'), 'exclude': lambda f: f is None }})
    r"""This field specifies if third party funding is allowed or not."""
    apple_pay_support: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applePaySupport'), 'exclude': lambda f: f is None }})
    r"""This field contains the flag for apple pay support."""
    auto_sweep_bank_details: Optional[shared_autosweepbankdetails.AutoSweepBankDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoSweepBankDetails'), 'exclude': lambda f: f is None }})
    billing_address_as_corporate: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billingAddressAsCorporate'), 'exclude': lambda f: f is None }})
    r"""This field indicates whether an individual customer at the child level should have the same billing address as the business address of the corporate customer at the parent level."""
    card_txn_narrative: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cardTxnNarrative'), 'exclude': lambda f: f is None }})
    r"""This field specifies the default transaction narrative."""
    card_txn_product_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cardTxnProductCode'), 'exclude': lambda f: f is None }})
    r"""This field specifies the internal card transaction product code."""
    card_txn_redirect_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cardTxnRedirectUrl'), 'exclude': lambda f: f is None }})
    r"""This field contains the card transaction redirected URL."""
    child_must_have_parent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('childMustHaveParent'), 'exclude': lambda f: f is None }})
    r"""This field indicates whether an individual customer must be treated as a child card and be associated with a corporate customer at the parent level."""
    client_hash_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientHashId'), 'exclude': lambda f: f is None }})
    r"""This field contains the unique client identifier generated and shared before API handshake."""
    client_id_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientIdNumber'), 'exclude': lambda f: f is None }})
    r"""This field shall be deprecated in future."""
    compliance_callback_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('complianceCallbackUrl'), 'exclude': lambda f: f is None }})
    r"""This field specifies the compliance callback URL."""
    compliance_status_callback_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('complianceStatusCallbackUrl'), 'exclude': lambda f: f is None }})
    r"""This field contains the redirection URL for compliance callback."""
    confirmation_of_payee: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confirmationOfPayee'), 'exclude': lambda f: f is None }})
    r"""This field indicates whether Confirmation of Payee is allowed or not."""
    contact_no: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactNo'), 'exclude': lambda f: f is None }})
    r"""This field contains the client's contact number."""
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('countryCode'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter ISO-4217 currency code."""
    currencies: Optional[List[shared_clientcurrencyresponsedto.ClientCurrencyResponseDTO]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencies'), 'exclude': lambda f: f is None }})
    r"""This is an array objects which holds currency details."""
    currency_authorization_type: Optional[ClientDetailResponseDto2CurrencyAuthorizationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyAuthorizationType'), 'exclude': lambda f: f is None }})
    r"""This field denotes the authorization type of a client. The valid values are SINGLE, DUAL, MULTI, and AUTO_SWEEP."""
    customer_auth_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerAuthUrl'), 'exclude': lambda f: f is None }})
    r"""This field contains the customer authorization URL."""
    custom_fee_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customFeeEnabled'), 'exclude': lambda f: f is None }})
    r"""This field contains the client preference to levy custom fee."""
    deduplication_flag: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deduplicationFlag'), 'exclude': lambda f: f is None }})
    r"""This field contains the mobile/email uniqueness flag."""
    ekyc_redirect_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ekycRedirectUrl'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""This field contains the client's email Id."""
    funding_instrument_type: Optional[ClientDetailResponseDto2FundingInstrumentType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fundingInstrumentType'), 'exclude': lambda f: f is None }})
    r"""This field is used to define whether the customer is allowed to fund their wallet or not. If yes that is not RESTRICTED, then either using DEBIT CARD or both DEBIT and CREDIT cards."""
    google_pay_support: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('googlePaySupport'), 'exclude': lambda f: f is None }})
    r"""This field contains the flag for google pay support."""
    license_entity: Optional[ClientDetailResponseDto2LicenseEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('licenseEntity'), 'exclude': lambda f: f is None }})
    r"""This field contains the license ownership for a client.The possible values are:"""
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logoUrl'), 'exclude': lambda f: f is None }})
    r"""This field contains the client's logo URL."""
    markup: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markup'), 'exclude': lambda f: f is None }})
    r"""This field contains the cross currency transaction markup value."""
    minimum_customer_age: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimumCustomerAge'), 'exclude': lambda f: f is None }})
    r"""This field contains the minimum customer age which should be 18 years. Discuss with your NIUM account manager for any special use-cases."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""This field contains the name of a client."""
    notification_webhook: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationWebhook'), 'exclude': lambda f: f is None }})
    r"""This field contains the Webhook notification redirection URL."""
    payment_ids: Optional[List[shared_paymentidsdto.PaymentIdsDTO]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentIds'), 'exclude': lambda f: f is None }})
    r"""This is an array object which holds the client payment Id response details."""
    post_funded_payout: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postFundedPayout'), 'exclude': lambda f: f is None }})
    r"""This field contains the Post Funded Payout of the client."""
    prefund_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefundName'), 'exclude': lambda f: f is None }})
    r"""This field contains the name defined for ICC transactions"""
    regulatory_region: Optional[ClientDetailResponseDto2RegulatoryRegion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('regulatoryRegion'), 'exclude': lambda f: f is None }})
    r"""This field contains the regulatory region of the client."""
    samsung_pay_support: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('samsungPaySupport'), 'exclude': lambda f: f is None }})
    r"""This field contains the flag for samsung pay support."""
    whitelisted_remitter_accounts: Optional[List[shared_remitteraccountwhitelist.RemitterAccountWhiteList]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('whitelistedRemitterAccounts'), 'exclude': lambda f: f is None }})
    r"""This is an array object which holds the remitter accounts which are whitelisted for the client."""
    

