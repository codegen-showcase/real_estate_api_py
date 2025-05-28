import pydantic
import typing
import typing_extensions


class PropertyBulkParameters(typing_extensions.TypedDict):
    """
    PropertyBulkParameters
    """

    ids: typing_extensions.Required[typing.List[str]]
    """
    List of property IDs (max 1000)
    """


class _SerializerPropertyBulkParameters(pydantic.BaseModel):
    """
    Serializer for PropertyBulkParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ids: typing.List[str] = pydantic.Field(
        alias="ids",
    )
