import pydantic
import typing

from .address_verify_response_obj0_input_addresses_item import (
    AddressVerifyResponseObj0InputAddressesItem,
)


class AddressVerifyResponseObj0Input(pydantic.BaseModel):
    """
    AddressVerifyResponseObj0Input
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    addresses: typing.Optional[
        typing.List[AddressVerifyResponseObj0InputAddressesItem]
    ] = pydantic.Field(alias="addresses", default=None)
