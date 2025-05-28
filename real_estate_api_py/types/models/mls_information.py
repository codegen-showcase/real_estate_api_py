import pydantic
import typing


class MlsInformation(pydantic.BaseModel):
    """
    Multiple Listing Service (MLS) information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

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
