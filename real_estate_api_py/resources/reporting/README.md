
### CSV Generator API <a name="generate_csv"></a>

Generate CSV exports of property data based on search criteria. 
Useful for bulk data exports and reporting.


**API Endpoint**: `POST /v2/CSVBuilder`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.reporting.generate_csv(
    file_name="property_export_2024",
    map=["id", "address", "estimatedValue", "bedrooms", "bathrooms"],
)
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.reporting.generate_csv(
    file_name="property_export_2024",
    map=["id", "address", "estimatedValue", "bedrooms", "bathrooms"],
)
```

### Involuntary Liens API <a name="lien"></a>

Go beyond standard tax liens and add involuntary lien data to your property insights.
Includes federal tax liens, judgment liens, mechanic's liens, and other encumbrances.


**API Endpoint**: `POST /v2/Reports/PropertyLiens`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.reporting.lien(address="123 Main St, Arlington, VA 22205")
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.reporting.lien(address="123 Main St, Arlington, VA 22205")
```
