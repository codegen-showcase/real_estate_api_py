
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

* [auto_complete](real_estate_api_py/resources/address/README.md#auto_complete) - AutoComplete API
* [verify](real_estate_api_py/resources/address/README.md#verify) - Address Verification API

### [avm](real_estate_api_py/resources/avm/README.md)

* [get_valuation](real_estate_api_py/resources/avm/README.md#get_valuation) - Lender Grade AVM API

### [gpt](real_estate_api_py/resources/gpt/README.md)

* [chat](real_estate_api_py/resources/gpt/README.md#chat) - PropGPT API

### [property](real_estate_api_py/resources/property/README.md)

* [bulk_details](real_estate_api_py/resources/property/README.md#bulk_details) - Property Detail Bulk API
* [comparables](real_estate_api_py/resources/property/README.md#comparables) - Property Comparables API v2
* [comparables_advanced](real_estate_api_py/resources/property/README.md#comparables_advanced) - Property Comparables API v3
* [details](real_estate_api_py/resources/property/README.md#details) - Property Detail API
* [parcel](real_estate_api_py/resources/property/README.md#parcel) - Property Boundary API
* [pins](real_estate_api_py/resources/property/README.md#pins) - Mapping (Pins) API [BETA]
* [search](real_estate_api_py/resources/property/README.md#search) - Property Search API

### [reporting](real_estate_api_py/resources/reporting/README.md)

* [generate_csv](real_estate_api_py/resources/reporting/README.md#generate_csv) - CSV Generator API
* [lien](real_estate_api_py/resources/reporting/README.md#lien) - Involuntary Liens API

<!-- MODULE DOCS END -->
