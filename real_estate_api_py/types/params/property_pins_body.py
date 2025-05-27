import pydantic
import typing
import typing_extensions


class PropertyPinsBody(typing_extensions.TypedDict):
    """
    PropertyPinsBody
    """

    absentee_owner: typing_extensions.NotRequired[bool]

    address: typing_extensions.NotRequired[str]
    """
    Only use if performing a radius search around a specific fully formatted address (123 Main St, Anywhere, TX 11111)
    """

    adjustable_rate: typing_extensions.NotRequired[bool]

    assessed_improvement_value_max: typing_extensions.NotRequired[int]

    assessed_improvement_value_min: typing_extensions.NotRequired[int]

    assessed_land_value_max: typing_extensions.NotRequired[int]

    assessed_land_value_min: typing_extensions.NotRequired[int]

    assessed_value_max: typing_extensions.NotRequired[int]

    assessed_value_min: typing_extensions.NotRequired[int]

    assumable: typing_extensions.NotRequired[bool]

    attic: typing_extensions.NotRequired[bool]

    auction: typing_extensions.NotRequired[bool]

    auction_date_max: typing_extensions.NotRequired[str]

    auction_date_min: typing_extensions.NotRequired[str]

    basement: typing_extensions.NotRequired[bool]

    baths_max: typing_extensions.NotRequired[int]

    baths_min: typing_extensions.NotRequired[int]

    beds_max: typing_extensions.NotRequired[int]

    beds_min: typing_extensions.NotRequired[int]

    breezeway: typing_extensions.NotRequired[bool]

    building_size_max: typing_extensions.NotRequired[int]

    building_size_min: typing_extensions.NotRequired[int]

    carport: typing_extensions.NotRequired[bool]

    cash_buyer: typing_extensions.NotRequired[bool]

    city: typing_extensions.NotRequired[str]

    construction: typing_extensions.NotRequired[str]

    corporate_owned: typing_extensions.NotRequired[bool]

    county: typing_extensions.NotRequired[str]

    death: typing_extensions.NotRequired[bool]

    deck: typing_extensions.NotRequired[bool]

    deck_area_max: typing_extensions.NotRequired[int]

    deck_area_min: typing_extensions.NotRequired[int]

    document_type_code: typing_extensions.NotRequired[str]

    estimated_equity_max: typing_extensions.NotRequired[int]

    estimated_equity_min: typing_extensions.NotRequired[int]

    feature_balcony: typing_extensions.NotRequired[bool]

    fire_sprinklers: typing_extensions.NotRequired[bool]

    flood_zone: typing_extensions.NotRequired[bool]

    flood_zone_type: typing_extensions.NotRequired[str]

    foreclosure: typing_extensions.NotRequired[bool]

    foreclosure_date_max: typing_extensions.NotRequired[str]

    foreclosure_date_min: typing_extensions.NotRequired[str]

    free_clear: typing_extensions.NotRequired[bool]

    garage: typing_extensions.NotRequired[bool]

    high_equity: typing_extensions.NotRequired[bool]

    house: typing_extensions.NotRequired[str]

    in_state_owner: typing_extensions.NotRequired[bool]

    inherited: typing_extensions.NotRequired[bool]

    investor_buyer: typing_extensions.NotRequired[bool]

    judgment: typing_extensions.NotRequired[bool]

    last_sale_date_max: typing_extensions.NotRequired[str]

    last_sale_date_min: typing_extensions.NotRequired[str]

    last_sale_price_max: typing_extensions.NotRequired[int]

    last_sale_price_min: typing_extensions.NotRequired[int]

    latitude: typing_extensions.NotRequired[float]

    loan_type_code_first: typing_extensions.NotRequired[str]

    loan_type_code_second: typing_extensions.NotRequired[str]

    loan_type_code_third: typing_extensions.NotRequired[str]

    longitude: typing_extensions.NotRequired[float]

    lot_size_max: typing_extensions.NotRequired[int]

    lot_size_min: typing_extensions.NotRequired[int]

    ltv_max: typing_extensions.NotRequired[int]

    ltv_min: typing_extensions.NotRequired[int]

    median_income_max: typing_extensions.NotRequired[int]

    median_income_min: typing_extensions.NotRequired[int]

    mfh_2to4: typing_extensions.NotRequired[bool]

    mfh_5plus: typing_extensions.NotRequired[bool]

    mls_active: typing_extensions.NotRequired[bool]

    mls_cancelled: typing_extensions.NotRequired[bool]

    mls_days_market_max: typing_extensions.NotRequired[int]

    mls_days_on_market_min: typing_extensions.NotRequired[int]

    mls_listing_price_max: typing_extensions.NotRequired[int]

    mls_listing_price_min: typing_extensions.NotRequired[int]

    mls_pending: typing_extensions.NotRequired[bool]

    mortgage_max: typing_extensions.NotRequired[int]

    mortgage_min: typing_extensions.NotRequired[int]

    multi_polygon: typing_extensions.NotRequired[str]

    notice_type: typing_extensions.NotRequired[
        typing_extensions.Literal["FOR", "NOD", "NOL", "NTS", "REO"]
    ]

    out_of_state_owner: typing_extensions.NotRequired[bool]

    patio: typing_extensions.NotRequired[bool]

    polygon: typing_extensions.NotRequired[str]

    pool: typing_extensions.NotRequired[bool]

    pool_area_max: typing_extensions.NotRequired[int]

    pool_area_min: typing_extensions.NotRequired[int]

    portfolio_equity_max: typing_extensions.NotRequired[int]

    portfolio_equity_min: typing_extensions.NotRequired[int]

    portfolio_mortgage_balance_max: typing_extensions.NotRequired[int]

    portfolio_mortgage_balance_min: typing_extensions.NotRequired[int]

    portfolio_purchased_last12_max: typing_extensions.NotRequired[int]

    portfolio_purchased_last12_min: typing_extensions.NotRequired[int]

    portfolio_purchased_last6_max: typing_extensions.NotRequired[int]

    portfolio_purchased_last6_min: typing_extensions.NotRequired[int]

    portfolio_value_max: typing_extensions.NotRequired[int]

    portfolio_value_min: typing_extensions.NotRequired[int]

    pre_foreclosure: typing_extensions.NotRequired[bool]

    pre_foreclosure_date_max: typing_extensions.NotRequired[str]

    pre_foreclosure_date_min: typing_extensions.NotRequired[str]

    prior_owner_individual: typing_extensions.NotRequired[bool]

    prior_owner_months_owned_max: typing_extensions.NotRequired[int]

    prior_owner_months_owned_min: typing_extensions.NotRequired[int]

    private_lender: typing_extensions.NotRequired[bool]

    properties_owned_max: typing_extensions.NotRequired[int]

    properties_owned_min: typing_extensions.NotRequired[int]

    property_type: typing_extensions.NotRequired[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ]

    property_use_code: typing_extensions.NotRequired[int]
    """
    can also be an array of property use codes: [128, 392, etc.]
    """

    quit_claim: typing_extensions.NotRequired[bool]

    radius: typing_extensions.NotRequired[float]

    reo: typing_extensions.NotRequired[bool]

    result_index: typing_extensions.NotRequired[int]

    rooms_max: typing_extensions.NotRequired[int]

    rooms_min: typing_extensions.NotRequired[int]

    rv_parking: typing_extensions.NotRequired[bool]

    sewage: typing_extensions.NotRequired[str]

    size: typing_extensions.NotRequired[int]

    state: typing_extensions.NotRequired[str]

    stories_max: typing_extensions.NotRequired[int]

    stories_min: typing_extensions.NotRequired[int]

    street: typing_extensions.NotRequired[str]

    tax_delinquent_year_max: typing_extensions.NotRequired[int]

    tax_delinquent_year_min: typing_extensions.NotRequired[int]

    tax_lien: typing_extensions.NotRequired[bool]

    trust_owned: typing_extensions.NotRequired[bool]

    units_max: typing_extensions.NotRequired[int]

    units_min: typing_extensions.NotRequired[int]

    vacant: typing_extensions.NotRequired[bool]

    value_max: typing_extensions.NotRequired[int]

    value_min: typing_extensions.NotRequired[int]

    water_source: typing_extensions.NotRequired[str]

    year_built_max: typing_extensions.NotRequired[int]

    year_built_min: typing_extensions.NotRequired[int]

    years_owned_max: typing_extensions.NotRequired[int]

    years_owned_min: typing_extensions.NotRequired[int]

    zip: typing_extensions.NotRequired[str]


