
### Lender Grade AVM API <a name="get_valuation"></a>

Get the most precise property valuations using our lender-grade Automated Valuation Model 
that uses statistical modeling, recent sales data, and market-to-market analysis.


**API Endpoint**: `POST /v2/PropertyAvm`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.avm.get_valuation(address="123 Main St, Arlington, VA 22205")
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.avm.get_valuation(address="123 Main St, Arlington, VA 22205")
```
