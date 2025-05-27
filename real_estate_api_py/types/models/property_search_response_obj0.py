import pydantic
import typing

from .property_search_response_obj0_data_item import PropertySearchResponseObj0DataItem
from .property_search_response_obj0_input import PropertySearchResponseObj0Input


class PropertySearchResponseObj0(pydantic.BaseModel):
    """
    PropertySearchResponseObj0
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[PropertySearchResponseObj0DataItem]] = (
        pydantic.Field(alias="data", default=None)
    )
    input: typing.Optional[PropertySearchResponseObj0Input] = pydantic.Field(
        alias="input", default=None
    )
    live: typing.Optional[bool] = pydantic.Field(alias="live", default=None)
    record_count: typing.Optional[int] = pydantic.Field(
        alias="recordCount", default=None
    )
    request_execution_time_ms: typing.Optional[str] = pydantic.Field(
        alias="requestExecutionTimeMS", default=None
    )
    result_count: typing.Optional[int] = pydantic.Field(
        alias="resultCount", default=None
    )
    result_index: typing.Optional[int] = pydantic.Field(
        alias="resultIndex", default=None
    )
    status_code: typing.Optional[int] = pydantic.Field(alias="statusCode", default=None)
    status_message: typing.Optional[str] = pydantic.Field(
        alias="statusMessage", default=None
    )
