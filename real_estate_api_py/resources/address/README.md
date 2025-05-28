
### Address Verification API <a name="verify"></a>

Verify 1 - 100 addresses at a time for accuracy and standardization.


**API Endpoint**: `POST /v2/AddressVerification`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.address.verify(addresses=[{}])
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.address.verify(addresses=[{}])
```

### AutoComplete API <a name="auto_complete"></a>

The AutoComplete approximates like property searches based on incomplete address parts and combinations. 
Our AutoComplete algorithms are powered by machine learning and give you rich property lists 
without having to design tons of different Property Search queries.


**API Endpoint**: `POST /v2/AutoComplete`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.address.auto_complete(search="string")
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.address.auto_complete(search="string")
```
