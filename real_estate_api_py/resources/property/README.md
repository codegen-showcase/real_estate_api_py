
### CSV Generator API <a name="generate_csv"></a>



**API Endpoint**: `POST /v2/CSVBuilder`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.generate_csv()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.generate_csv()
```

### v2/PropertyComps API <a name="comps_standard"></a>



**API Endpoint**: `POST /v2/PropertyComps`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.comps_standard()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.comps_standard()
```

### Property Detail API <a name="details"></a>

Comps, Mortgages, Mailing Addresses, Property Sales History & More!

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

### Property Detail Bulk API <a name="details_bulk"></a>

For retrieving of up to 1000 properties at once.  Can be used standalone, but it's designed to work together with the Property Search API.  Use this API for quickly exporting lists, or bulk search requests for analytics.  Pass in addresses, or a list of ID's returned from the Property Search API.

**API Endpoint**: `POST /v2/PropertyDetailBulk`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.details_bulk()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.details_bulk()
```

### [BETA] Mapping ("Pins") API <a name="pins"></a>

Have your PropTech Maps Come to Life with Unlimited "Pins" on a Map API. Only available on Growth+ Plans

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

Searchable API for list building, search counts, and advanced filtering on properties.  You can also use this API to implement your own comparables API, or property analytics API.  Questions?  Contact our team to ask us for best practices with using this API.This API implements easy paging so your apps can easily manage filtered results in a results pane with paging.  When your user clicks on a result, just use the id from this API to get the full property results using the Property Detail API.  Questions on best practices for implementing paged property results in your app?  Just contact our team.

**API Endpoint**: `POST /v2/PropertySearch`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.search(x_api_key="string")
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.search(x_api_key="string")
```

### /v3/PropertyComps API <a name="comps_custom"></a>

Customize your comps model

**API Endpoint**: `POST /v3/PropertyComps`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.property.comps_custom()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.property.comps_custom()
```
