# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_convert.convert import Convert
from binance_sdk_convert.rest_api.models import ListAllConvertPairsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    proxy = {
        "host": "127.0.0.1",
        "port": 8080,
        "protocol": "http", # or 'https'
        "auth": {
            "username": "proxy-user",
            "password": "proxy-password",
        },
    }
)
client = Convert(config_rest_api=configuration)

try:
    response = client.rest_api.list_all_convert_pairs()
    data: ListAllConvertPairsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
