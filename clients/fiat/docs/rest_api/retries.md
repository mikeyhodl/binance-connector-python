# Retries Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_fiat.fiat import Fiat
from binance_sdk_fiat.rest_api.models import GetFiatDepositWithdrawHistoryResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
    retries=2
)
client = Fiat(config_rest_api=configuration)

try:
    response = client.rest_api.get_fiat_deposit_withdraw_history()
    data: GetFiatDepositWithdrawHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
