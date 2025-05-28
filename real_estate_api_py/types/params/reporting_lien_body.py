import pydantic
import typing
import typing_extensions


class ReportingLienBody(typing_extensions.TypedDict):
    """
    ReportingLienBody
    """

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address
    """

    apn: typing_extensions.NotRequired[str]
    """
    Assessor's Parcel Number
    """

    fips: typing_extensions.NotRequired[str]
    """
    FIPS county code
    """

    id: typing_extensions.NotRequired[str]
    """
    Property ID from search results
    """

    zip: typing_extensions.NotRequired[str]
    """
    5-digit ZIP code
    """


class _SerializerReportingLienBody(pydantic.BaseModel):
    """
    Serializer for ReportingLienBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
