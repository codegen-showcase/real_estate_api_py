import pydantic
import typing


class PropertySearchResponseObj0Input(pydantic.BaseModel):
    """
    PropertySearchResponseObj0Input
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    count: typing.Optional[bool] = pydantic.Field(alias="count", default=None)
    mls_active: typing.Optional[bool] = pydantic.Field(alias="mls_active", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
