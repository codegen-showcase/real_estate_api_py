import pydantic
import typing
import typing_extensions


class SalesHistoryRecord(pydantic.BaseModel):
    """
    Historical sales transaction record
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buyer_names: typing.Optional[str] = pydantic.Field(alias="buyerNames", default=None)
    """
    Names of the buyers
    """
    document_type: typing.Optional[str] = pydantic.Field(
        alias="documentType", default=None
    )
    """
    Type of sale document
    """
    down_payment: typing.Optional[int] = pydantic.Field(
        alias="downPayment", default=None
    )
    """
    Down payment amount in USD
    """
    ltv: typing.Optional[float] = pydantic.Field(alias="ltv", default=None)
    """
    Loan-to-value ratio as a percentage
    """
    purchase_method: typing.Optional[
        typing_extensions.Literal["Cash Purchase", "Financed", "Unknown"]
    ] = pydantic.Field(alias="purchaseMethod", default=None)
    """
    Method of purchase (Cash, Financed, etc.)
    """
    recording_date: typing.Optional[str] = pydantic.Field(
        alias="recordingDate", default=None
    )
    """
    Date the sale was recorded
    """
    sale_amount: typing.Optional[int] = pydantic.Field(alias="saleAmount", default=None)
    """
    Sale price in USD
    """
    sale_date: typing.Optional[str] = pydantic.Field(alias="saleDate", default=None)
    """
    Actual sale date
    """
    seller_names: typing.Optional[str] = pydantic.Field(
        alias="sellerNames", default=None
    )
    """
    Names of the sellers
    """
    seq: typing.Optional[int] = pydantic.Field(alias="seq", default=None)
    """
    Sequence number for this sales record
    """
    transaction_type: typing.Optional[str] = pydantic.Field(
        alias="transactionType", default=None
    )
    """
    Type of transaction
    """
