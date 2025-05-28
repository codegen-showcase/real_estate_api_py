import pydantic
import typing

from .property_detail import PropertyDetail
from .property_search_result import PropertySearchResult


class PropertyComparablesResponseData(pydantic.BaseModel):
    """
    PropertyComparablesResponseData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    comps: typing.Optional[typing.List[PropertySearchResult]] = pydantic.Field(
        alias="comps", default=None
    )
    reapi_avm: typing.Optional[int] = pydantic.Field(alias="reapiAvm", default=None)
    """
    RealEstateAPI's Automated Valuation Model estimate
    """
    record_count: typing.Optional[int] = pydantic.Field(
        alias="recordCount", default=None
    )
    """
    Number of comparable properties returned
    """
    subject: typing.Optional[PropertyDetail] = pydantic.Field(
        alias="subject", default=None
    )
    """
    Complete property details
    """
