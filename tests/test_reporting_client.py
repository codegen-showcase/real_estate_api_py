import pydantic
import pytest

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment
from real_estate_api_py.types import models


def test_lien_200_success_default():
    """Tests a POST request to the /v2/Reports/PropertyLiens endpoint.

    Operation: lien
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportingLienResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.reporting.lien(address="123 Main St, Arlington, VA 22205")
    try:
        pydantic.TypeAdapter(models.ReportingLienResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_lien_200_success_default():
    """Tests a POST request to the /v2/Reports/PropertyLiens endpoint.

    Operation: lien
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportingLienResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.reporting.lien(address="123 Main St, Arlington, VA 22205")
    try:
        pydantic.TypeAdapter(models.ReportingLienResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_generate_csv_200_success_default():
    """Tests a POST request to the /v2/CSVBuilder endpoint.

    Operation: generate_csv
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportingGenerateCsvResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.reporting.generate_csv(
        file_name="property_export_2024",
        map=["id", "address", "estimatedValue", "bedrooms", "bathrooms"],
    )
    try:
        pydantic.TypeAdapter(models.ReportingGenerateCsvResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_generate_csv_200_success_default():
    """Tests a POST request to the /v2/CSVBuilder endpoint.

    Operation: generate_csv
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportingGenerateCsvResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.reporting.generate_csv(
        file_name="property_export_2024",
        map=["id", "address", "estimatedValue", "bedrooms", "bathrooms"],
    )
    try:
        pydantic.TypeAdapter(models.ReportingGenerateCsvResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
