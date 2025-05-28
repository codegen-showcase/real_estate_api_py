import pydantic
import typing

from .neighborhood import Neighborhood
from .property_address import PropertyAddress


class AddressAutoCompleteResponseDataItem(pydantic.BaseModel):
    """
    AddressAutoCompleteResponseDataItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[PropertyAddress] = pydantic.Field(
        alias="address", default=None
    )
    """
    Standardized property address information
    """
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    """
    Assessor's Parcel Number
    """
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    """
    FIPS county code
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the suggestion
    """
    neighborhood: typing.Optional[Neighborhood] = pydantic.Field(
        alias="neighborhood", default=None
    )
    """
    Neighborhood information
    """
    property_id: typing.Optional[str] = pydantic.Field(alias="propertyId", default=None)
    """
    Property ID if this is a specific property
    """
    search_type: typing.Optional[str] = pydantic.Field(alias="searchType", default=None)
    """
    Type of search result
    """
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    """
    Display title for the suggestion
    """
