import pydantic
import typing

from .demographics import Demographics
from .flood_zone_information import FloodZoneInformation
from .mls_information import MlsInformation
from .mortgage_information import MortgageInformation
from .neighborhood import Neighborhood
from .owner_information import OwnerInformation
from .property_address import PropertyAddress
from .property_detail_property_flags import PropertyDetailPropertyFlags
from .property_detail_property_info import PropertyDetailPropertyInfo
from .property_valuation import PropertyValuation
from .sales_history_record import SalesHistoryRecord
from .tax_information import TaxInformation


class PropertyDetail(pydantic.BaseModel):
    """
    Complete property details
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    """
    Assessor's Parcel Number - unique identifier assigned by county assessor
    """
    apn_unformatted: typing.Optional[str] = pydantic.Field(
        alias="apnUnformatted", default=None
    )
    """
    Unformatted APN without dashes or spaces
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique property identifier in the Real Estate API system
    """
    parcel_account_number: typing.Optional[str] = pydantic.Field(
        alias="parcelAccountNumber", default=None
    )
    """
    County parcel account number
    """
    prior_id: typing.Optional[str] = pydantic.Field(alias="priorId", default=None)
    """
    Previous property ID (if property was re-indexed)
    """
    address: typing.Optional[PropertyAddress] = pydantic.Field(
        alias="address", default=None
    )
    """
    Standardized property address information
    """
    comps: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(
        alias="comps", default=None
    )
    """
    Comparable properties (when requested)
    """
    current_mortgages: typing.Optional[typing.List[MortgageInformation]] = (
        pydantic.Field(alias="currentMortgages", default=None)
    )
    demographics: typing.Optional[Demographics] = pydantic.Field(
        alias="demographics", default=None
    )
    """
    Demographic and rental information for the area
    """
    flood_info: typing.Optional[FloodZoneInformation] = pydantic.Field(
        alias="floodInfo", default=None
    )
    """
    Flood zone and environmental hazard information
    """
    mls_info: typing.Optional[MlsInformation] = pydantic.Field(
        alias="mlsInfo", default=None
    )
    """
    Multiple Listing Service (MLS) information
    """
    mortgage_history: typing.Optional[typing.List[MortgageInformation]] = (
        pydantic.Field(alias="mortgageHistory", default=None)
    )
    neighborhood: typing.Optional[Neighborhood] = pydantic.Field(
        alias="neighborhood", default=None
    )
    """
    Neighborhood information
    """
    owner_info: typing.Optional[OwnerInformation] = pydantic.Field(
        alias="ownerInfo", default=None
    )
    """
    Property owner information and characteristics
    """
    property_flags: typing.Optional[PropertyDetailPropertyFlags] = pydantic.Field(
        alias="propertyFlags", default=None
    )
    property_info: typing.Optional[PropertyDetailPropertyInfo] = pydantic.Field(
        alias="propertyInfo", default=None
    )
    property_valuation: typing.Optional[PropertyValuation] = pydantic.Field(
        alias="propertyValuation", default=None
    )
    """
    Property valuation and equity information
    """
    reapi_avm: typing.Optional[int] = pydantic.Field(alias="reapiAvm", default=None)
    """
    RealEstateAPI's Automated Valuation Model
    """
    sale_history: typing.Optional[typing.List[SalesHistoryRecord]] = pydantic.Field(
        alias="saleHistory", default=None
    )
    tax_info: typing.Optional[TaxInformation] = pydantic.Field(
        alias="taxInfo", default=None
    )
    """
    Property tax information
    """
