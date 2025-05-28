import pydantic
import typing

from .address_verify_response_data_item_input import AddressVerifyResponseDataItemInput
from .property_address import PropertyAddress


class AddressVerifyResponseDataItem(pydantic.BaseModel):
    """
    AddressVerifyResponseDataItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[PropertyAddress] = pydantic.Field(
        alias="address", default=None
    )
    """
    Standardized property address information
    """
    error: typing.Optional[bool] = pydantic.Field(alias="error", default=None)
    """
    Whether an error occurred
    """
    error_message: typing.Optional[str] = pydantic.Field(
        alias="errorMessage", default=None
    )
    """
    Error message if applicable
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Property ID if matched
    """
    input: typing.Optional[AddressVerifyResponseDataItemInput] = pydantic.Field(
        alias="input", default=None
    )
    """
    Original input address
    """
    mail_address: typing.Optional[PropertyAddress] = pydantic.Field(
        alias="mailAddress", default=None
    )
    """
    Standardized property address information
    """
    match_: typing.Optional[bool] = pydantic.Field(alias="match", default=None)
    """
    Whether address was successfully matched
    """
    property_details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="propertyDetails", default=None
    )
    """
    Basic property information
    """
