import pydantic
import pytest

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment


def test_chat_200_generated_success():
    """Tests a POST request to the /v2/PropGPT endpoint.

    Operation: chat
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : str

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.gpt.chat(x_api_key="string", x_openai_key="string")
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_text = True
    except pydantic.ValidationError:
        is_text = False
    assert is_text, "failed response type check"


@pytest.mark.asyncio
async def test_await_chat_200_generated_success():
    """Tests a POST request to the /v2/PropGPT endpoint.

    Operation: chat
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : str

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.gpt.chat(x_api_key="string", x_openai_key="string")
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_text = True
    except pydantic.ValidationError:
        is_text = False
    assert is_text, "failed response type check"
