import pydantic
import typing

from .address_verify_response_obj1_input_addresses_item import (
    AddressVerifyResponseObj1InputAddressesItem,
)


class AddressVerifyResponseObj1Input(pydantic.BaseModel):
    """
    AddressVerifyResponseObj1Input
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    addresses: typing.Optional[
        typing.List[AddressVerifyResponseObj1InputAddressesItem]
    ] = pydantic.Field(alias="addresses", default=None)
