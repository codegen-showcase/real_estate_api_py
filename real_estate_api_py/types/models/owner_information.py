import pydantic
import typing

from .property_address import PropertyAddress


class OwnerInformation(pydantic.BaseModel):
    """
    Property owner information and characteristics
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="absenteeOwner", default=None
    )
    """
    Owner does not live at the property
    """
    corporate_owned: typing.Optional[bool] = pydantic.Field(
        alias="corporateOwned", default=None
    )
    """
    Property is owned by a corporation or LLC
    """
    in_state_absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="inStateAbsenteeOwner", default=None
    )
    """
    Absentee owner lives in the same state
    """
    mail_address: typing.Optional[PropertyAddress] = pydantic.Field(
        alias="mailAddress", default=None
    )
    """
    Standardized property address information
    """
    out_of_state_absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="outOfStateAbsenteeOwner", default=None
    )
    """
    Absentee owner lives in a different state
    """
    owner1_first_name: typing.Optional[str] = pydantic.Field(
        alias="owner1FirstName", default=None
    )
    """
    First owner's first name
    """
    owner1_full_name: typing.Optional[str] = pydantic.Field(
        alias="owner1FullName", default=None
    )
    """
    First owner's full name
    """
    owner1_last_name: typing.Optional[str] = pydantic.Field(
        alias="owner1LastName", default=None
    )
    """
    First owner's last name
    """
    owner2_first_name: typing.Optional[str] = pydantic.Field(
        alias="owner2FirstName", default=None
    )
    """
    Second owner's first name (if applicable)
    """
    owner2_full_name: typing.Optional[str] = pydantic.Field(
        alias="owner2FullName", default=None
    )
    """
    Second owner's full name (if applicable)
    """
    owner2_last_name: typing.Optional[str] = pydantic.Field(
        alias="owner2LastName", default=None
    )
    """
    Second owner's last name (if applicable)
    """
    owner_occupied: typing.Optional[bool] = pydantic.Field(
        alias="ownerOccupied", default=None
    )
    """
    Property is occupied by the owner
    """
    ownership_length: typing.Optional[int] = pydantic.Field(
        alias="ownershipLength", default=None
    )
    """
    Years the current owner has owned the property
    """
    trust_owned: typing.Optional[bool] = pydantic.Field(
        alias="trustOwned", default=None
    )
    """
    Property is owned by a trust
    """
    years_owned: typing.Optional[int] = pydantic.Field(alias="yearsOwned", default=None)
    """
    Years the current owner has owned the property
    """
