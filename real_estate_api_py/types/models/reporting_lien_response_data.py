import pydantic
import typing

from .property_address import PropertyAddress
from .reporting_lien_response_data_liens_item import ReportingLienResponseDataLiensItem


class ReportingLienResponseData(pydantic.BaseModel):
    """
    ReportingLienResponseData
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
    lien_count: typing.Optional[int] = pydantic.Field(alias="lienCount", default=None)
    """
    Total number of liens found
    """
    liens: typing.Optional[typing.List[ReportingLienResponseDataLiensItem]] = (
        pydantic.Field(alias="liens", default=None)
    )
    property_id: typing.Optional[str] = pydantic.Field(alias="propertyId", default=None)
    """
    Unique property identifier
    """
    total_lien_amount: typing.Optional[int] = pydantic.Field(
        alias="totalLienAmount", default=None
    )
    """
    Total amount of all liens in USD
    """
