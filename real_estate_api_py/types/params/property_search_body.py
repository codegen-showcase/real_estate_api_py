import pydantic
import typing
import typing_extensions

from .property_search_body_multi_polygon_item import (
    PropertySearchBodyMultiPolygonItem,
    _SerializerPropertySearchBodyMultiPolygonItem,
)
from .property_search_body_polygon_item import (
    PropertySearchBodyPolygonItem,
    _SerializerPropertySearchBodyPolygonItem,
)


class PropertySearchBody(typing_extensions.TypedDict):
    """
    PropertySearchBody
    """

    absentee_owner: typing_extensions.NotRequired[bool]
    """
    Used for searching for properties where the owner is not currently a resident.  Generally signifies a tenant or non-owner occupied property.
    """

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address for a property search.  This should include house, street, city, state and zip
    """

    adjustable_rate: typing_extensions.NotRequired[bool]
    """
    Indicates if the current mortgage on the property has an adjustable rate.
    """

    apn: typing_extensions.NotRequired[str]
    """
    AutoComplete Field. The Property's unique tax assessor identifier, returned as part of the AutoComplete API response.
    """

    assessed_improvement_value_max: typing_extensions.NotRequired[int]

    assessed_improvement_value_min: typing_extensions.NotRequired[int]
    """
    Value range search against the county assessed improvement value
    """

    assessed_land_value_max: typing_extensions.NotRequired[int]

    assessed_land_value_min: typing_extensions.NotRequired[int]
    """
    Value range search against the county assessed land value
    """

    assessed_value_max: typing_extensions.NotRequired[int]

    assessed_value_min: typing_extensions.NotRequired[int]
    """
    Value range search against the county assessed value
    """

    assumable: typing_extensions.NotRequired[bool]
    """
    Indicates if the mortgage on a given property is assumable.
    """

    attic: typing_extensions.NotRequired[bool]

    auction: typing_extensions.NotRequired[bool]
    """
    Used to find properties with an auction date.  Used with search_range or a default max of 1 year.
    """

    auction_date_max: typing_extensions.NotRequired[str]

    auction_date_min: typing_extensions.NotRequired[str]
    """
    filter on dates of upcoming foreclosure auctions (e.g. Current Date "2024-05-01" & set a future date range of "2024-05-15" to "2024-05-30"). Use with "auction": true
    """

    basement: typing_extensions.NotRequired[bool]
    """
    Used to find properties with a basement.
    """

    baths_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with bathrooms between a min and max.  Maximum numbers of bathrooms for the given property search
    """

    baths_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with bathrooms between a min and max.  Minimum numbers of bathrooms for the given property search
    """

    beds_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with bedrooms between a min and max.  Maximum numbers of bedrooms for the given property search
    """

    beds_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with bedrooms between a min and max.  Minimum numbers of bedrooms for the given property search
    """

    breezeway: typing_extensions.NotRequired[bool]

    building_size_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with an interior, living square footage between a min and max.  Maximum square footage of the interior living space for the given property search
    """

    building_size_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with an interior, living square footage between a min and max.  Minimum square footage of the interior living space for the given property search
    """

    carport: typing_extensions.NotRequired[bool]
    """
    Indicates properties with a carport structure.
    """

    cash_buyer: typing_extensions.NotRequired[bool]
    """
    Indicates if the property ownership is subsequent to an all cash transaction
    """

    census_block: typing_extensions.NotRequired[str]
    """
    Values 1000-5000
    """

    census_block_group: typing_extensions.NotRequired[str]
    """
    Values 0-10
    """

    census_tract: typing_extensions.NotRequired[str]
    """
    Official tract number from the U.S. Census Bureau
    """

    city: typing_extensions.NotRequired[str]
    """
    Used to search within a city only.  Must be accompanied with state or zip to limit results.
    """

    construction: typing_extensions.NotRequired[str]
    """
    Full list of construction types: https://developer.realestateapi.com/reference/construction-types
    """

    corporate_owned: typing_extensions.NotRequired[bool]
    """
    Used to find properties where one of the owners is company.
    """

    count: typing_extensions.NotRequired[bool]
    """
    Set to true to only return the count for the total  number of records that would be returned for the search and not the records themselves.
    """

    county: typing_extensions.NotRequired[str]
    """
    Used to search within a county.  Must be accompanied by state, or zip.
    """

    county_id: typing_extensions.NotRequired[str]
    """
    AutoComplete Field.
    """

    death: typing_extensions.NotRequired[bool]
    """
    Used to find properties where the property owner on the deed is recently deceased. Can be used for probate lists.
    """

    deck: typing_extensions.NotRequired[bool]
    """
    Used to find properties that have a deck
    """

    deck_area_max: typing_extensions.NotRequired[str]
    """
    In sq. ft.
    """

    deck_area_min: typing_extensions.NotRequired[int]
    """
    In sq. ft.
    """

    document_type_code: typing_extensions.NotRequired[str]
    """
    Used to find a specific document type for more granular searches other than the booleans provided.  This field can also be assigned an array of document type codes. Used in conjunction with search_range, or a maximum default value of 1 year.
    """

    equity_operator: typing_extensions.NotRequired[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ]
    """
    Comparison operator for searches using estimated_equity.  Returns properties based on a greater than, or less than operation coupled with the value provided for estimated_equity which is based on total dollars of equity estimated from the estimated value and any known open mortgages.
    """

    equity_percent: typing_extensions.NotRequired[int]
    """
    Used in conjunction with the equity_percent_operator to find properties where the equity percentage is greater than or less than the value provided.  Equity percentage is a based on the difference of the computed LTV.
    """

    equity_percent_operator: typing_extensions.NotRequired[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ]
    """
    Comparison operator for searches using equity_percent.  Returns properties based on a greater than, or less than operation coupled with the value provided for equity_percent which is based on the difference of the calculated LTV.
    """

    estimated_equity: typing_extensions.NotRequired[int]
    """
    Used in conjunction with the equity_percent_operator to find properties where the estimated equity amount is greater than or less than the value provided.  Equity dollar amount is computed as the difference of the estimated value less any known open mortgages.
    """

    estimated_equity_max: typing_extensions.NotRequired[int]

    estimated_equity_min: typing_extensions.NotRequired[int]
    """
    Filter for properties based on the nominal value of equity owners have in their homes. Works well with "value_min"/"value_max".
    """

    feature_balcony: typing_extensions.NotRequired[bool]
    """
    Used to find properties with a balcony.
    """

    fips: typing_extensions.NotRequired[str]
    """
    AutoComplete Field.
    """

    fire_sprinklers: typing_extensions.NotRequired[bool]
    """
    Used to find properties with registered fire sprinkler fixtures.
    """

    flood_zone: typing_extensions.NotRequired[bool]
    """
    Indicates if the property is in a flood zone area. This flag can be used in conjunction with "flood_zone_type" to get more specific result sets.
    """

    flood_zone_type: typing_extensions.NotRequired[str]
    """
    B, C, X (for moderate to low risk areas); A, AE, A1-30, AH, AO, AR, A99, V, VE, V1 - V30 (High Risk - Coastal Areas); D (Undetermined Risk Zone)
    """

    foreclosure: typing_extensions.NotRequired[bool]
    """
    Used to find properties in foreclosure.  Used with search_range or a default max of 1 year.
    """

    foreclosure_date_max: typing_extensions.NotRequired[str]

    foreclosure_date_min: typing_extensions.NotRequired[str]
    """
    Filter for properties based on a date range for when a specific Foreclosure document was recorded - use with "foreclosure": true & "notice_type"
    """

    free_clear: typing_extensions.NotRequired[bool]
    """
    Used to find properties without an open mortgage.
    """

    garage: typing_extensions.NotRequired[bool]
    """
    Used to find properties with a physical structure marked for garage use.
    """

    high_equity: typing_extensions.NotRequired[bool]
    """
    Indicates properties with high equity (>39%)
    """

    hoa: typing_extensions.NotRequired[bool]

    house: typing_extensions.NotRequired[str]
    """
    Used to search for specific house numbers.   Must be accompanied with state or zip to limit results.
    """

    id: typing_extensions.NotRequired[str]
    """
    AutoComplete Field. Can be a string or an integer. Represents the unique property id in the case of full address autocomplete searches.
    """

    ids: typing_extensions.NotRequired[typing.List[int]]
    """
    Provide a list of property IDs from past or saved Property Searches to pull back all of the enriched fields
    """

    ids_only: typing_extensions.NotRequired[bool]
    """
    Returns up to 10,000 property IDs matching your search criteria. When provided, the "size" and "resultIndex" will be ignored.
    """

    in_state_owner: typing_extensions.NotRequired[bool]
    """
    Used to find properties with an owner whose mailing address is in the same state as the property address.
    """

    inherited: typing_extensions.NotRequired[bool]
    """
    Set to true to search inherited properties
    """

    investor_buyer: typing_extensions.NotRequired[bool]
    """
    Signals that the property was cash purchased by an absentee owner/investor, rather than individual like with the cash_buyer flag
    """

    judgment: typing_extensions.NotRequired[bool]
    """
    Used to find properties where a lawsuit has been filed against a property owner or a party involved in a real estate transaction, and the court rules in favor of one of the parties, and issued a judgment.
    """

    last_sale_arms_length: typing_extensions.NotRequired[bool]

    last_sale_date: typing_extensions.NotRequired[str]
    """
    Find properties based on the date of the last sale history transaction
    """

    last_sale_date_max: typing_extensions.NotRequired[str]
    """
    Maximum Date for the last sale transaction date
    """

    last_sale_date_min: typing_extensions.NotRequired[str]
    """
    Minimum Date for the last sale transaction date
    """

    last_sale_date_operator: typing_extensions.NotRequired[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ]
    """
    Used in conjunction with "last_sale_date" to find properties that satisfy the range for when they were last sold in a transaction.
    """

    last_sale_price_max: typing_extensions.NotRequired[int]

    last_sale_price_min: typing_extensions.NotRequired[int]
    """
    Filter for properties based on a Last Sale Price range.
    """

    last_update_date_max: typing_extensions.NotRequired[str]

    last_update_date_min: typing_extensions.NotRequired[str]
    """
    fetch property IDs of properties that have been updated in a given time range.
    """

    latitude: typing_extensions.NotRequired[float]
    """
    If latitude & longitude are provided, the search radius will be calculated with that set of coordinates as center
    """

    loan_type_code_first: typing_extensions.NotRequired[str]
    """
    Refer to the Loan Codes that are searchable://developer.realestateapi.com/reference/loan-type-codes
    """

    loan_type_code_second: typing_extensions.NotRequired[str]

    loan_type_code_third: typing_extensions.NotRequired[str]

    longitude: typing_extensions.NotRequired[float]
    """
    If latitude & longitude are provided, the search radius will be calculated with that set of coordinates as center
    """

    lot_size_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with lot sizes between a min and max.  Maximum square footage of the exterior lot  built for the given property search
    """

    lot_size_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with lot sizes between a min and max.  Minimum square footage of the exterior lot  built for the given property search
    """

    ltv_max: typing_extensions.NotRequired[str]
    """
    Max of 100
    """

    ltv_min: typing_extensions.NotRequired[int]
    """
    Min. of 0
    """

    median_income: typing_extensions.NotRequired[int]
    """
    Find properties based on the median income of the Areas that contain the properties
    """

    median_income_max: typing_extensions.NotRequired[int]

    median_income_min: typing_extensions.NotRequired[int]
    """
    Filter for properties that are within a certain range of median income (Zipcode-level)
    """

    median_income_operator: typing_extensions.NotRequired[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ]
    """
    Used in conjunction with the "median_income" field in order to specify the range lower or higher you want to look at from the given median_income.
    """

    mfh_2to4: typing_extensions.NotRequired[bool]
    """
    Multi-family homes with 2 to 4 units
    """

    mfh_5plus: typing_extensions.NotRequired[bool]
    """
    Multi-family homes with 5 or more units
    """

    mls_active: typing_extensions.NotRequired[bool]
    """
    Find active MLS listings
    """

    mls_cancelled: typing_extensions.NotRequired[bool]
    """
    Find terminated MLS listings
    """

    mls_days_on_market_max: typing_extensions.NotRequired[int]

    mls_days_on_market_min: typing_extensions.NotRequired[int]
    """
    Find properties that have been on the market for a certain amount of days. Use with "mls_active": true, "mls_pending": true or "mls_cancelled": true
    """

    mls_listing_price: typing_extensions.NotRequired[int]
    """
    The official MLS listing price for the property
    """

    mls_listing_price_max: typing_extensions.NotRequired[int]
    """
    Minimum value of 1
    """

    mls_listing_price_min: typing_extensions.NotRequired[int]
    """
    Lower bound used with mls_listing_max to only find properties with MLS listing prices within a defined range
    """

    mls_listing_price_operator: typing_extensions.NotRequired[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ]
    """
    mls_operator is to be used with mls_listing_price to indicate a range less than or greater than starting with that listing price. For example, { mls_listing_price: 100000, mls_operator: 'gte' } would retrieve all properties with an MLS listing price of $100,000 or more
    """

    mls_pending: typing_extensions.NotRequired[bool]
    """
    Find pending MLS sales that are expected to close
    """

    mls_sold: typing_extensions.NotRequired[bool]
    """
    Find sold MLS listings
    """

    mortgage_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with an estimated total of open mortgages between a min and max.  Maximum estimated amount for all open mortgages for the given property search.
    """

    mortgage_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with an estimated total of open mortgages between a min and max.  Minimum estimated amount for all open mortgages for the given property search.
    """

    multi_polygon: typing_extensions.NotRequired[
        typing.List[PropertySearchBodyMultiPolygonItem]
    ]
    """
    Minimum of 1 polygon
    """

    neighborhood_id: typing_extensions.NotRequired[int]
    """
    Autocomplete field.
    """

    neighborhood_name: typing_extensions.NotRequired[str]
    """
    Autocomplete field.
    """

    notice_type: typing_extensions.NotRequired[
        typing_extensions.Literal["FOR", "NOD", "NOL", "NTS", "REO"]
    ]
    """
    Search by the Recording Date of the .foreclosureInfo data for the specified notice type
    """

    obfuscate: typing_extensions.NotRequired[bool]
    """
    Will remove the address and name fields on the properties returned
    """

    out_of_state_owner: typing_extensions.NotRequired[bool]
    """
    Used to find properties with an owner whose mailing address is in a different state as the property address.
    """

    parcel_account_number: typing_extensions.NotRequired[str]
    """
    e.g. 05-00925.01
    """

    patio: typing_extensions.NotRequired[bool]
    """
    Used to find properties with a patio
    """

    polygon: typing_extensions.NotRequired[typing.List[PropertySearchBodyPolygonItem]]
    """
    Provide an array of latitude/longitude pairs for the Geo portion of your query
    """

    pool: typing_extensions.NotRequired[bool]
    """
    Used to find properties with a pool
    """

    pool_area_max: typing_extensions.NotRequired[int]
    """
    In sq. ft.
    """

    pool_area_min: typing_extensions.NotRequired[int]
    """
    In sq. ft.
    """

    portfolio_equity_max: typing_extensions.NotRequired[int]
    """
    Used to find properties where the maximum ownership interest or the stake that an investor has in the portfolio is as specified. Portfolio equity is the difference between the total value of the portfolio and any outstanding debts or liabilities related to the portfolio.
    """

    portfolio_equity_min: typing_extensions.NotRequired[int]
    """
    Used to find properties where the minimum ownership interest or the stake that an investor has in the portfolio is as specified. Portfolio equity is the difference between the total value of the portfolio and any outstanding debts or liabilities related to the portfolio.
    """

    portfolio_mortgage_balance_max: typing_extensions.NotRequired[int]

    portfolio_mortgage_balance_min: typing_extensions.NotRequired[int]
    """
    Filter for properties based on the remaining open mortgage balance of the Portfolio for Owners with > 1 property
    """

    portfolio_purchased_last12_max: typing_extensions.NotRequired[int]

    portfolio_purchased_last12_min: typing_extensions.NotRequired[int]

    portfolio_purchased_last6_max: typing_extensions.NotRequired[int]

    portfolio_purchased_last6_min: typing_extensions.NotRequired[int]

    portfolio_value_max: typing_extensions.NotRequired[int]

    portfolio_value_min: typing_extensions.NotRequired[int]
    """
    Filter for properties based on the Total Value of the Portfolio for Owners with > 1 property
    """

    pre_foreclosure: typing_extensions.NotRequired[bool]
    """
    Used to find poperties that have received any notice of preforeclosure.   Used with search_range or a default max of 1 year.
    """

    pre_foreclosure_date_max: typing_extensions.NotRequired[str]

    pre_foreclosure_date_min: typing_extensions.NotRequired[str]
    """
    Filter by the Recording Date of Pre-Foreclosure Related Documents. Use with "pre_foreclosure": true
    """

    prior_owner_individual: typing_extensions.NotRequired[bool]
    """
    Helps determine what properties are the result of a Flip. Use with "prior_owner_months_owned_min"/"prior_owner_months_owned_max"
    """

    prior_owner_months_owned_max: typing_extensions.NotRequired[int]

    prior_owner_months_owned_min: typing_extensions.NotRequired[int]
    """
    Define the time range for what constitutes a "Flip" period between the last 2 transactions
    """

    private_lender: typing_extensions.NotRequired[bool]
    """
    Returns all properties that are currently financed by a private lender
    """

    properties_owned_max: typing_extensions.NotRequired[int]
    """
    The maximum amount of total properties that any property owner's portfolio will have for each property returned.
    """

    properties_owned_min: typing_extensions.NotRequired[int]
    """
    The minimum amount of total properties that any property owner's portfolio will have for each property returned.
    """

    property_type: typing_extensions.NotRequired[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ]
    """
    Provide the type of residences/properties you are looking for
    """

    property_use_code: typing_extensions.NotRequired[int]
    """
    Also accepts an Array of Integers, where each integer is one of our accepted Property Use Codes. See all codes here: https://developer.realestateapi.com/reference/property-use-codes-reference
    """

    quit_claim: typing_extensions.NotRequired[bool]
    """
    Indicates if the property ownership was subsequent to a quit claim
    """

    radius: typing_extensions.NotRequired[float]
    """
    Provide a search radius between 0.1-10 miles for narrowing your search
    """

    reo: typing_extensions.NotRequired[bool]
    """
    Used to find properties owned by a bank, trust, services entity, or tax entity.  Used with search_range or a default max of 1 year.
    """

    result_index: typing_extensions.NotRequired[int]
    """
    Used with size to accomplish paging.  The server will skip the number of records specified by resultIndex, and return the records starting after the resultIndex.  The total number of records returned will not be greater than the size specified, or a max of 250 set by the server.
    """

    rooms_max: typing_extensions.NotRequired[int]
    """
    Used for setting the maximum on the number of total rooms you want your properties to have.
    """

    rooms_min: typing_extensions.NotRequired[int]
    """
    Used for setting the minimum on the number of total rooms you want your properties to have.
    """

    rv_parking: typing_extensions.NotRequired[bool]
    """
    The property is designated as having RV Parking
    """

    search_type: typing_extensions.NotRequired[
        typing_extensions.Literal["A", "C", "G", "N", "S", "T", "Z"]
    ]
    """
    AutoComplete Field. A = full address ; C = city ; N = county; S = street ; Z = zip; G = neighborhood; T = state
    """

    search_range: typing_extensions.NotRequired[
        typing_extensions.Literal["1_MONTH", "1_YEAR", "2_MONTH", "3_MONTH", "6_MONTH"]
    ]
    """
    Used in conjunction for reo, auction, foreclosure, and preforeclosure searches to limit the search to only return records where the event happened within the provided range.  All ranges work from NOW back to the provided range.
    """

    sewage: typing_extensions.NotRequired[str]
    """
    Options: Municipal, Yes, Septic, None, Storm
    """

    size: typing_extensions.NotRequired[int]
    """
    Set to the maximum number of records that the server can return for the search.  Used in conjunction with resultIndex for paging results.
    """

    sort: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    Sorts result set based on user defined sorting definitions across the Property Search fields
    """

    state: typing_extensions.NotRequired[str]
    """
    Used to search within a state.  Must be accompanied by city, house, or street to limit results.
    """

    state_id: typing_extensions.NotRequired[str]
    """
    AutoComplete Field.
    """

    stories_max: typing_extensions.NotRequired[int]
    """
    The maximum amount of floors/stories you want properties in your response to have
    """

    stories_min: typing_extensions.NotRequired[int]
    """
    The minimum amount of floors/stories you want properties in your response to have
    """

    street: typing_extensions.NotRequired[str]
    """
    Used to search searching street names only.  Must be accompanied with state or zip to limit results.
    """

    summary: typing_extensions.NotRequired[bool]
    """
    Returns an aggregation of all lead types in a summary object. The summary object will return totals for each lead type within the context of the given search.
    """

    tax_delinquent_year_max: typing_extensions.NotRequired[int]
    """
    2019 - 2022 range yields most results. Matching Min & Max will give a single year range.
    """

    tax_delinquent_year_min: typing_extensions.NotRequired[int]
    """
    2019 - 2022 range yields most results. Matching Min & Max will give a single year range.
    """

    tax_lien: typing_extensions.NotRequired[bool]
    """
    Find properties where there is a tax lien against the property
    """

    title: typing_extensions.NotRequired[str]
    """
    AutoComplete Field.
    """

    trust_owned: typing_extensions.NotRequired[bool]
    """
    The property is owned by a Trust
    """

    units_max: typing_extensions.NotRequired[int]
    """
    The maximum amount of individual units that the property contains
    """

    units_min: typing_extensions.NotRequired[int]
    """
    The minimum amount of individual units that the property contains
    """

    usps_mail_state: typing_extensions.NotRequired[str]

    vacant: typing_extensions.NotRequired[bool]
    """
    Used to find properties that are vacant
    """

    value_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with an estimated value between a min and max.  Maximum estimated value for the given property search.
    """

    value_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties with an estimated value between a min and max.  Minimum estimated value for the given property search
    """

    water_source: typing_extensions.NotRequired[str]
    """
    Full list of water source types you can filter by: https://developer.realestateapi.com/reference/water-source-searches
    """

    year_built_max: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties built between a min and max.  Minimum year built for the given property search
    """

    year_built_min: typing_extensions.NotRequired[int]
    """
    Used for searching a range of properties built between a min and max.  Minimum year built for the given property search
    """

    year_max: typing_extensions.NotRequired[int]
    """
    **Deprecation Notice** (replace with year_built_min). Used for searching a range of properties built between a min and max.  Maximum year built for the given property search
    """

    year_min: typing_extensions.NotRequired[int]
    """
    **Deprecation Notice** (replace with year_built_min). Used for searching a range of properties built between a min and max.  Minimum year built for the given property search
    """

    years_owned: typing_extensions.NotRequired[int]
    """
    Number value of the years owned you are searching for. To be used with years_owned_operator
    """

    years_owned_max: typing_extensions.NotRequired[int]
    """
    Number value for lower bound of a range search for years_owned. Used in conjunction with years_owned_min.
    """

    years_owned_min: typing_extensions.NotRequired[int]
    """
    Number value for lower bound of a range search for years_owned. Used in conjunction with years_owned_max
    """

    years_owned_operator: typing_extensions.NotRequired[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ]
    """
    Operator for less than and greater than searches on years_owned field
    """

    zip: typing_extensions.NotRequired[str]
    """
    Used to search within a US zip code. An array of zips (of type:string) can also be provided to this field.
    """


class _SerializerPropertySearchBody(pydantic.BaseModel):
    """
    Serializer for PropertySearchBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    absentee_owner: typing.Optional[bool] = pydantic.Field(
        alias="absentee_owner", default=None
    )
    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    adjustable_rate: typing.Optional[bool] = pydantic.Field(
        alias="adjustable_rate", default=None
    )
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    assessed_improvement_value_max: typing.Optional[int] = pydantic.Field(
        alias="assessed_improvement_value_max", default=None
    )
    assessed_improvement_value_min: typing.Optional[int] = pydantic.Field(
        alias="assessed_improvement_value_min", default=None
    )
    assessed_land_value_max: typing.Optional[int] = pydantic.Field(
        alias="assessed_land_value_max", default=None
    )
    assessed_land_value_min: typing.Optional[int] = pydantic.Field(
        alias="assessed_land_value_min", default=None
    )
    assessed_value_max: typing.Optional[int] = pydantic.Field(
        alias="assessed_value_max", default=None
    )
    assessed_value_min: typing.Optional[int] = pydantic.Field(
        alias="assessed_value_min", default=None
    )
    assumable: typing.Optional[bool] = pydantic.Field(alias="assumable", default=None)
    attic: typing.Optional[bool] = pydantic.Field(alias="attic", default=None)
    auction: typing.Optional[bool] = pydantic.Field(alias="auction", default=None)
    auction_date_max: typing.Optional[str] = pydantic.Field(
        alias="auction_date_max", default=None
    )
    auction_date_min: typing.Optional[str] = pydantic.Field(
        alias="auction_date_min", default=None
    )
    basement: typing.Optional[bool] = pydantic.Field(alias="basement", default=None)
    baths_max: typing.Optional[int] = pydantic.Field(alias="baths_max", default=None)
    baths_min: typing.Optional[int] = pydantic.Field(alias="baths_min", default=None)
    beds_max: typing.Optional[int] = pydantic.Field(alias="beds_max", default=None)
    beds_min: typing.Optional[int] = pydantic.Field(alias="beds_min", default=None)
    breezeway: typing.Optional[bool] = pydantic.Field(alias="breezeway", default=None)
    building_size_max: typing.Optional[int] = pydantic.Field(
        alias="building_size_max", default=None
    )
    building_size_min: typing.Optional[int] = pydantic.Field(
        alias="building_size_min", default=None
    )
    carport: typing.Optional[bool] = pydantic.Field(alias="carport", default=None)
    cash_buyer: typing.Optional[bool] = pydantic.Field(alias="cash_buyer", default=None)
    census_block: typing.Optional[str] = pydantic.Field(
        alias="census_block", default=None
    )
    census_block_group: typing.Optional[str] = pydantic.Field(
        alias="census_block_group", default=None
    )
    census_tract: typing.Optional[str] = pydantic.Field(
        alias="census_tract", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    construction: typing.Optional[str] = pydantic.Field(
        alias="construction", default=None
    )
    corporate_owned: typing.Optional[bool] = pydantic.Field(
        alias="corporate_owned", default=None
    )
    count: typing.Optional[bool] = pydantic.Field(alias="count", default=None)
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    county_id: typing.Optional[str] = pydantic.Field(alias="countyId", default=None)
    death: typing.Optional[bool] = pydantic.Field(alias="death", default=None)
    deck: typing.Optional[bool] = pydantic.Field(alias="deck", default=None)
    deck_area_max: typing.Optional[str] = pydantic.Field(
        alias="deck_area_max", default=None
    )
    deck_area_min: typing.Optional[int] = pydantic.Field(
        alias="deck_area_min", default=None
    )
    document_type_code: typing.Optional[str] = pydantic.Field(
        alias="document_type_code", default=None
    )
    equity_operator: typing.Optional[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ] = pydantic.Field(alias="equity_operator", default=None)
    equity_percent: typing.Optional[int] = pydantic.Field(
        alias="equity_percent", default=None
    )
    equity_percent_operator: typing.Optional[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ] = pydantic.Field(alias="equity_percent_operator", default=None)
    estimated_equity: typing.Optional[int] = pydantic.Field(
        alias="estimated_equity", default=None
    )
    estimated_equity_max: typing.Optional[int] = pydantic.Field(
        alias="estimated_equity_max", default=None
    )
    estimated_equity_min: typing.Optional[int] = pydantic.Field(
        alias="estimated_equity_min", default=None
    )
    feature_balcony: typing.Optional[bool] = pydantic.Field(
        alias="feature_balcony", default=None
    )
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    fire_sprinklers: typing.Optional[bool] = pydantic.Field(
        alias="fire_sprinklers", default=None
    )
    flood_zone: typing.Optional[bool] = pydantic.Field(alias="flood_zone", default=None)
    flood_zone_type: typing.Optional[str] = pydantic.Field(
        alias="flood_zone_type", default=None
    )
    foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="foreclosure", default=None
    )
    foreclosure_date_max: typing.Optional[str] = pydantic.Field(
        alias="foreclosure_date_max", default=None
    )
    foreclosure_date_min: typing.Optional[str] = pydantic.Field(
        alias="foreclosure_date_min", default=None
    )
    free_clear: typing.Optional[bool] = pydantic.Field(alias="free_clear", default=None)
    garage: typing.Optional[bool] = pydantic.Field(alias="garage", default=None)
    high_equity: typing.Optional[bool] = pydantic.Field(
        alias="high_equity", default=None
    )
    hoa: typing.Optional[bool] = pydantic.Field(alias="hoa", default=None)
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    ids: typing.Optional[typing.List[int]] = pydantic.Field(alias="ids", default=None)
    ids_only: typing.Optional[bool] = pydantic.Field(alias="ids_only", default=None)
    in_state_owner: typing.Optional[bool] = pydantic.Field(
        alias="in_state_owner", default=None
    )
    inherited: typing.Optional[bool] = pydantic.Field(alias="inherited", default=None)
    investor_buyer: typing.Optional[bool] = pydantic.Field(
        alias="investor_buyer", default=None
    )
    judgment: typing.Optional[bool] = pydantic.Field(alias="judgment", default=None)
    last_sale_arms_length: typing.Optional[bool] = pydantic.Field(
        alias="last_sale_arms_length", default=None
    )
    last_sale_date: typing.Optional[str] = pydantic.Field(
        alias="last_sale_date", default=None
    )
    last_sale_date_max: typing.Optional[str] = pydantic.Field(
        alias="last_sale_date_max", default=None
    )
    last_sale_date_min: typing.Optional[str] = pydantic.Field(
        alias="last_sale_date_min", default=None
    )
    last_sale_date_operator: typing.Optional[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ] = pydantic.Field(alias="last_sale_date_operator", default=None)
    last_sale_price_max: typing.Optional[int] = pydantic.Field(
        alias="last_sale_price_max", default=None
    )
    last_sale_price_min: typing.Optional[int] = pydantic.Field(
        alias="last_sale_price_min", default=None
    )
    last_update_date_max: typing.Optional[str] = pydantic.Field(
        alias="last_update_date_max", default=None
    )
    last_update_date_min: typing.Optional[str] = pydantic.Field(
        alias="last_update_date_min", default=None
    )
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    loan_type_code_first: typing.Optional[str] = pydantic.Field(
        alias="loan_type_code_first", default=None
    )
    loan_type_code_second: typing.Optional[str] = pydantic.Field(
        alias="loan_type_code_second", default=None
    )
    loan_type_code_third: typing.Optional[str] = pydantic.Field(
        alias="loan_type_code_third", default=None
    )
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    lot_size_max: typing.Optional[int] = pydantic.Field(
        alias="lot_size_max", default=None
    )
    lot_size_min: typing.Optional[int] = pydantic.Field(
        alias="lot_size_min", default=None
    )
    ltv_max: typing.Optional[str] = pydantic.Field(alias="ltv_max", default=None)
    ltv_min: typing.Optional[int] = pydantic.Field(alias="ltv_min", default=None)
    median_income: typing.Optional[int] = pydantic.Field(
        alias="median_income", default=None
    )
    median_income_max: typing.Optional[int] = pydantic.Field(
        alias="median_income_max", default=None
    )
    median_income_min: typing.Optional[int] = pydantic.Field(
        alias="median_income_min", default=None
    )
    median_income_operator: typing.Optional[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ] = pydantic.Field(alias="median_income_operator", default=None)
    mfh_2to4: typing.Optional[bool] = pydantic.Field(alias="mfh_2to4", default=None)
    mfh_5plus: typing.Optional[bool] = pydantic.Field(alias="mfh_5plus", default=None)
    mls_active: typing.Optional[bool] = pydantic.Field(alias="mls_active", default=None)
    mls_cancelled: typing.Optional[bool] = pydantic.Field(
        alias="mls_cancelled", default=None
    )
    mls_days_on_market_max: typing.Optional[int] = pydantic.Field(
        alias="mls_days_on_market_max", default=None
    )
    mls_days_on_market_min: typing.Optional[int] = pydantic.Field(
        alias="mls_days_on_market_min", default=None
    )
    mls_listing_price: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price", default=None
    )
    mls_listing_price_max: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price_max", default=None
    )
    mls_listing_price_min: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price_min", default=None
    )
    mls_listing_price_operator: typing.Optional[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ] = pydantic.Field(alias="mls_listing_price_operator", default=None)
    mls_pending: typing.Optional[bool] = pydantic.Field(
        alias="mls_pending", default=None
    )
    mls_sold: typing.Optional[bool] = pydantic.Field(alias="mls_sold", default=None)
    mortgage_max: typing.Optional[int] = pydantic.Field(
        alias="mortgage_max", default=None
    )
    mortgage_min: typing.Optional[int] = pydantic.Field(
        alias="mortgage_min", default=None
    )
    multi_polygon: typing.Optional[
        typing.List[_SerializerPropertySearchBodyMultiPolygonItem]
    ] = pydantic.Field(alias="multi_polygon", default=None)
    neighborhood_id: typing.Optional[int] = pydantic.Field(
        alias="neighborhood_id", default=None
    )
    neighborhood_name: typing.Optional[str] = pydantic.Field(
        alias="neighborhood_name", default=None
    )
    notice_type: typing.Optional[
        typing_extensions.Literal["FOR", "NOD", "NOL", "NTS", "REO"]
    ] = pydantic.Field(alias="notice_type", default=None)
    obfuscate: typing.Optional[bool] = pydantic.Field(alias="obfuscate", default=None)
    out_of_state_owner: typing.Optional[bool] = pydantic.Field(
        alias="out_of_state_owner", default=None
    )
    parcel_account_number: typing.Optional[str] = pydantic.Field(
        alias="parcel_account_number", default=None
    )
    patio: typing.Optional[bool] = pydantic.Field(alias="patio", default=None)
    polygon: typing.Optional[typing.List[_SerializerPropertySearchBodyPolygonItem]] = (
        pydantic.Field(alias="polygon", default=None)
    )
    pool: typing.Optional[bool] = pydantic.Field(alias="pool", default=None)
    pool_area_max: typing.Optional[int] = pydantic.Field(
        alias="pool_area_max", default=None
    )
    pool_area_min: typing.Optional[int] = pydantic.Field(
        alias="pool_area_min", default=None
    )
    portfolio_equity_max: typing.Optional[int] = pydantic.Field(
        alias="portfolio_equity_max", default=None
    )
    portfolio_equity_min: typing.Optional[int] = pydantic.Field(
        alias="portfolio_equity_min", default=None
    )
    portfolio_mortgage_balance_max: typing.Optional[int] = pydantic.Field(
        alias="portfolio_mortgage_balance_max", default=None
    )
    portfolio_mortgage_balance_min: typing.Optional[int] = pydantic.Field(
        alias="portfolio_mortgage_balance_min", default=None
    )
    portfolio_purchased_last12_max: typing.Optional[int] = pydantic.Field(
        alias="portfolio_purchased_last12_max", default=None
    )
    portfolio_purchased_last12_min: typing.Optional[int] = pydantic.Field(
        alias="portfolio_purchased_last12_min", default=None
    )
    portfolio_purchased_last6_max: typing.Optional[int] = pydantic.Field(
        alias="portfolio_purchased_last6_max", default=None
    )
    portfolio_purchased_last6_min: typing.Optional[int] = pydantic.Field(
        alias="portfolio_purchased_last6_min", default=None
    )
    portfolio_value_max: typing.Optional[int] = pydantic.Field(
        alias="portfolio_value_max", default=None
    )
    portfolio_value_min: typing.Optional[int] = pydantic.Field(
        alias="portfolio_value_min", default=None
    )
    pre_foreclosure: typing.Optional[bool] = pydantic.Field(
        alias="pre_foreclosure", default=None
    )
    pre_foreclosure_date_max: typing.Optional[str] = pydantic.Field(
        alias="pre_foreclosure_date_max", default=None
    )
    pre_foreclosure_date_min: typing.Optional[str] = pydantic.Field(
        alias="pre_foreclosure_date_min", default=None
    )
    prior_owner_individual: typing.Optional[bool] = pydantic.Field(
        alias="prior_owner_individual", default=None
    )
    prior_owner_months_owned_max: typing.Optional[int] = pydantic.Field(
        alias="prior_owner_months_owned_max", default=None
    )
    prior_owner_months_owned_min: typing.Optional[int] = pydantic.Field(
        alias="prior_owner_months_owned_min", default=None
    )
    private_lender: typing.Optional[bool] = pydantic.Field(
        alias="private_lender", default=None
    )
    properties_owned_max: typing.Optional[int] = pydantic.Field(
        alias="properties_owned_max", default=None
    )
    properties_owned_min: typing.Optional[int] = pydantic.Field(
        alias="properties_owned_min", default=None
    )
    property_type: typing.Optional[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ] = pydantic.Field(alias="property_type", default=None)
    property_use_code: typing.Optional[int] = pydantic.Field(
        alias="property_use_code", default=None
    )
    quit_claim: typing.Optional[bool] = pydantic.Field(alias="quit_claim", default=None)
    radius: typing.Optional[float] = pydantic.Field(alias="radius", default=None)
    reo: typing.Optional[bool] = pydantic.Field(alias="reo", default=None)
    result_index: typing.Optional[int] = pydantic.Field(
        alias="resultIndex", default=None
    )
    rooms_max: typing.Optional[int] = pydantic.Field(alias="rooms_max", default=None)
    rooms_min: typing.Optional[int] = pydantic.Field(alias="rooms_min", default=None)
    rv_parking: typing.Optional[bool] = pydantic.Field(alias="rv_parking", default=None)
    search_type: typing.Optional[
        typing_extensions.Literal["A", "C", "G", "N", "S", "T", "Z"]
    ] = pydantic.Field(alias="searchType", default=None)
    search_range: typing.Optional[
        typing_extensions.Literal["1_MONTH", "1_YEAR", "2_MONTH", "3_MONTH", "6_MONTH"]
    ] = pydantic.Field(alias="search_range", default=None)
    sewage: typing.Optional[str] = pydantic.Field(alias="sewage", default=None)
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
    sort: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="sort", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    state_id: typing.Optional[str] = pydantic.Field(alias="stateId", default=None)
    stories_max: typing.Optional[int] = pydantic.Field(
        alias="stories_max", default=None
    )
    stories_min: typing.Optional[int] = pydantic.Field(
        alias="stories_min", default=None
    )
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    summary: typing.Optional[bool] = pydantic.Field(alias="summary", default=None)
    tax_delinquent_year_max: typing.Optional[int] = pydantic.Field(
        alias="tax_delinquent_year_max", default=None
    )
    tax_delinquent_year_min: typing.Optional[int] = pydantic.Field(
        alias="tax_delinquent_year_min", default=None
    )
    tax_lien: typing.Optional[bool] = pydantic.Field(alias="tax_lien", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    trust_owned: typing.Optional[bool] = pydantic.Field(
        alias="trust_owned", default=None
    )
    units_max: typing.Optional[int] = pydantic.Field(alias="units_max", default=None)
    units_min: typing.Optional[int] = pydantic.Field(alias="units_min", default=None)
    usps_mail_state: typing.Optional[str] = pydantic.Field(
        alias="usps_mail_state", default=None
    )
    vacant: typing.Optional[bool] = pydantic.Field(alias="vacant", default=None)
    value_max: typing.Optional[int] = pydantic.Field(alias="value_max", default=None)
    value_min: typing.Optional[int] = pydantic.Field(alias="value_min", default=None)
    water_source: typing.Optional[str] = pydantic.Field(
        alias="water_source", default=None
    )
    year_built_max: typing.Optional[int] = pydantic.Field(
        alias="year_built_max", default=None
    )
    year_built_min: typing.Optional[int] = pydantic.Field(
        alias="year_built_min", default=None
    )
    year_max: typing.Optional[int] = pydantic.Field(alias="year_max", default=None)
    year_min: typing.Optional[int] = pydantic.Field(alias="year_min", default=None)
    years_owned: typing.Optional[int] = pydantic.Field(
        alias="years_owned", default=None
    )
    years_owned_max: typing.Optional[int] = pydantic.Field(
        alias="years_owned_max", default=None
    )
    years_owned_min: typing.Optional[int] = pydantic.Field(
        alias="years_owned_min", default=None
    )
    years_owned_operator: typing.Optional[
        typing_extensions.Literal["gt", "gte", "lt", "lte"]
    ] = pydantic.Field(alias="years_owned_operator", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
