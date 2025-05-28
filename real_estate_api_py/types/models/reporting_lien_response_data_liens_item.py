import pydantic
import typing
import typing_extensions


class ReportingLienResponseDataLiensItem(pydantic.BaseModel):
    """
    ReportingLienResponseDataLiensItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    Lien amount in USD
    """
    document_number: typing.Optional[str] = pydantic.Field(
        alias="documentNumber", default=None
    )
    """
    Recording document number
    """
    lien_holder: typing.Optional[str] = pydantic.Field(alias="lienHolder", default=None)
    """
    Name of the lien holder
    """
    recording_date: typing.Optional[str] = pydantic.Field(
        alias="recordingDate", default=None
    )
    """
    Date the lien was recorded
    """
    release_date: typing.Optional[str] = pydantic.Field(
        alias="releaseDate", default=None
    )
    """
    Date the lien was released (if applicable)
    """
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "EXPIRED", "RELEASED", "SATISFIED"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Current status of the lien
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "FEDERAL_TAX_LIEN", "JUDGMENT_LIEN", "MECHANICS_LIEN", "OTHER", "TAX_LIEN"
        ]
    ] = pydantic.Field(alias="type", default=None)
    """
    Type of lien
    """
