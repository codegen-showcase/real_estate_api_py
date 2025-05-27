
### Involuntary Liens API <a name="property_liens"></a>

Go beyond our standard tax_liens & add Involuntary Lien Data to your Insights on a Property

**API Endpoint**: `POST /v2/Reports/PropertyLiens`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.reports.property_liens()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.reports.property_liens()
```
