import pydantic
import typing

from .property_search_response_obj2_input import PropertySearchResponseObj2Input


class PropertySearchResponseObj2(pydantic.BaseModel):
    """
    PropertySearchResponseObj2
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(
        alias="data", default=None
    )
    input: typing.Optional[PropertySearchResponseObj2Input] = pydantic.Field(
        alias="input", default=None
    )
