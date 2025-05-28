import pydantic
import typing
import typing_extensions


class AutoCompleteParameters(typing_extensions.TypedDict):
    """
    AutoCompleteParameters
    """

    latitude: typing_extensions.NotRequired[float]

    longitude: typing_extensions.NotRequired[float]

    precision: typing_extensions.NotRequired[int]
    """
    Coordinate precision digits
    """

    search: typing_extensions.Required[str]
    """
    Search term (minimum 3 characters)
    """

    search_types: typing_extensions.NotRequired[typing.List[str]]
    """
    Filter by search types
    """


class _SerializerAutoCompleteParameters(pydantic.BaseModel):
    """
    Serializer for AutoCompleteParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    precision: typing.Optional[int] = pydantic.Field(alias="precision", default=None)
    search: str = pydantic.Field(
        alias="search",
    )
    search_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="search_types", default=None
    )
