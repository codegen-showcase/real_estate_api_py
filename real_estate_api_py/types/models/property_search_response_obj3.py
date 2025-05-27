import pydantic
import typing

from .property_search_response_obj3_input import PropertySearchResponseObj3Input


class PropertySearchResponseObj3(pydantic.BaseModel):
    """
    PropertySearchResponseObj3
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.Any] = pydantic.Field(alias="data", default=None)
    input: typing.Optional[PropertySearchResponseObj3Input] = pydantic.Field(
        alias="input", default=None
    )
