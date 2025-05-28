import pydantic
import typing


class Demographics(pydantic.BaseModel):
    """
    Demographic and rental information for the area
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fmr_efficiency: typing.Optional[str] = pydantic.Field(
        alias="fmrEfficiency", default=None
    )
    """
    Fair Market Rent for efficiency unit in USD
    """
    fmr_four_bedroom: typing.Optional[str] = pydantic.Field(
        alias="fmrFourBedroom", default=None
    )
    """
    Fair Market Rent for four bedroom unit in USD
    """
    fmr_one_bedroom: typing.Optional[str] = pydantic.Field(
        alias="fmrOneBedroom", default=None
    )
    """
    Fair Market Rent for one bedroom unit in USD
    """
    fmr_three_bedroom: typing.Optional[str] = pydantic.Field(
        alias="fmrThreeBedroom", default=None
    )
    """
    Fair Market Rent for three bedroom unit in USD
    """
    fmr_two_bedroom: typing.Optional[str] = pydantic.Field(
        alias="fmrTwoBedroom", default=None
    )
    """
    Fair Market Rent for two bedroom unit in USD
    """
    fmr_year: typing.Optional[str] = pydantic.Field(alias="fmrYear", default=None)
    """
    Fair Market Rent data year
    """
    hud_area_code: typing.Optional[str] = pydantic.Field(
        alias="hudAreaCode", default=None
    )
    """
    HUD area code
    """
    hud_area_name: typing.Optional[str] = pydantic.Field(
        alias="hudAreaName", default=None
    )
    """
    HUD area name for Fair Market Rent calculations
    """
    median_income: typing.Optional[str] = pydantic.Field(
        alias="medianIncome", default=None
    )
    """
    Median household income for the area in USD
    """
    suggested_rent: typing.Optional[str] = pydantic.Field(
        alias="suggestedRent", default=None
    )
    """
    Suggested monthly rental rate in USD
    """
