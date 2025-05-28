import pydantic
import typing
import typing_extensions

from .address_to_verify import AddressToVerify, _SerializerAddressToVerify


class AddressVerificationParameters(typing_extensions.TypedDict):
    """
    AddressVerificationParameters
    """

    addresses: typing_extensions.Required[typing.List[AddressToVerify]]

    strict: typing_extensions.NotRequired[bool]
    """
    Enable strict verification mode
    """


class _SerializerAddressVerificationParameters(pydantic.BaseModel):
    """
    Serializer for AddressVerificationParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    addresses: typing.List[_SerializerAddressToVerify] = pydantic.Field(
        alias="addresses",
    )
    strict: typing.Optional[bool] = pydantic.Field(alias="strict", default=None)