class _SerializerPropertyPinsBody(pydantic.BaseModel):
    """
    Serializer for PropertyPinsBody handling case conversions
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
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    construction: typing.Optional[str] = pydantic.Field(
        alias="construction", default=None
    )
    corporate_owned: typing.Optional[bool] = pydantic.Field(
        alias="corporate_owned", default=None
    )
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    death: typing.Optional[bool] = pydantic.Field(alias="death", default=None)
    deck: typing.Optional[bool] = pydantic.Field(alias="deck", default=None)
    deck_area_max: typing.Optional[int] = pydantic.Field(
        alias="deck_area_max", default=None
    )
    deck_area_min: typing.Optional[int] = pydantic.Field(
        alias="deck_area_min", default=None
    )
    document_type_code: typing.Optional[str] = pydantic.Field(
        alias="document_type_code", default=None
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
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    in_state_owner: typing.Optional[bool] = pydantic.Field(
        alias="in_state_owner", default=None
    )
    inherited: typing.Optional[bool] = pydantic.Field(alias="inherited", default=None)
    investor_buyer: typing.Optional[bool] = pydantic.Field(
        alias="investor_buyer", default=None
    )
    judgment: typing.Optional[bool] = pydantic.Field(alias="judgment", default=None)
    last_sale_date_max: typing.Optional[str] = pydantic.Field(
        alias="last_sale_date_max", default=None
    )
    last_sale_date_min: typing.Optional[str] = pydantic.Field(
        alias="last_sale_date_min", default=None
    )
    last_sale_price_max: typing.Optional[int] = pydantic.Field(
        alias="last_sale_price_max", default=None
    )
    last_sale_price_min: typing.Optional[int] = pydantic.Field(
        alias="last_sale_price_min", default=None
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
    ltv_max: typing.Optional[int] = pydantic.Field(alias="ltv_max", default=None)
    ltv_min: typing.Optional[int] = pydantic.Field(alias="ltv_min", default=None)
    median_income_max: typing.Optional[int] = pydantic.Field(
        alias="median_income_max", default=None
    )
    median_income_min: typing.Optional[int] = pydantic.Field(
        alias="median_income_min", default=None
    )
    mfh_2to4: typing.Optional[bool] = pydantic.Field(alias="mfh_2to4", default=None)
    mfh_5plus: typing.Optional[bool] = pydantic.Field(alias="mfh_5plus", default=None)
    mls_active: typing.Optional[bool] = pydantic.Field(alias="mls_active", default=None)
    mls_cancelled: typing.Optional[bool] = pydantic.Field(
        alias="mls_cancelled", default=None
    )
    mls_days_market_max: typing.Optional[int] = pydantic.Field(
        alias="mls_days_market_max", default=None
    )
    mls_days_on_market_min: typing.Optional[int] = pydantic.Field(
        alias="mls_days_on_market_min", default=None
    )
    mls_listing_price_max: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price_max", default=None
    )
    mls_listing_price_min: typing.Optional[int] = pydantic.Field(
        alias="mls_listing_price_min", default=None
    )
    mls_pending: typing.Optional[bool] = pydantic.Field(
        alias="mls_pending", default=None
    )
    mortgage_max: typing.Optional[int] = pydantic.Field(
        alias="mortgage_max", default=None
    )
    mortgage_min: typing.Optional[int] = pydantic.Field(
        alias="mortgage_min", default=None
    )
    multi_polygon: typing.Optional[str] = pydantic.Field(
        alias="multi_polygon", default=None
    )
    notice_type: typing.Optional[
        typing_extensions.Literal["FOR", "NOD", "NOL", "NTS", "REO"]
    ] = pydantic.Field(alias="notice_type", default=None)
    out_of_state_owner: typing.Optional[bool] = pydantic.Field(
        alias="out_of_state_owner", default=None
    )
    patio: typing.Optional[bool] = pydantic.Field(alias="patio", default=None)
    polygon: typing.Optional[str] = pydantic.Field(alias="polygon", default=None)
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
    sewage: typing.Optional[str] = pydantic.Field(alias="sewage", default=None)
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    stories_max: typing.Optional[int] = pydantic.Field(
        alias="stories_max", default=None
    )
    stories_min: typing.Optional[int] = pydantic.Field(
        alias="stories_min", default=None
    )
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    tax_delinquent_year_max: typing.Optional[int] = pydantic.Field(
        alias="tax_delinquent_year_max", default=None
    )
    tax_delinquent_year_min: typing.Optional[int] = pydantic.Field(
        alias="tax_delinquent_year_min", default=None
    )
    tax_lien: typing.Optional[bool] = pydantic.Field(alias="tax_lien", default=None)
    trust_owned: typing.Optional[bool] = pydantic.Field(
        alias="trust_owned", default=None
    )
    units_max: typing.Optional[int] = pydantic.Field(alias="units_max", default=None)
    units_min: typing.Optional[int] = pydantic.Field(alias="units_min", default=None)
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
    years_owned_max: typing.Optional[int] = pydantic.Field(
        alias="years_owned_max", default=None
    )
    years_owned_min: typing.Optional[int] = pydantic.Field(
        alias="years_owned_min", default=None
    )
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
