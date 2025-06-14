"""Copyright (C) 2023 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

from ibapi.const import UNSET_DECIMAL, UNSET_INTEGER
from ibapi.enum_implem import Enum
from ibapi.object_implem import Object
from ibapi.utils import decimalMaxString, floatMaxString, intMaxString

TickerId = int
OrderId = int
TagValueList = list

FaDataType = int
FaDataTypeEnum = Enum("N/A", "GROUPS", "N/A", "ALIASES")

MarketDataType = int
MarketDataTypeEnum = Enum("N/A", "REALTIME", "FROZEN", "DELAYED", "DELAYED_FROZEN")

Liquidities = int
LiquiditiesEnum = Enum("None", "Added", "Remove", "RoudedOut")

SetOfString = set
SetOfFloat = set
ListOfOrder = list
ListOfFamilyCode = list
ListOfContractDescription = list
ListOfDepthExchanges = list
ListOfNewsProviders = list
SmartComponentMap = dict
HistogramDataList = list
ListOfPriceIncrements = list
ListOfHistoricalTick = list
ListOfHistoricalTickBidAsk = list
ListOfHistoricalTickLast = list
ListOfHistoricalSessions = list


class BarData(Object):
    def __init__(self) -> None:
        self.date = ""
        self.open = 0.0
        self.high = 0.0
        self.low = 0.0
        self.close = 0.0
        self.volume = UNSET_DECIMAL
        self.wap = UNSET_DECIMAL
        self.barCount = 0

    def __str__(self) -> str:
        return f"Date: {self.date}, Open: {floatMaxString(self.open)}, High: {floatMaxString(self.high)}, Low: {floatMaxString(self.low)}, Close: {floatMaxString(self.close)}, Volume: {decimalMaxString(self.volume)}, WAP: {decimalMaxString(self.wap)}, BarCount: {intMaxString(self.barCount)}"


class RealTimeBar(Object):
    def __init__(
        self,
        time=0,
        endTime=-1,
        open_=0.0,
        high=0.0,
        low=0.0,
        close=0.0,
        volume=UNSET_DECIMAL,
        wap=UNSET_DECIMAL,
        count=0,
    ) -> None:
        self.time = time
        self.endTime = endTime
        self.open_ = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.wap = wap
        self.count = count

    def __str__(self) -> str:
        return f"Time: {intMaxString(self.time)}, Open: {floatMaxString(self.open_)}, High: {floatMaxString(self.high)}, Low: {floatMaxString(self.low)}, Close: {floatMaxString(self.close)}, Volume: {decimalMaxString(self.volume)}, WAP: {decimalMaxString(self.wap)}, Count: {intMaxString(self.count)}"


class HistogramData(Object):
    def __init__(self) -> None:
        self.price = 0.0
        self.size = UNSET_DECIMAL

    def __str__(self) -> str:
        return (
            f"Price: {floatMaxString(self.price)}, Size: {decimalMaxString(self.size)}"
        )


class NewsProvider(Object):
    def __init__(self) -> None:
        self.code = ""
        self.name = ""

    def __str__(self) -> str:
        return f"Code: {self.code}, Name: {self.name}"


class DepthMktDataDescription(Object):
    def __init__(self) -> None:
        self.exchange = ""
        self.secType = ""
        self.listingExch = ""
        self.serviceDataType = ""
        self.aggGroup = UNSET_INTEGER

    def __str__(self) -> str:
        aggGroup = self.aggGroup if self.aggGroup != UNSET_INTEGER else ""
        return f"Exchange: {self.exchange}, SecType: {self.secType}, ListingExchange: {self.listingExch}, ServiceDataType: {self.serviceDataType}, AggGroup: {intMaxString(aggGroup)}, "


class SmartComponent(Object):
    def __init__(self) -> None:
        self.bitNumber = 0
        self.exchange = ""
        self.exchangeLetter = ""

    def __str__(self) -> str:
        return "BitNumber: %d, Exchange: %s, ExchangeLetter: %s" % (
            self.bitNumber,
            self.exchange,
            self.exchangeLetter,
        )


class TickAttrib(Object):
    def __init__(self) -> None:
        self.canAutoExecute = False
        self.pastLimit = False
        self.preOpen = False

    def __str__(self) -> str:
        return "CanAutoExecute: %d, PastLimit: %d, PreOpen: %d" % (
            self.canAutoExecute,
            self.pastLimit,
            self.preOpen,
        )


class TickAttribBidAsk(Object):
    def __init__(self) -> None:
        self.bidPastLow = False
        self.askPastHigh = False

    def __str__(self) -> str:
        return "BidPastLow: %d, AskPastHigh: %d" % (self.bidPastLow, self.askPastHigh)


class TickAttribLast(Object):
    def __init__(self) -> None:
        self.pastLimit = False
        self.unreported = False

    def __str__(self) -> str:
        return "PastLimit: %d, Unreported: %d" % (self.pastLimit, self.unreported)


class FamilyCode(Object):
    def __init__(self) -> None:
        self.accountID = ""
        self.familyCodeStr = ""

    def __str__(self) -> str:
        return f"AccountId: {self.accountID}, FamilyCodeStr: {self.familyCodeStr}"


class PriceIncrement(Object):
    def __init__(self) -> None:
        self.lowEdge = 0.0
        self.increment = 0.0

    def __str__(self) -> str:
        return f"LowEdge: {floatMaxString(self.lowEdge)}, Increment: {floatMaxString(self.increment)}"


class HistoricalTick(Object):
    def __init__(self) -> None:
        self.time = 0
        self.price = 0.0
        self.size = UNSET_DECIMAL

    def __str__(self) -> str:
        return f"Time: {intMaxString(self.time)}, Price: {floatMaxString(self.price)}, Size: {decimalMaxString(self.size)}"


class HistoricalTickBidAsk(Object):
    def __init__(self) -> None:
        self.time = 0
        self.tickAttribBidAsk = TickAttribBidAsk()
        self.priceBid = 0.0
        self.priceAsk = 0.0
        self.sizeBid = UNSET_DECIMAL
        self.sizeAsk = UNSET_DECIMAL

    def __str__(self) -> str:
        return f"Time: {intMaxString(self.time)}, TickAttriBidAsk: {self.tickAttribBidAsk}, PriceBid: {floatMaxString(self.priceBid)}, PriceAsk: {floatMaxString(self.priceAsk)}, SizeBid: {decimalMaxString(self.sizeBid)}, SizeAsk: {decimalMaxString(self.sizeAsk)}"


class HistoricalTickLast(Object):
    def __init__(self) -> None:
        self.time = 0
        self.tickAttribLast = TickAttribLast()
        self.price = 0.0
        self.size = UNSET_DECIMAL
        self.exchange = ""
        self.specialConditions = ""

    def __str__(self) -> str:
        return f"Time: {intMaxString(self.time)}, TickAttribLast: {self.tickAttribLast}, Price: {floatMaxString(self.price)}, Size: {decimalMaxString(self.size)}, Exchange: {self.exchange}, SpecialConditions: {self.specialConditions}"


class HistoricalSession(Object):
    def __init__(self) -> None:
        self.startDateTime = ""
        self.endDateTime = ""
        self.refDate = ""

    def __str__(self) -> str:
        return f"Start: {self.startDateTime}, End: {self.endDateTime}, Ref Date: {self.refDate}"


class WshEventData(Object):
    def __init__(self) -> None:
        self.conId = UNSET_INTEGER
        self.filter = ""
        self.fillWatchlist = False
        self.fillPortfolio = False
        self.fillCompetitors = False
        self.startDate = ""
        self.endDate = ""
        self.totalLimit = UNSET_INTEGER

    def __str__(self) -> str:
        return f"WshEventData. ConId: {intMaxString(self.conId)}, Filter: {self.filter}, Fill Watchlist: {self.fillWatchlist:d}, Fill Portfolio: {self.fillPortfolio:d}, Fill Competitors: {self.fillCompetitors:d}"
