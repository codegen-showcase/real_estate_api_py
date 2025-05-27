import pydantic
import typing

from .address_verify_response_obj0_data_item_address import (
    AddressVerifyResponseObj0DataItemAddress,
)
from .address_verify_response_obj0_data_item_input import (
    AddressVerifyResponseObj0DataItemInput,
)
from .address_verify_response_obj0_data_item_mail_address import (
    AddressVerifyResponseObj0DataItemMailAddress,
)


class AddressVerifyResponseObj0DataItem(pydantic.BaseModel):
    """
    AddressVerifyResponseObj0DataItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="absenteeOwner", default=None
    )
    address: typing.Optional[AddressVerifyResponseObj0DataItemAddress] = pydantic.Field(
        alias="address", default=None
    )
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    input: typing.Optional[AddressVerifyResponseObj0DataItemInput] = pydantic.Field(
        alias="input", default=None
    )
    latitude: typing.Optional[str] = pydantic.Field(alias="latitude", default=None)
    longitude: typing.Optional[str] = pydantic.Field(alias="longitude", default=None)
    lot_number: typing.Optional[str] = pydantic.Field(alias="lotNumber", default=None)
    mail_address: typing.Optional[AddressVerifyResponseObj0DataItemMailAddress] = (
        pydantic.Field(alias="mailAddress", default=None)
    )
    match_: typing.Optional[bool] = pydantic.Field(alias="match", default=None)
    precision: typing.Optional[str] = pydantic.Field(alias="precision", default=None)
    property_use: typing.Optional[str] = pydantic.Field(
        alias="propertyUse", default=None
    )
    search_type: typing.Optional[str] = pydantic.Field(alias="searchType", default=None)
    vacant: typing.Optional[bool] = pydantic.Field(alias="vacant", default=None)
