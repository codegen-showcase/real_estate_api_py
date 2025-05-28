import pydantic
import typing


class Neighborhood(pydantic.BaseModel):
    """
    Neighborhood information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    center: typing.Optional[str] = pydantic.Field(alias="center", default=None)
    """
    Geographic center point of neighborhood (WKT format)
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique neighborhood identifier
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Neighborhood name
    """
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    """
    Type of neighborhood boundary
    """
