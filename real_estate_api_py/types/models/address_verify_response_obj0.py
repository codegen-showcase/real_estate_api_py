import pydantic
import typing

from .address_verify_response_obj0_data_item import AddressVerifyResponseObj0DataItem
from .address_verify_response_obj0_input import AddressVerifyResponseObj0Input


class AddressVerifyResponseObj0(pydantic.BaseModel):
    """
    AddressVerifyResponseObj0
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address_verification_execution_time_ms: typing.Optional[str] = pydantic.Field(
        alias="addressVerificationExecutionTimeMS", default=None
    )
    credits: typing.Optional[int] = pydantic.Field(alias="credits", default=None)
    data: typing.Optional[typing.List[AddressVerifyResponseObj0DataItem]] = (
        pydantic.Field(alias="data", default=None)
    )
    input: typing.Optional[AddressVerifyResponseObj0Input] = pydantic.Field(
        alias="input", default=None
    )
    live: typing.Optional[bool] = pydantic.Field(alias="live", default=None)
    request_execution_time_ms: typing.Optional[str] = pydantic.Field(
        alias="requestExecutionTimeMS", default=None
    )
    status_code: typing.Optional[int] = pydantic.Field(alias="statusCode", default=None)
    status_message: typing.Optional[str] = pydantic.Field(
        alias="statusMessage", default=None
    )
