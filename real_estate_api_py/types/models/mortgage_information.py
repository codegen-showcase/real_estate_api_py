import pydantic
import typing
import typing_extensions


class MortgageInformation(pydantic.BaseModel):
    """
    Mortgage and financing details
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    Original mortgage amount in USD
    """
    deed_type: typing.Optional[str] = pydantic.Field(alias="deedType", default=None)
    """
    Type of deed or mortgage document
    """
    document_date: typing.Optional[str] = pydantic.Field(
        alias="documentDate", default=None
    )
    """
    Date the mortgage document was created
    """
    grantee_name: typing.Optional[str] = pydantic.Field(
        alias="granteeName", default=None
    )
    """
    Name of the grantee (borrower)
    """
    interest_rate: typing.Optional[float] = pydantic.Field(
        alias="interestRate", default=None
    )
    """
    Interest rate as a percentage
    """
    interest_rate_type: typing.Optional[
        typing_extensions.Literal["ADJUSTABLE RATE", "FIXED RATE", "UNKNOWN"]
    ] = pydantic.Field(alias="interestRateType", default=None)
    """
    Type of interest rate
    """
    lender_name: typing.Optional[str] = pydantic.Field(alias="lenderName", default=None)
    """
    Name of the lending institution
    """
    loan_type: typing.Optional[str] = pydantic.Field(alias="loanType", default=None)
    """
    Type of loan
    """
    maturity_date: typing.Optional[str] = pydantic.Field(
        alias="maturityDate", default=None
    )
    """
    Mortgage maturity date (timestamp format)
    """
    position: typing.Optional[str] = pydantic.Field(alias="position", default=None)
    """
    Mortgage position (First, Second, etc.)
    """
    recording_date: typing.Optional[str] = pydantic.Field(
        alias="recordingDate", default=None
    )
    """
    Date the mortgage was recorded
    """
    seq: typing.Optional[str] = pydantic.Field(alias="seq", default=None)
    """
    Sequence number for this mortgage record
    """
    term: typing.Optional[str] = pydantic.Field(alias="term", default=None)
    """
    Loan term in months
    """
    term_type: typing.Optional[str] = pydantic.Field(alias="termType", default=None)
    """
    Term type description
    """
    transaction_type: typing.Optional[str] = pydantic.Field(
        alias="transactionType", default=None
    )
    """
    Type of transaction
    """
