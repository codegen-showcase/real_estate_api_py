import pydantic
import typing
import typing_extensions


class ReportsPropertyLiensBody(typing_extensions.TypedDict):
    """
    ReportsPropertyLiensBody
    """

    address: typing_extensions.NotRequired[str]

    apn: typing_extensions.NotRequired[str]

    fips: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[int]

    zip: typing_extensions.NotRequired[str]


class _SerializerReportsPropertyLiensBody(pydantic.BaseModel):
    """
    Serializer for ReportsPropertyLiensBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
