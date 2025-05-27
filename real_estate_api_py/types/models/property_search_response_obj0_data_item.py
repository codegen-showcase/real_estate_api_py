import pydantic
import typing

from .property_search_response_obj0_data_item_address import (
    PropertySearchResponseObj0DataItemAddress,
)
from .property_search_response_obj0_data_item_mail_address import (
    PropertySearchResponseObj0DataItemMailAddress,
)
from .property_search_response_obj0_data_item_neighborhood import (
    PropertySearchResponseObj0DataItemNeighborhood,
)


class PropertySearchResponseObj0DataItem(pydantic.BaseModel):
    """
    PropertySearchResponseObj0DataItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mfh2to4: typing.Optional[bool] = pydantic.Field(alias="MFH2to4", default=None)
    mfh5plus: typing.Optional[bool] = pydantic.Field(alias="MFH5plus", default=None)
    absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="absenteeOwner", default=None
    )
    address: typing.Optional[PropertySearchResponseObj0DataItemAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    adjustable_rate: typing.Optional[bool] = pydantic.Field(
        alias="adjustableRate", default=None
    )
    air_conditioning_available: typing.Optional[bool] = pydantic.Field(
        alias="airConditioningAvailable", default=None
    )
    assessed_improvement_value: typing.Optional[int] = pydantic.Field(
        alias="assessedImprovementValue", default=None
    )
    assessed_land_value: typing.Optional[int] = pydantic.Field(
        alias="assessedLandValue", default=None
    )
    assessed_value: typing.Optional[int] = pydantic.Field(
        alias="assessedValue", default=None
    )
    auction: typing.Optional[bool] = pydantic.Field(alias="auction", default=None)
    basement: typing.Optional[bool] = pydantic.Field(alias="basement", default=None)
    bathrooms: typing.Optional[int] = pydantic.Field(alias="bathrooms", default=None)
    bedrooms: typing.Optional[int] = pydantic.Field(alias="bedrooms", default=None)
    cash_buyer: typing.Optional[bool] = pydantic.Field(alias="cashBuyer", default=None)
    corporate_owned: typing.Optional[bool] = pydantic.Field(
        alias="corporateOwned", default=None
    )
    death: typing.Optional[bool] = pydantic.Field(alias="death", default=None)
    distressed: typing.Optional[bool] = pydantic.Field(alias="distressed", default=None)
    document_type: typing.Optional[str] = pydantic.Field(
        alias="documentType", default=None
    )
    document_type_code: typing.Optional[str] = pydantic.Field(
        alias="documentTypeCode", default=None
    )
    equity: typing.Optional[bool] = pydantic.Field(alias="equity", default=None)
    equity_percent: typing.Optional[int] = pydantic.Field(
        alias="equityPercent", default=None
    )
    estimated_equity: typing.Optional[int] = pydantic.Field(
        alias="estimatedEquity", default=None
    )
    estimated_value: typing.Optional[int] = pydantic.Field(
        alias="estimatedValue", default=None
    )
    flood_zone: typing.Optional[bool] = pydantic.Field(alias="floodZone", default=None)
    flood_zone_description: typing.Optional[str] = pydantic.Field(
        alias="floodZoneDescription", default=None
    )
    flood_zone_type: typing.Optional[str] = pydantic.Field(
        alias="floodZoneType", default=None
    )
    for_sale: typing.Optional[bool] = pydantic.Field(alias="forSale", default=None)
    foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="foreclosure", default=None
    )
    free_clear: typing.Optional[bool] = pydantic.Field(alias="freeClear", default=None)
    garage: typing.Optional[bool] = pydantic.Field(alias="garage", default=None)
    high_equity: typing.Optional[bool] = pydantic.Field(
        alias="highEquity", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    in_state_absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="inStateAbsenteeOwner", default=None
    )
    inherited: typing.Optional[bool] = pydantic.Field(alias="inherited", default=None)
    investor_buyer: typing.Optional[bool] = pydantic.Field(
        alias="investorBuyer", default=None
    )
    land_use: typing.Optional[str] = pydantic.Field(alias="landUse", default=None)
    last_mortgage1_amount: typing.Optional[typing.Any] = pydantic.Field(
        alias="lastMortgage1Amount", default=None
    )
    last_sale_amount: typing.Optional[str] = pydantic.Field(
        alias="lastSaleAmount", default=None
    )
    last_sale_date: typing.Optional[str] = pydantic.Field(
        alias="lastSaleDate", default=None
    )
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    lender_name: typing.Optional[str] = pydantic.Field(alias="lenderName", default=None)
    listing_amount: typing.Optional[typing.Any] = pydantic.Field(
        alias="listingAmount", default=None
    )
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    lot_square_feet: typing.Optional[int] = pydantic.Field(
        alias="lotSquareFeet", default=None
    )
    mail_address: typing.Optional[PropertySearchResponseObj0DataItemMailAddress] = (
        pydantic.Field(alias="mailAddress", default=None)
    )
    median_income: typing.Optional[str] = pydantic.Field(
        alias="medianIncome", default=None
    )
    mls_active: typing.Optional[bool] = pydantic.Field(alias="mlsActive", default=None)
    mls_cancelled: typing.Optional[bool] = pydantic.Field(
        alias="mlsCancelled", default=None
    )
    mls_days_on_market: typing.Optional[int] = pydantic.Field(
        alias="mlsDaysOnMarket", default=None
    )
    mls_failed: typing.Optional[bool] = pydantic.Field(alias="mlsFailed", default=None)
    mls_has_photos: typing.Optional[bool] = pydantic.Field(
        alias="mlsHasPhotos", default=None
    )
    mls_last_sale_date: typing.Optional[str] = pydantic.Field(
        alias="mlsLastSaleDate", default=None
    )
    mls_last_status_date: typing.Optional[str] = pydantic.Field(
        alias="mlsLastStatusDate", default=None
    )
    mls_listing_date: typing.Optional[str] = pydantic.Field(
        alias="mlsListingDate", default=None
    )
    mls_listing_price: typing.Optional[int] = pydantic.Field(
        alias="mlsListingPrice", default=None
    )
    mls_pending: typing.Optional[bool] = pydantic.Field(
        alias="mlsPending", default=None
    )
    mls_sold: typing.Optional[bool] = pydantic.Field(alias="mlsSold", default=None)
    mls_status: typing.Optional[str] = pydantic.Field(alias="mlsStatus", default=None)
    mls_type: typing.Optional[str] = pydantic.Field(alias="mlsType", default=None)
    negative_equity: typing.Optional[bool] = pydantic.Field(
        alias="negativeEquity", default=None
    )
    neighborhood: typing.Optional[PropertySearchResponseObj0DataItemNeighborhood] = (
        pydantic.Field(alias="neighborhood", default=None)
    )
    open_mortgage_balance: typing.Optional[int] = pydantic.Field(
        alias="openMortgageBalance", default=None
    )
    out_of_state_absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="outOfStateAbsenteeOwner", default=None
    )
    owner1_first_name: typing.Optional[str] = pydantic.Field(
        alias="owner1FirstName", default=None
    )
    owner1_last_name: typing.Optional[str] = pydantic.Field(
        alias="owner1LastName", default=None
    )
    owner2_first_name: typing.Optional[str] = pydantic.Field(
        alias="owner2FirstName", default=None
    )
    owner2_last_name: typing.Optional[str] = pydantic.Field(
        alias="owner2LastName", default=None
    )
    owner_occupied: typing.Optional[bool] = pydantic.Field(
        alias="ownerOccupied", default=None
    )
    pre_foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="preForeclosure", default=None
    )
    private_lender: typing.Optional[bool] = pydantic.Field(
        alias="privateLender", default=None
    )
    property_id: typing.Optional[str] = pydantic.Field(alias="propertyId", default=None)
    property_type: typing.Optional[str] = pydantic.Field(
        alias="propertyType", default=None
    )
    property_use: typing.Optional[str] = pydantic.Field(
        alias="propertyUse", default=None
    )
    property_use_code: typing.Optional[int] = pydantic.Field(
        alias="propertyUseCode", default=None
    )
    rent_amount: typing.Optional[typing.Any] = pydantic.Field(
        alias="rentAmount", default=None
    )
    reo: typing.Optional[bool] = pydantic.Field(alias="reo", default=None)
    rooms_count: typing.Optional[int] = pydantic.Field(alias="roomsCount", default=None)
    square_feet: typing.Optional[int] = pydantic.Field(alias="squareFeet", default=None)
    suggested_rent: typing.Optional[str] = pydantic.Field(
        alias="suggestedRent", default=None
    )
    units_count: typing.Optional[int] = pydantic.Field(alias="unitsCount", default=None)
    vacant: typing.Optional[bool] = pydantic.Field(alias="vacant", default=None)
    year_built: typing.Optional[int] = pydantic.Field(alias="yearBuilt", default=None)
    years_owned: typing.Optional[int] = pydantic.Field(alias="yearsOwned", default=None)
