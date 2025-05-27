import pydantic
import typing


class PropertySearchResponseObj3Input(pydantic.BaseModel):
    """
    PropertySearchResponseObj3Input
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    baths_max: typing.Optional[int] = pydantic.Field(alias="baths_max", default=None)
    baths_min: typing.Optional[int] = pydantic.Field(alias="baths_min", default=None)
    beds_max: typing.Optional[int] = pydantic.Field(alias="beds_max", default=None)
    beds_min: typing.Optional[int] = pydantic.Field(alias="beds_min", default=None)
    equity: typing.Optional[int] = pydantic.Field(alias="equity", default=None)
    equity_comparison: typing.Optional[str] = pydantic.Field(
        alias="equity_comparison", default=None
    )
    summary: typing.Optional[bool] = pydantic.Field(alias="summary", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
