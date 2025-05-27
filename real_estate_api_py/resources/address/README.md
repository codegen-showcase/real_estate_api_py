
### Address Verification API <a name="verify"></a>

Verify 1 - 100 addresses at a time.

**API Endpoint**: `POST /v2/AddressVerification`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.address.verify()
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.address.verify()
```
