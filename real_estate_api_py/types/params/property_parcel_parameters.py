import pydantic
import typing
import typing_extensions

from .geo_coordinate import GeoCoordinate, _SerializerGeoCoordinate


class PropertyParcelParameters(typing_extensions.TypedDict):
    """
    PropertyParcelParameters
    """

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address
    """

    apn: typing_extensions.NotRequired[str]
    """
    Assessor's Parcel Number
    """

    city: typing_extensions.NotRequired[str]
    """
    City name
    """

    county: typing_extensions.NotRequired[str]
    """
    County name
    """

    fips: typing_extensions.NotRequired[str]
    """
    FIPS county code
    """

    house: typing_extensions.NotRequired[str]
    """
    House number
    """

    id: typing_extensions.NotRequired[str]
    """
    Property ID
    """

    latitude: typing_extensions.NotRequired[float]

    longitude: typing_extensions.NotRequired[float]

    polygon: typing_extensions.NotRequired[typing.List[GeoCoordinate]]

    radius: typing_extensions.NotRequired[float]

    result_index: typing_extensions.NotRequired[int]

    size: typing_extensions.NotRequired[int]

    state: typing_extensions.NotRequired[str]

    street: typing_extensions.NotRequired[str]
    """
    Street name
    """

    unit: typing_extensions.NotRequired[str]
    """
    Unit number
    """

    zip: typing_extensions.NotRequired[str]


class _SerializerPropertyParcelParameters(pydantic.BaseModel):
    """
    Serializer for PropertyParcelParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    polygon: typing.Optional[typing.List[_SerializerGeoCoordinate]] = pydantic.Field(
        alias="polygon", default=None
    )
    radius: typing.Optional[float] = pydantic.Field(alias="radius", default=None)
    result_index: typing.Optional[int] = pydantic.Field(
        alias="resultIndex", default=None
    )
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    unit: typing.Optional[str] = pydantic.Field(alias="unit", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
