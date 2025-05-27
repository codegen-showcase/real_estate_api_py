
### PropGPT API <a name="chat"></a>

Check out the functionality of this endpoint at https://www.propgpt.com

**API Endpoint**: `POST /v2/PropGPT`

#### Synchronous Client

```python
from os import getenv
from real_estate_api_py import Client

client = Client(api_key=getenv("API_KEY"))
res = client.gpt.chat(x_api_key="string", x_openai_key="string")
```

#### Asynchronous Client

```python
from os import getenv
from real_estate_api_py import AsyncClient

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.gpt.chat(x_api_key="string", x_openai_key="string")
```
