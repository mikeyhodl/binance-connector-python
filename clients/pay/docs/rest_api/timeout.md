# Timeout

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_pay.pay import Pay
from binance_sdk_pay.rest_api.models import GetPayTradeHistoryResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
)
client =  Pay(config_rest_api=configuration)

try:
    response = client.rest_api.get_pay_trade_history(startTimestamp=1637186702000, limit=50)
    data: GetPayTradeHistoryResponse = response.data()
    print(data)
except Exception as e:
    logging.error(f"error: {e}")
```
