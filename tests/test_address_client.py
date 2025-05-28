import pydantic
import pytest

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment
from real_estate_api_py.types import models


def test_auto_complete_200_success_default():
    """Tests a POST request to the /v2/AutoComplete endpoint.

    Operation: auto_complete
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.AddressAutoCompleteResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.address.auto_complete(search="string")
    try:
        pydantic.TypeAdapter(models.AddressAutoCompleteResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_auto_complete_200_success_default():
    """Tests a POST request to the /v2/AutoComplete endpoint.

    Operation: auto_complete
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.AddressAutoCompleteResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.address.auto_complete(search="string")
    try:
        pydantic.TypeAdapter(models.AddressAutoCompleteResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_verify_200_success_default():
    """Tests a POST request to the /v2/AddressVerification endpoint.

    Operation: verify
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.AddressVerifyResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.address.verify()
    try:
        pydantic.TypeAdapter(models.AddressVerifyResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_verify_200_success_default():
    """Tests a POST request to the /v2/AddressVerification endpoint.

    Operation: verify
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.AddressVerifyResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.address.verify()
    try:
        pydantic.TypeAdapter(models.AddressVerifyResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
