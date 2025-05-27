import pydantic
import typing


class AddressVerifyResponseObj0DataItemInput(pydantic.BaseModel):
    """
    AddressVerifyResponseObj0DataItemInput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    key: typing.Optional[int] = pydantic.Field(alias="key", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
