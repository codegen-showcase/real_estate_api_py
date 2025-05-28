import pydantic
import pytest

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment
from real_estate_api_py.types import models


def test_chat_200_success_default():
    """Tests a POST request to the /v2/PropGPT endpoint.

    Operation: chat
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GptChatResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.gpt.chat(
        query="Find all properties listed for sale in Herndon Virginia between 600K and 700K",
        x_api_key="string",
        x_openai_key="string",
    )
    try:
        pydantic.TypeAdapter(models.GptChatResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_chat_200_success_default():
    """Tests a POST request to the /v2/PropGPT endpoint.

    Operation: chat
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GptChatResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.gpt.chat(
        query="Find all properties listed for sale in Herndon Virginia between 600K and 700K",
        x_api_key="string",
        x_openai_key="string",
    )
    try:
        pydantic.TypeAdapter(models.GptChatResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
