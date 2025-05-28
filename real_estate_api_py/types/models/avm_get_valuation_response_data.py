import pydantic
import typing

from .property_address import PropertyAddress
from .property_search_result import PropertySearchResult


class AvmGetValuationResponseData(pydantic.BaseModel):
    """
    AvmGetValuationResponseData
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
    avm_value: typing.Optional[int] = pydantic.Field(alias="avmValue", default=None)
    """
    Automated Valuation Model estimate in USD
    """
    comparables: typing.Optional[typing.List[PropertySearchResult]] = pydantic.Field(
        alias="comparables", default=None
    )
    """
    Properties used in valuation calculation
    """
    confidence: typing.Optional[float] = pydantic.Field(
        alias="confidence", default=None
    )
    """
    Confidence score for the valuation (0-1)
    """
    fsd: typing.Optional[float] = pydantic.Field(alias="fsd", default=None)
    """
    Forecast Standard Deviation
    """
    property_id: typing.Optional[str] = pydantic.Field(alias="propertyId", default=None)
    """
    Unique property identifier
    """
    valuation_date: typing.Optional[str] = pydantic.Field(
        alias="valuationDate", default=None
    )
    """
    Date of the valuation
    """
