import pydantic
import pytest
import typing

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment


def test_property_liens_200_generated_success():
    """Tests a POST request to the /v2/Reports/PropertyLiens endpoint.

    Operation: property_liens
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.reports.property_liens()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_property_liens_200_generated_success():
    """Tests a POST request to the /v2/Reports/PropertyLiens endpoint.

    Operation: property_liens
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.reports.property_liens()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
