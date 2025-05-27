import pydantic
import typing


class PropertySearchResponseObj0DataItemAddress(pydantic.BaseModel):
    """
    PropertySearchResponseObj0DataItemAddress
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
