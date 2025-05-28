import pydantic
import typing
import typing_extensions


class PropertySearchResult(pydantic.BaseModel):
    """
    TODO: enhance - Property search result summary
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
    address: str = pydantic.Field(
        alias="address",
    )
    """
    Complete formatted address
    """
    carrier_route: typing.Optional[str] = pydantic.Field(
        alias="carrierRoute", default=None
    )
    """
    USPS carrier route
    """
    census_tract: typing.Optional[str] = pydantic.Field(
        alias="censusTract", default=None
    )
    """
    Census tract identifier
    """
    city: str = pydantic.Field(
        alias="city",
    )
    """
    City name
    """
    congressional_district: typing.Optional[str] = pydantic.Field(
        alias="congressionalDistrict", default=None
    )
    """
    Congressional district number
    """
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    """
    County name
    """
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    """
    Federal Information Processing Standards (FIPS) county code
    """
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    """
    House number
    """
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    """
    Formatted address label for display
    """
    post_direction: typing.Optional[str] = pydantic.Field(
        alias="postDirection", default=None
    )
    """
    Street suffix direction
    """
    pre_direction: typing.Optional[str] = pydantic.Field(
        alias="preDirection", default=None
    )
    """
    Street prefix direction (N, S, E, W, etc.)
    """
    state: str = pydantic.Field(
        alias="state",
    )
    """
    Two-character state code
    """
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    """
    Street name without house number
    """
    street_type: typing.Optional[str] = pydantic.Field(alias="streetType", default=None)
    """
    Street type (St, Ave, Blvd, etc.)
    """
    unit: typing.Optional[str] = pydantic.Field(alias="unit", default=None)
    """
    Unit, suite, or apartment number
    """
    zip: str = pydantic.Field(
        alias="zip",
    )
    """
    Five-digit ZIP code
    """
    zip4: typing.Optional[str] = pydantic.Field(alias="zip4", default=None)
    """
    Four-digit ZIP+4 extension
    """
    bathrooms: typing.Optional[int] = pydantic.Field(alias="bathrooms", default=None)
    """
    Number of full bathrooms
    """
    bedrooms: typing.Optional[int] = pydantic.Field(alias="bedrooms", default=None)
    """
    Number of bedrooms
    """
    building_square_feet: typing.Optional[int] = pydantic.Field(
        alias="buildingSquareFeet", default=None
    )
    """
    Total building square footage including non-living areas
    """
    land_use: typing.Optional[str] = pydantic.Field(alias="landUse", default=None)
    """
    Land use classification
    """
    living_square_feet: typing.Optional[int] = pydantic.Field(
        alias="livingSquareFeet", default=None
    )
    """
    Heated/cooled living area square footage
    """
    lot_acres: typing.Optional[float] = pydantic.Field(alias="lotAcres", default=None)
    """
    Lot size in acres
    """
    lot_square_feet: typing.Optional[int] = pydantic.Field(
        alias="lotSquareFeet", default=None
    )
    """
    Lot size in square feet
    """
    parking_spaces: typing.Optional[int] = pydantic.Field(
        alias="parkingSpaces", default=None
    )
    """
    Number of parking spaces
    """
    partial_bathrooms: typing.Optional[int] = pydantic.Field(
        alias="partialBathrooms", default=None
    )
    """
    Number of partial/half bathrooms
    """
    property_type: typing.Optional[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ] = pydantic.Field(alias="propertyType", default=None)
    """
    Primary property type classification
    """
    property_use: typing.Optional[str] = pydantic.Field(
        alias="propertyUse", default=None
    )
    """
    Detailed property use description
    """
    property_use_code: typing.Optional[int] = pydantic.Field(
        alias="propertyUseCode", default=None
    )
    """
    Numeric code for property use type
    """
    rooms_count: typing.Optional[int] = pydantic.Field(alias="roomsCount", default=None)
    """
    Total number of rooms
    """
    square_feet: typing.Optional[int] = pydantic.Field(alias="squareFeet", default=None)
    """
    Living area square footage
    """
    stories: typing.Optional[int] = pydantic.Field(alias="stories", default=None)
    """
    Number of stories/floors
    """
    units_count: typing.Optional[int] = pydantic.Field(alias="unitsCount", default=None)
    """
    Number of units (for multi-family properties)
    """
    year_built: typing.Optional[int] = pydantic.Field(alias="yearBuilt", default=None)
    """
    Year the property was built
    """
    assessed_improvement_value: typing.Optional[int] = pydantic.Field(
        alias="assessedImprovementValue", default=None
    )
    """
    County assessed improvement value in USD
    """
    assessed_land_value: typing.Optional[int] = pydantic.Field(
        alias="assessedLandValue", default=None
    )
    """
    County assessed land value in USD
    """
    assessed_value: typing.Optional[int] = pydantic.Field(
        alias="assessedValue", default=None
    )
    """
    County assessed value in USD
    """
    equity_percent: typing.Optional[int] = pydantic.Field(
        alias="equityPercent", default=None
    )
    """
    Equity as percentage of property value
    """
    estimated_equity: typing.Optional[int] = pydantic.Field(
        alias="estimatedEquity", default=None
    )
    """
    Estimated owner equity (value minus mortgages) in USD
    """
    estimated_value: typing.Optional[int] = pydantic.Field(
        alias="estimatedValue", default=None
    )
    """
    Current estimated market value in USD
    """
    market_improvement_value: typing.Optional[int] = pydantic.Field(
        alias="marketImprovementValue", default=None
    )
    """
    Market improvement value in USD
    """
    market_land_value: typing.Optional[int] = pydantic.Field(
        alias="marketLandValue", default=None
    )
    """
    Market land value in USD
    """
    market_value: typing.Optional[int] = pydantic.Field(
        alias="marketValue", default=None
    )
    """
    Market value from county records in USD
    """
    cash_buyer: typing.Optional[bool] = pydantic.Field(alias="cashBuyer", default=None)
    """
    Current owner purchased with cash
    """
    death: typing.Optional[bool] = pydantic.Field(alias="death", default=None)
    """
    Recent death of property owner
    """
    distressed: typing.Optional[bool] = pydantic.Field(alias="distressed", default=None)
    """
    Property shows signs of distress
    """
    free_clear: typing.Optional[bool] = pydantic.Field(alias="freeClear", default=None)
    """
    Property has no outstanding mortgages
    """
    high_equity: typing.Optional[bool] = pydantic.Field(
        alias="highEquity", default=None
    )
    """
    Property has high equity (>40%)
    """
    inherited: typing.Optional[bool] = pydantic.Field(alias="inherited", default=None)
    """
    Property was inherited by current owner
    """
    investor_buyer: typing.Optional[bool] = pydantic.Field(
        alias="investorBuyer", default=None
    )
    """
    Property was purchased by an investor
    """
    negative_equity: typing.Optional[bool] = pydantic.Field(
        alias="negativeEquity", default=None
    )
    """
    Property has negative equity (underwater)
    """
    vacant: typing.Optional[bool] = pydantic.Field(alias="vacant", default=None)
    """
    Property appears to be vacant
    """
    adjustable_rate: typing.Optional[bool] = pydantic.Field(
        alias="adjustableRate", default=None
    )
    """
    Property has adjustable rate mortgage
    """
    assumable: typing.Optional[bool] = pydantic.Field(alias="assumable", default=None)
    """
    Mortgage is assumable
    """
    auction: typing.Optional[bool] = pydantic.Field(alias="auction", default=None)
    """
    Property is scheduled for auction
    """
    foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="foreclosure", default=None
    )
    """
    Property is in foreclosure process
    """
    judgment: typing.Optional[bool] = pydantic.Field(alias="judgment", default=None)
    """
    Property owner has legal judgments
    """
    pre_foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="preForeclosure", default=None
    )
    """
    Property received foreclosure notice
    """
    private_lender: typing.Optional[bool] = pydantic.Field(
        alias="privateLender", default=None
    )
    """
    Property financed by private lender
    """
    quit_claim: typing.Optional[bool] = pydantic.Field(alias="quitClaim", default=None)
    """
    Recent quit claim deed transfer
    """
    reo: typing.Optional[bool] = pydantic.Field(alias="reo", default=None)
    """
    Property is Real Estate Owned (bank-owned)
    """
    tax_lien: typing.Optional[bool] = pydantic.Field(alias="taxLien", default=None)
    """
    Property has tax liens
    """
    mls_active: typing.Optional[bool] = pydantic.Field(alias="mlsActive", default=None)
    """
    Property is currently active on MLS
    """
    mls_cancelled: typing.Optional[bool] = pydantic.Field(
        alias="mlsCancelled", default=None
    )
    """
    MLS listing was cancelled
    """
    mls_days_on_market: typing.Optional[int] = pydantic.Field(
        alias="mlsDaysOnMarket", default=None
    )
    """
    Number of days property was on market
    """
    mls_failed: typing.Optional[bool] = pydantic.Field(alias="mlsFailed", default=None)
    """
    MLS listing failed to sell
    """
    mls_has_photos: typing.Optional[bool] = pydantic.Field(
        alias="mlsHasPhotos", default=None
    )
    """
    MLS listing includes photos
    """
    mls_last_sale_date: typing.Optional[str] = pydantic.Field(
        alias="mlsLastSaleDate", default=None
    )
    """
    Date of last MLS sale
    """
    mls_last_status_date: typing.Optional[str] = pydantic.Field(
        alias="mlsLastStatusDate", default=None
    )
    """
    Date of last MLS status change
    """
    mls_listing_date: typing.Optional[str] = pydantic.Field(
        alias="mlsListingDate", default=None
    )
    """
    Date property was listed on MLS
    """
    mls_listing_price: typing.Optional[int] = pydantic.Field(
        alias="mlsListingPrice", default=None
    )
    """
    Current or last MLS listing price in USD
    """
    mls_pending: typing.Optional[bool] = pydantic.Field(
        alias="mlsPending", default=None
    )
    """
    Property sale is pending on MLS
    """
    mls_sold: typing.Optional[bool] = pydantic.Field(alias="mlsSold", default=None)
    """
    Property was sold through MLS
    """
    mls_status: typing.Optional[str] = pydantic.Field(alias="mlsStatus", default=None)
    """
    Current MLS status
    """
    mls_type: typing.Optional[str] = pydantic.Field(alias="mlsType", default=None)
    """
    Type of MLS listing
    """
