import pydantic
import typing
import typing_extensions


class PropertyComparablesAdvancedBody(typing_extensions.TypedDict):
    """
    PropertyComparablesAdvancedBody
    """

    address: typing_extensions.NotRequired[str]
    """
    The fully formatted address for your subject property
    """

    arms_length: typing_extensions.NotRequired[bool]
    """
    Only include arms-length transactions
    """

    bathrooms_boost: typing_extensions.NotRequired[int]
    """
    Boost factor for bathroom matching (1-50)
    """

    bathrooms_max: typing_extensions.NotRequired[int]

    bathrooms_min: typing_extensions.NotRequired[int]

    bedrooms_boost: typing_extensions.NotRequired[int]
    """
    Boost factor for bedroom matching (1-50)
    """

    bedrooms_max: typing_extensions.NotRequired[int]

    bedrooms_min: typing_extensions.NotRequired[int]

    exact_match: typing_extensions.NotRequired[bool]
    """
    Enforces strictness on the address matching. No fuzzy matching.
    """

    id: typing_extensions.NotRequired[str]
    """
    Property ID for subject property
    """

    last_sale_price_max: typing_extensions.NotRequired[int]

    last_sale_price_min: typing_extensions.NotRequired[int]

    living_square_feet_boost: typing_extensions.NotRequired[int]
    """
    Boost factor for square footage matching (1-50)
    """

    living_square_feet_max: typing_extensions.NotRequired[int]

    living_square_feet_min: typing_extensions.NotRequired[int]

    lot_square_feet_boost: typing_extensions.NotRequired[int]
    """
    Boost factor for lot size matching (1-50)
    """

    lot_square_feet_max: typing_extensions.NotRequired[int]

    lot_square_feet_min: typing_extensions.NotRequired[int]

    max_days_back: typing_extensions.NotRequired[int]
    """
    Number of days back to search for recent sales comps
    """

    max_radius_miles: typing_extensions.NotRequired[float]
    """
    Search radius for comparables
    """

    max_results: typing_extensions.NotRequired[int]
    """
    Maximum number of comparable properties to return
    """

    mls_listing_price_max: typing_extensions.NotRequired[int]

    mls_listing_price_min: typing_extensions.NotRequired[int]

    same_baths: typing_extensions.NotRequired[bool]
    """
    Only include properties with same number of bathrooms
    """

    same_beds: typing_extensions.NotRequired[bool]
    """
    Only include properties with same number of bedrooms
    """

    same_census_tract: typing_extensions.NotRequired[bool]
    """
    Only include properties in same census tract
    """

    same_county: typing_extensions.NotRequired[bool]
    """
    Only include properties in same county
    """

    same_neighborhood: typing_extensions.NotRequired[bool]
    """
    Only include properties in same neighborhood
    """

    same_zip: typing_extensions.NotRequired[bool]
    """
    Only include properties in same zip code
    """

    year_built_boost: typing_extensions.NotRequired[int]
    """
    Boost factor for year built matching (1-50)
    """

    year_built_max: typing_extensions.NotRequired[int]

    year_built_min: typing_extensions.NotRequired[int]


class _SerializerPropertyComparablesAdvancedBody(pydantic.BaseModel):
    """
    Serializer for PropertyComparablesAdvancedBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    arms_length: typing.Optional[bool] = pydantic.Field(
        alias="arms_length", default=None
    )
    bathrooms_boost: typing.Optional[int] = pydantic.Field(
        alias="bathrooms_boost", default=None
    )
    bathrooms_max: typing.Optional[int] = pydantic.Field(
        alias="bathrooms_max", default=None
    )
    bathrooms_min: typing.Optional[int] = pydantic.Field(
        alias="bathrooms_min", default=None
    )
    bedrooms_boost: typing.Optional[int] = pydantic.Field(
        alias="bedrooms_boost", default=None
    )
    bedrooms_max: typing.Optional[int] = pydantic.Field(
        alias="bedrooms_max", default=None
    )
    bedrooms_min: typing.Optional[int] = pydantic.Field(
        alias="bedrooms_min", default=None
    )
    exact_match: typing.Optional[bool] = pydantic.Field(
        alias="exact_match", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    last_sale_price_max: typing.Optional[int] = pydantic.Field(
        alias="last_sale_price_max", default=None
    )
    last_sale_price_min: typing.Optional[int] = pydantic.Field(
        alias="last_sale_price_min", default=None
    )
    living_square_feet_boost: typing.Optional[int] = pydantic.Field(
        alias="living_square_feet_boost", default=None
    )
    living_square_feet_max: typing.Optional[int] = pydantic.Field(
        alias="living_square_feet_max", default=None
    )
    living_square_feet_min: typing.Optional[int] = pydantic.Field(
        alias="living_square_feet_min", default=None
    )
    lot_square_feet_boost: typing.Optional[int] = pydantic.Field(
        alias="lot_square_feet_boost", default=None
    )
    lot_square_feet_max: typing.Optional[int] = pydantic.Field(
        alias="lot_square_feet_max", default=None
    )
    lot_square_feet_min: typing.Optional[int] = pydantic.Field(
        alias="lot_square_feet_min", default=None
    )
    max_days_back: typing.Optional[int] = pydantic.Field(
        alias="max_days_back", default=None
    )
    max_radius_miles: typing.Optional[float] = pydantic.Field(
        alias="max_radius_miles", default=None
    )
    max_results: typing.Optional[int] = pydantic.Field(
        alias="max_results", default=None
    )
    mls_listing_price_max: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price_max", default=None
    )
    mls_listing_price_min: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price_min", default=None
    )
    same_baths: typing.Optional[bool] = pydantic.Field(alias="same_baths", default=None)
    same_beds: typing.Optional[bool] = pydantic.Field(alias="same_beds", default=None)
    same_census_tract: typing.Optional[bool] = pydantic.Field(
        alias="same_census_tract", default=None
    )
    same_county: typing.Optional[bool] = pydantic.Field(
        alias="same_county", default=None
    )
    same_neighborhood: typing.Optional[bool] = pydantic.Field(
        alias="same_neighborhood", default=None
    )
    same_zip: typing.Optional[bool] = pydantic.Field(alias="same_zip", default=None)
    year_built_boost: typing.Optional[int] = pydantic.Field(
        alias="year_built_boost", default=None
    )
    year_built_max: typing.Optional[int] = pydantic.Field(
        alias="year_built_max", default=None
    )
    year_built_min: typing.Optional[int] = pydantic.Field(
        alias="year_built_min", default=None
    )
