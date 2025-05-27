import pydantic
import typing


class AddressVerifyResponseObj1InputAddressesItem(pydantic.BaseModel):
    """
    AddressVerifyResponseObj1InputAddressesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    key: typing.Optional[int] = pydantic.Field(alias="key", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
