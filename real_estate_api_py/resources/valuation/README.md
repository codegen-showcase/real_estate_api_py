
### Lender Grade AVM API <a name="avm"></a>

Need the most precise Valuations for properties possible? Try out our Lender Grade AVM that uses statistical modeling, recent sales data, and market-to-market analysis to produce reliable AVMs

**API Endpoint**: `POST /v2/PropertyAvm`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.valuation.avm()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.valuation.avm()
```
