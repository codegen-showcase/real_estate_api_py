import pydantic
import typing


class PropertySearchResponseObj0DataItemNeighborhood(pydantic.BaseModel):
    """
    PropertySearchResponseObj0DataItemNeighborhood
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    center: typing.Optional[str] = pydantic.Field(alias="center", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
