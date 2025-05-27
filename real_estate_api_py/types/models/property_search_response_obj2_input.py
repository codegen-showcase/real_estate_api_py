import pydantic
import typing


class PropertySearchResponseObj2Input(pydantic.BaseModel):
    """
    PropertySearchResponseObj2Input
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    count: typing.Optional[bool] = pydantic.Field(alias="count", default=None)
    obfuscate: typing.Optional[bool] = pydantic.Field(alias="obfuscate", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
