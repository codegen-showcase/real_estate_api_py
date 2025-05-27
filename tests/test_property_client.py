import pydantic
import pytest
import typing

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment
from real_estate_api_py.types import models


def test_comps_custom_200_generated_success():
    """Tests a POST request to the /v3/PropertyComps endpoint.

    Operation: comps_custom
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
    response = client.property.comps_custom()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_comps_custom_200_generated_success():
    """Tests a POST request to the /v3/PropertyComps endpoint.

    Operation: comps_custom
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
    response = await client.property.comps_custom()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_search_200_generated_success():
    """Tests a POST request to the /v2/PropertySearch endpoint.

    Operation: search
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.PropertySearchResponseObj0, models.PropertySearchResponseObj1, models.PropertySearchResponseObj2, models.PropertySearchResponseObj3]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.property.search(x_api_key="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[
                models.PropertySearchResponseObj0,
                models.PropertySearchResponseObj1,
                models.PropertySearchResponseObj2,
                models.PropertySearchResponseObj3,
            ]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_search_200_generated_success():
    """Tests a POST request to the /v2/PropertySearch endpoint.

    Operation: search
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.PropertySearchResponseObj0, models.PropertySearchResponseObj1, models.PropertySearchResponseObj2, models.PropertySearchResponseObj3]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.property.search(x_api_key="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[
                models.PropertySearchResponseObj0,
                models.PropertySearchResponseObj1,
                models.PropertySearchResponseObj2,
                models.PropertySearchResponseObj3,
            ]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_pins_200_generated_success():
    """Tests a POST request to the /v2/PropertyMapping endpoint.

    Operation: pins
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
    response = client.property.pins()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_pins_200_generated_success():
    """Tests a POST request to the /v2/PropertyMapping endpoint.

    Operation: pins
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
    response = await client.property.pins()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_details_bulk_200_generated_success():
    """Tests a POST request to the /v2/PropertyDetailBulk endpoint.

    Operation: details_bulk
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Any

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.property.details_bulk()
    try:
        pydantic.TypeAdapter(typing.Any).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_details_bulk_200_generated_success():
    """Tests a POST request to the /v2/PropertyDetailBulk endpoint.

    Operation: details_bulk
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Any

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.property.details_bulk()
    try:
        pydantic.TypeAdapter(typing.Any).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_details_200_generated_success():
    """Tests a POST request to the /v2/PropertyDetail endpoint.

    Operation: details
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Any

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.property.details()
    try:
        pydantic.TypeAdapter(typing.Any).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_details_200_generated_success():
    """Tests a POST request to the /v2/PropertyDetail endpoint.

    Operation: details
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Any

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.property.details()
    try:
        pydantic.TypeAdapter(typing.Any).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_comps_standard_200_generated_success():
    """Tests a POST request to the /v2/PropertyComps endpoint.

    Operation: comps_standard
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Any

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.property.comps_standard()
    try:
        pydantic.TypeAdapter(typing.Any).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_comps_standard_200_generated_success():
    """Tests a POST request to the /v2/PropertyComps endpoint.

    Operation: comps_standard
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Any

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.property.comps_standard()
    try:
        pydantic.TypeAdapter(typing.Any).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_generate_csv_200_generated_success():
    """Tests a POST request to the /v2/CSVBuilder endpoint.

    Operation: generate_csv
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
    response = client.property.generate_csv()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_generate_csv_200_generated_success():
    """Tests a POST request to the /v2/CSVBuilder endpoint.

    Operation: generate_csv
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
    response = await client.property.generate_csv()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
