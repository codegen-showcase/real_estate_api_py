
### Property Boundary API <a name="parcel"></a>

Shape files API and property search API. All requests return the parcel boundaries 
in GEOJSON format. Quickly implement this API into your mapping applications.


**API Endpoint**: `POST /v1/PropertyParcel`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.parcel()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.parcel()
```

### Property Comparables API v2 <a name="comparables"></a>

Generate property comparables (comps) for valuation analysis using our standard algorithm.


**API Endpoint**: `POST /v2/PropertyComps`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.comparables()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.comparables()
```

### Property Detail API <a name="details"></a>

Comprehensive property information including comps, mortgages, mailing addresses, 
property sales history & more!


**API Endpoint**: `POST /v2/PropertyDetail`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.details()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.details()
```

### Property Detail Bulk API <a name="bulk_details"></a>

For retrieving up to 1000 properties at once. Can be used standalone, but it's designed 
to work together with the Property Search API. Use this API for quickly exporting lists, 
or bulk search requests for analytics.


**API Endpoint**: `POST /v2/PropertyDetailBulk`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.bulk_details(ids=["string"])
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.bulk_details(ids=["string"])
```

### Mapping (Pins) API [BETA] <a name="pins"></a>

Create unlimited map pins for PropTech mapping applications. 
Returns property data optimized for map display with coordinates and summary information.
Only available on Growth+ Plans.


**API Endpoint**: `POST /v2/PropertyMapping`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.pins()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.pins()
```

### Property Search API <a name="search"></a>

Searchable API for list building, search counts, and advanced filtering on properties. 
You can also use this API to implement your own comparables API, or property analytics API.

This API implements easy paging so your apps can easily manage filtered results in a results pane with paging. 
When your user clicks on a result, just use the id from this API to get the full property results using the Property Detail API.


**API Endpoint**: `POST /v2/PropertySearch`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.search()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.search()
```

### Property Comparables API v3 <a name="comparables_advanced"></a>

Advanced property comparables API with customizable comp model parameters 
for more precise valuation analysis.


**API Endpoint**: `POST /v3/PropertyComps`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.comparables_advanced(
    address="123 Main St, Arlington, VA 22205",
    max_days_back=180,
    max_radius_miles=1.0,
    max_results=10,
)
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.comparables_advanced(
    address="123 Main St, Arlington, VA 22205",
    max_days_back=180,
    max_radius_miles=1.0,
    max_results=10,
)
```
