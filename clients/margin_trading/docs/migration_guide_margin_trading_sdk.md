# Migration Guide: Binance Margin Trading SDK Modularization

With the transition to a modularized structure, the Binance Connector has been split into separate Python libraries, each focusing on a distinct product (e.g., Spot, Futures, etc.). This guide explains how to migrate from the monolithic `binance-connector` package to the new `binance-sdk-margin-trading` library.

---

## Key Changes

1. **Package Name**:  
   The modularised Margin Trading Connector has been moved to a new package:

   **Old:** `binance-connector`  
   **New:** `binance-sdk-margin-trading`

2. **Installation**:  
   Uninstall the old package and install the new one:

   ```bash
   pip uninstall binance-connector
   pip install binance-sdk-margin-trading
   ```

3. **Imports**:  
   Update your import paths.  

   **Old:**

   ```python
   from binance.spot import Spot as Client
   ```

   **New:**

   ```python
   from binance_sdk_margin_trading.margin_trading import MarginTrading, ConfigurationRestAPI
   ```

4. **Configuration and Client Initialization**:  
   The new structure keeps the existing configuration options but modularizes clients into `MarginTrading`.

   **Old:**

   ```python
   from binance.spot import Spot as Client

   client = Client(api_key="your-key", api_secret="your-secret")
   response = client.get_small_liability_exchange_coin_list()
   print(response)
   ```

   **New:**

   ```python
   from binance_sdk_margin_trading.margin_trading import MarginTrading, ConfigurationRestAPI

   configuration = ConfigurationRestAPI(
      api_key="your-key",
      api_secret="your-secret"
   )
   client = MarginTrading(config_rest_api=configuration)
      
   response = client.rest_api.get_small_liability_exchange_coin_list()
   ```

5. **Examples and Documentation**:  
   Updated examples can be found in the new repository folders:
   - REST API: `examples/rest_api/`
   - WebSocket Streams: `examples/websocket_streams/`

---

## Migration Steps

### 1. Uninstall the Old Package

Remove the old package from your project:

```bash
pip uninstall binance-connector
```

### 2. Install the New Package

Install the new MarginTrading-specific package:

```bash
pip install binance-sdk-margin-trading
```

### 3. Update Import Paths

Replace all occurrences of:

```python
from binance.spot import Spot as Client
```

With:

```python
from binance_sdk_margin_trading.margin_trading import MarginTrading
```

### 4. Update Client Initialization

Adjust your code to use the modularized structure. For example:

**Old:**

```python
client = Client(apiKey='your-key', apiSecret='your-secret')
```

**New:**

```python
from binance_sdk_margin_trading.margin_trading import MarginTrading, ConfigurationRestAPI

configuration = ConfigurationRestAPI(
    api_key="your-key",
    api_secret="your-secret"
)
client = MarginTrading(config_rest_api=configuration)
```

### 5. Test and Verify

Run your application to ensure everything works as expected. Refer to the new documentation for any advanced features or configuration options.

---

## Additional Notes

- **Future Modular Packages**: Similar packages for other products (e.g., Wallet, Staking) will follow this pattern.

For more details, refer to the updated [README](../README.md) and [Examples](../examples/).
