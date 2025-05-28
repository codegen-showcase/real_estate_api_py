import pydantic
import typing


class TaxInformation(pydantic.BaseModel):
    """
    Property tax information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assessment_year: typing.Optional[int] = pydantic.Field(
        alias="assessmentYear", default=None
    )
    """
    Year of the assessment
    """
    property_id: typing.Optional[str] = pydantic.Field(alias="propertyId", default=None)
    """
    Property identifier for tax records
    """
    tax_amount: typing.Optional[int] = pydantic.Field(alias="taxAmount", default=None)
    """
    Annual property tax amount in cents
    """
    year: typing.Optional[int] = pydantic.Field(alias="year", default=None)
    """
    Tax year
    """
