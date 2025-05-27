
# Property APIs Python SDK

## Overview
real-estate-api (1.0)

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
```

## Module Documentation and Snippets

### [address](real_estate_api_py/resources/address/README.md)

* [verify](real_estate_api_py/resources/address/README.md#verify) - Address Verification API

### [gpt](real_estate_api_py/resources/gpt/README.md)

* [chat](real_estate_api_py/resources/gpt/README.md#chat) - PropGPT API

### [property](real_estate_api_py/resources/property/README.md)

* [comps_custom](real_estate_api_py/resources/property/README.md#comps_custom) - /v3/PropertyComps API
* [comps_standard](real_estate_api_py/resources/property/README.md#comps_standard) - v2/PropertyComps API
* [details](real_estate_api_py/resources/property/README.md#details) - Property Detail API
* [details_bulk](real_estate_api_py/resources/property/README.md#details_bulk) - Property Detail Bulk API
* [generate_csv](real_estate_api_py/resources/property/README.md#generate_csv) - CSV Generator API
* [pins](real_estate_api_py/resources/property/README.md#pins) - [BETA] Mapping ("Pins") API
* [search](real_estate_api_py/resources/property/README.md#search) - Property Search API

### [reports](real_estate_api_py/resources/reports/README.md)

* [property_liens](real_estate_api_py/resources/reports/README.md#property_liens) - Involuntary Liens API

### [valuation](real_estate_api_py/resources/valuation/README.md)

* [avm](real_estate_api_py/resources/valuation/README.md#avm) - Lender Grade AVM API

<!-- MODULE DOCS END -->
