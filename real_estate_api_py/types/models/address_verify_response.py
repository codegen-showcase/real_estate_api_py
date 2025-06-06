import pydantic
import typing

from .address_verify_response_data_item import AddressVerifyResponseDataItem


class AddressVerifyResponse(pydantic.BaseModel):
    """
    AddressVerifyResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credits: typing.Optional[float] = pydantic.Field(alias="credits", default=None)
    """
    Number of API credits consumed by this request
    """
    live: bool = pydantic.Field(
        alias="live",
    )
    """
    Indicates if this is live data or test data
    """
    request_execution_time_ms: typing.Optional[str] = pydantic.Field(
        alias="requestExecutionTimeMS", default=None
    )
    """
    Total request execution time
    """
    status_code: int = pydantic.Field(
        alias="statusCode",
    )
    """
    HTTP status code
    """
    status_message: str = pydantic.Field(
        alias="statusMessage",
    )
    """
    Human-readable status message
    """
    data: typing.Optional[typing.List[AddressVerifyResponseDataItem]] = pydantic.Field(
        alias="data", default=None
    )
