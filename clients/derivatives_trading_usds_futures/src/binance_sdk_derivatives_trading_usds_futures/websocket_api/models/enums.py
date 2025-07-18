"""
Binance Derivatives Trading USDS Futures WebSocket API

OpenAPI Specification for the Binance Derivatives Trading USDS Futures WebSocket API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from enum import Enum


class ModifyOrderSideEnum(Enum):
    BUY = "BUY"
    SELL = "SELL"


class ModifyOrderPriceMatchEnum(Enum):
    NONE = "NONE"
    OPPONENT = "OPPONENT"
    OPPONENT_5 = "OPPONENT_5"
    OPPONENT_10 = "OPPONENT_10"
    OPPONENT_20 = "OPPONENT_20"
    QUEUE = "QUEUE"
    QUEUE_5 = "QUEUE_5"
    QUEUE_10 = "QUEUE_10"
    QUEUE_20 = "QUEUE_20"


class NewOrderSideEnum(Enum):
    BUY = "BUY"
    SELL = "SELL"


class NewOrderPositionSideEnum(Enum):
    BOTH = "BOTH"
    LONG = "LONG"
    SHORT = "SHORT"


class NewOrderTimeInForceEnum(Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"
    GTX = "GTX"
    GTD = "GTD"


class NewOrderWorkingTypeEnum(Enum):
    MARK_PRICE = "MARK_PRICE"
    CONTRACT_PRICE = "CONTRACT_PRICE"


class NewOrderNewOrderRespTypeEnum(Enum):
    ACK = "ACK"
    RESULT = "RESULT"


class NewOrderPriceMatchEnum(Enum):
    NONE = "NONE"
    OPPONENT = "OPPONENT"
    OPPONENT_5 = "OPPONENT_5"
    OPPONENT_10 = "OPPONENT_10"
    OPPONENT_20 = "OPPONENT_20"
    QUEUE = "QUEUE"
    QUEUE_5 = "QUEUE_5"
    QUEUE_10 = "QUEUE_10"
    QUEUE_20 = "QUEUE_20"


class NewOrderSelfTradePreventionModeEnum(Enum):
    EXPIRE_TAKER = "EXPIRE_TAKER"
    EXPIRE_BOTH = "EXPIRE_BOTH"
    EXPIRE_MAKER = "EXPIRE_MAKER"
