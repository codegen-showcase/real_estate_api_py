import pydantic
import typing
import typing_extensions

from .date_range import DateRange, _SerializerDateRange
from .int_range import IntRange, _SerializerIntRange


class PropertyPinsBody(typing_extensions.TypedDict):
    """
    PropertyPinsBody
    """

    absentee_owner: typing_extensions.NotRequired[bool]

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address
    """

    adjustable_rate: typing_extensions.NotRequired[bool]

    assumable: typing_extensions.NotRequired[bool]

    auction: typing_extensions.NotRequired[bool]

    basement: typing_extensions.NotRequired[bool]

    baths: typing_extensions.NotRequired[IntRange]

    beds: typing_extensions.NotRequired[IntRange]

    building_size: typing_extensions.NotRequired[IntRange]

    cash_buyer: typing_extensions.NotRequired[bool]

    city: typing_extensions.NotRequired[str]
    """
    City name
    """

    corporate_owned: typing_extensions.NotRequired[bool]

    count: typing_extensions.NotRequired[bool]
    """
    Return only count, not results
    """

    county: typing_extensions.NotRequired[str]
    """
    County name
    """

    death: typing_extensions.NotRequired[bool]

    deck: typing_extensions.NotRequired[bool]

    estimated_equity: typing_extensions.NotRequired[IntRange]

    flood_zone: typing_extensions.NotRequired[bool]

    foreclosure: typing_extensions.NotRequired[bool]

    free_clear: typing_extensions.NotRequired[bool]

    garage: typing_extensions.NotRequired[bool]

    high_equity: typing_extensions.NotRequired[bool]

    house: typing_extensions.NotRequired[str]
    """
    House number
    """

    ids: typing_extensions.NotRequired[typing.List[str]]
    """
    List of property IDs to retrieve
    """

    ids_only: typing_extensions.NotRequired[bool]
    """
    Return only property IDs
    """

    inherited: typing_extensions.NotRequired[bool]

    last_sale_date: typing_extensions.NotRequired[DateRange]

    last_sale_price: typing_extensions.NotRequired[IntRange]

    latitude: typing_extensions.NotRequired[float]

    longitude: typing_extensions.NotRequired[float]

    lot_size: typing_extensions.NotRequired[IntRange]

    mls_active: typing_extensions.NotRequired[bool]

    mls_cancelled: typing_extensions.NotRequired[bool]

    mls_days_on_market: typing_extensions.NotRequired[IntRange]

    mls_listing_price: typing_extensions.NotRequired[IntRange]

    mls_pending: typing_extensions.NotRequired[bool]

    mls_sold: typing_extensions.NotRequired[bool]

    multi_polygon: typing_extensions.NotRequired[str]
    """
    Multi-polygon boundaries as string format
    """

    obfuscate: typing_extensions.NotRequired[bool]
    """
    Remove address and name fields
    """

    polygon: typing_extensions.NotRequired[str]
    """
    Polygon boundary as string format
    """

    pool: typing_extensions.NotRequired[bool]

    pre_foreclosure: typing_extensions.NotRequired[bool]

    private_lender: typing_extensions.NotRequired[bool]

    property_type: typing_extensions.NotRequired[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ]

    property_use_code: typing_extensions.NotRequired[int]
    """
    Property use code or array of codes
    """

    quit_claim: typing_extensions.NotRequired[bool]

    radius: typing_extensions.NotRequired[float]
    """
    Search radius in miles
    """

    reo: typing_extensions.NotRequired[bool]

    result_index: typing_extensions.NotRequired[int]
    """
    Starting index for pagination
    """

    size: typing_extensions.NotRequired[int]
    """
    Number of results to return
    """

    state: typing_extensions.NotRequired[str]
    """
    Two-letter state code
    """

    street: typing_extensions.NotRequired[str]
    """
    Street name
    """

    summary: typing_extensions.NotRequired[bool]
    """
    Return aggregated summary data
    """

    tax_lien: typing_extensions.NotRequired[bool]

    vacant: typing_extensions.NotRequired[bool]

    value: typing_extensions.NotRequired[IntRange]

    year_built: typing_extensions.NotRequired[IntRange]

    years_owned: typing_extensions.NotRequired[IntRange]

    zip: typing_extensions.NotRequired[str]
    """
    5-digit ZIP code
    """


class _SerializerPropertyPinsBody(pydantic.BaseModel):
    """
    Serializer for PropertyPinsBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="absentee_owner", default=None
    )
    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    adjustable_rate: typing.Optional[bool] = pydantic.Field(
        alias="adjustable_rate", default=None
    )
    assumable: typing.Optional[bool] = pydantic.Field(alias="assumable", default=None)
    auction: typing.Optional[bool] = pydantic.Field(alias="auction", default=None)
    basement: typing.Optional[bool] = pydantic.Field(alias="basement", default=None)
    baths: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="baths", default=None
    )
    beds: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="beds", default=None
    )
    building_size: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="building_size", default=None
    )
    cash_buyer: typing.Optional[bool] = pydantic.Field(alias="cash_buyer", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    corporate_owned: typing.Optional[bool] = pydantic.Field(
        alias="corporate_owned", default=None
    )
    count: typing.Optional[bool] = pydantic.Field(alias="count", default=None)
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    death: typing.Optional[bool] = pydantic.Field(alias="death", default=None)
    deck: typing.Optional[bool] = pydantic.Field(alias="deck", default=None)
    estimated_equity: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="estimated_equity", default=None
    )
    flood_zone: typing.Optional[bool] = pydantic.Field(alias="flood_zone", default=None)
    foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="foreclosure", default=None
    )
    free_clear: typing.Optional[bool] = pydantic.Field(alias="free_clear", default=None)
    garage: typing.Optional[bool] = pydantic.Field(alias="garage", default=None)
    high_equity: typing.Optional[bool] = pydantic.Field(
        alias="high_equity", default=None
    )
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    ids: typing.Optional[typing.List[str]] = pydantic.Field(alias="ids", default=None)
    ids_only: typing.Optional[bool] = pydantic.Field(alias="ids_only", default=None)
    inherited: typing.Optional[bool] = pydantic.Field(alias="inherited", default=None)
    last_sale_date: typing.Optional[_SerializerDateRange] = pydantic.Field(
        alias="last_sale_date", default=None
    )
    last_sale_price: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="last_sale_price", default=None
    )
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    lot_size: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="lot_size", default=None
    )
    mls_active: typing.Optional[bool] = pydantic.Field(alias="mls_active", default=None)
    mls_cancelled: typing.Optional[bool] = pydantic.Field(
        alias="mls_cancelled", default=None
    )
    mls_days_on_market: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="mls_days_on_market", default=None
    )
    mls_listing_price: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="mls_listing_price", default=None
    )
    mls_pending: typing.Optional[bool] = pydantic.Field(
        alias="mls_pending", default=None
    )
    mls_sold: typing.Optional[bool] = pydantic.Field(alias="mls_sold", default=None)
    multi_polygon: typing.Optional[str] = pydantic.Field(
        alias="multi_polygon", default=None
    )
    obfuscate: typing.Optional[bool] = pydantic.Field(alias="obfuscate", default=None)
    polygon: typing.Optional[str] = pydantic.Field(alias="polygon", default=None)
    pool: typing.Optional[bool] = pydantic.Field(alias="pool", default=None)
    pre_foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="pre_foreclosure", default=None
    )
    private_lender: typing.Optional[bool] = pydantic.Field(
        alias="private_lender", default=None
    )
    property_type: typing.Optional[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ] = pydantic.Field(alias="property_type", default=None)
    property_use_code: typing.Optional[int] = pydantic.Field(
        alias="property_use_code", default=None
    )
    quit_claim: typing.Optional[bool] = pydantic.Field(alias="quit_claim", default=None)
    radius: typing.Optional[float] = pydantic.Field(alias="radius", default=None)
    reo: typing.Optional[bool] = pydantic.Field(alias="reo", default=None)
    result_index: typing.Optional[int] = pydantic.Field(
        alias="resultIndex", default=None
    )
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    summary: typing.Optional[bool] = pydantic.Field(alias="summary", default=None)
    tax_lien: typing.Optional[bool] = pydantic.Field(alias="tax_lien", default=None)
    vacant: typing.Optional[bool] = pydantic.Field(alias="vacant", default=None)
    value: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="value", default=None
    )
    year_built: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="year_built", default=None
    )
    years_owned: typing.Optional[_SerializerIntRange] = pydantic.Field(
        alias="years_owned", default=None
    )
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
