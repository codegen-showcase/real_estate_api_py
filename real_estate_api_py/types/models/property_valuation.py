import pydantic
import typing


class PropertyValuation(pydantic.BaseModel):
    """
    Property valuation and equity information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

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
