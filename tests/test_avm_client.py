import pydantic
import pytest
import os

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment
from real_estate_api_py.types import models


def test_get_valuation_200_success_default():
    """Tests a POST request to the /v2/PropertyAvm endpoint.

    Operation: get_valuation
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.AvmGetValuationResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        api_key=os.getenv("REAL_ESTATE_API_KEY"), environment=Environment.PRODUCTION
    )
    response = client.avm.get_valuation(address="123 Main St, Arlington, VA 22205")
    try:
        pydantic.TypeAdapter(models.AvmGetValuationResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_valuation_200_success_default():
    """Tests a POST request to the /v2/PropertyAvm endpoint.

    Operation: get_valuation
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.AvmGetValuationResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        api_key=os.getenv("REAL_ESTATE_API_KEY"), environment=Environment.PRODUCTION
    )
    response = await client.avm.get_valuation(
        address="123 Main St, Arlington, VA 22205"
    )
    try:
        pydantic.TypeAdapter(models.AvmGetValuationResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
