import pydantic
import typing

from .address_verify_response_obj1_data_item_input import (
    AddressVerifyResponseObj1DataItemInput,
)


class AddressVerifyResponseObj1DataItem(pydantic.BaseModel):
    """
    AddressVerifyResponseObj1DataItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    error: typing.Optional[bool] = pydantic.Field(alias="error", default=None)
    error_message: typing.Optional[str] = pydantic.Field(
        alias="errorMessage", default=None
    )
    input: typing.Optional[AddressVerifyResponseObj1DataItemInput] = pydantic.Field(
        alias="input", default=None
    )
    match_: typing.Optional[bool] = pydantic.Field(alias="match", default=None)
