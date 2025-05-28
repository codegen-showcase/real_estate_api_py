import pydantic
import typing
import typing_extensions


class ReportingGenerateCsvResponseData(pydantic.BaseModel):
    """
    ReportingGenerateCsvResponseData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    download_url: typing.Optional[str] = pydantic.Field(
        alias="downloadUrl", default=None
    )
    """
    URL to download the CSV file (available when completed)
    """
    estimated_records: typing.Optional[int] = pydantic.Field(
        alias="estimatedRecords", default=None
    )
    """
    Estimated number of records to be exported
    """
    file_name: typing.Optional[str] = pydantic.Field(alias="fileName", default=None)
    """
    Name of the generated CSV file
    """
    job_id: typing.Optional[str] = pydantic.Field(alias="jobId", default=None)
    """
    Unique identifier for the CSV generation job
    """
    status: typing.Optional[
        typing_extensions.Literal["completed", "failed", "processing", "queued"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Current status of the export job
    """
