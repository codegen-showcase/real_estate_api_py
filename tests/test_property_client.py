import pydantic
import pytest
import os

from real_estate_api_py import AsyncClient, Client
from real_estate_api_py.environment import Environment
from real_estate_api_py.types import models


def test_comparables_advanced_200_success_default():
    """Tests a POST request to the /v3/PropertyComps endpoint.

    Operation: comparables_advanced
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertyComparablesAdvancedResponse

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
    response = client.property.comparables_advanced(
        address="123 Main St, Arlington, VA 22205",
        max_days_back=180,
        max_radius_miles=1.0,
        max_results=10,
    )
    try:
        pydantic.TypeAdapter(
            models.PropertyComparablesAdvancedResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_comparables_advanced_200_success_default():
    """Tests a POST request to the /v3/PropertyComps endpoint.

    Operation: comparables_advanced
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertyComparablesAdvancedResponse

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
    response = await client.property.comparables_advanced(
        address="123 Main St, Arlington, VA 22205",
        max_days_back=180,
        max_radius_miles=1.0,
        max_results=10,
    )
    try:
        pydantic.TypeAdapter(
            models.PropertyComparablesAdvancedResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_search_200_success_default():
    """Tests a POST request to the /v2/PropertySearch endpoint.

    Operation: search
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertySearchResponse

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
    response = client.property.search()
    try:
        pydantic.TypeAdapter(models.PropertySearchResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_search_200_success_default():
    """Tests a POST request to the /v2/PropertySearch endpoint.

    Operation: search
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertySearchResponse

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
    response = await client.property.search()
    try:
        pydantic.TypeAdapter(models.PropertySearchResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_pins_200_success_default():
    """Tests a POST request to the /v2/PropertyMapping endpoint.

    Operation: pins
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertyPinsResponse

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
    response = client.property.pins()
    try:
        pydantic.TypeAdapter(models.PropertyPinsResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_pins_200_success_default():
    """Tests a POST request to the /v2/PropertyMapping endpoint.

    Operation: pins
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertyPinsResponse

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
    response = await client.property.pins()
    try:
        pydantic.TypeAdapter(models.PropertyPinsResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_bulk_details_200_success_default():
    """Tests a POST request to the /v2/PropertyDetailBulk endpoint.

    Operation: bulk_details
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertyBulkDetailsResponse

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
    response = client.property.bulk_details(ids=["string"])
    try:
        pydantic.TypeAdapter(models.PropertyBulkDetailsResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_bulk_details_200_success_default():
    """Tests a POST request to the /v2/PropertyDetailBulk endpoint.

    Operation: bulk_details
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertyBulkDetailsResponse

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
    response = await client.property.bulk_details(ids=["string"])
    try:
        pydantic.TypeAdapter(models.PropertyBulkDetailsResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_details_200_success_default():
    """Tests a POST request to the /v2/PropertyDetail endpoint.

    Operation: details
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertyDetailsResponse

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
    response = client.property.details()
    try:
        pydantic.TypeAdapter(models.PropertyDetailsResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_details_200_success_default():
    """Tests a POST request to the /v2/PropertyDetail endpoint.

    Operation: details
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertyDetailsResponse

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
    response = await client.property.details()
    try:
        pydantic.TypeAdapter(models.PropertyDetailsResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_comparables_200_success_default():
    """Tests a POST request to the /v2/PropertyComps endpoint.

    Operation: comparables
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertyComparablesResponse

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
    response = client.property.comparables()
    try:
        pydantic.TypeAdapter(models.PropertyComparablesResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_comparables_200_success_default():
    """Tests a POST request to the /v2/PropertyComps endpoint.

    Operation: comparables
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertyComparablesResponse

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
    response = await client.property.comparables()
    try:
        pydantic.TypeAdapter(models.PropertyComparablesResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_parcel_200_success_default():
    """Tests a POST request to the /v1/PropertyParcel endpoint.

    Operation: parcel
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PropertyParcelResponse

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
    response = client.property.parcel()
    try:
        pydantic.TypeAdapter(models.PropertyParcelResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_parcel_200_success_default():
    """Tests a POST request to the /v1/PropertyParcel endpoint.

    Operation: parcel
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PropertyParcelResponse

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
    response = await client.property.parcel()
    try:
        pydantic.TypeAdapter(models.PropertyParcelResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
