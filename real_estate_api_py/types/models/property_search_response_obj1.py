import pydantic
import typing

from .property_search_response_obj1_input import PropertySearchResponseObj1Input


class PropertySearchResponseObj1(pydantic.BaseModel):
    """
    PropertySearchResponseObj1
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(
        alias="data", default=None
    )
    input: typing.Optional[PropertySearchResponseObj1Input] = pydantic.Field(
        alias="input", default=None
    )
