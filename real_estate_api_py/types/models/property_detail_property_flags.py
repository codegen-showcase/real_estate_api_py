import pydantic
import typing


class PropertyDetailPropertyFlags(pydantic.BaseModel):
    """
    PropertyDetailPropertyFlags
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

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
