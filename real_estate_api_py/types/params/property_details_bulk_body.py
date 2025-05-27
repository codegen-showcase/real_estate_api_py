import pydantic
import typing
import typing_extensions


class PropertyDetailsBulkBody(typing_extensions.TypedDict):
    """
    PropertyDetailsBulkBody
    """

    ids: typing_extensions.Required[typing.List[int]]
    """
    List of property ids returned in the response of our Property Search API
    """


class _SerializerPropertyDetailsBulkBody(pydantic.BaseModel):
    """
    Serializer for PropertyDetailsBulkBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ids: typing.List[int] = pydantic.Field(
        alias="ids",
    )
