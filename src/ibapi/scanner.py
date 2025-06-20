"""Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

from ibapi.const import UNSET_DOUBLE, UNSET_INTEGER
from ibapi.object_implem import Object


class ScanData(Object):
    def __init__(
        self,
        contract=None,
        rank=0,
        distance="",
        benchmark="",
        projection="",
        legsStr="",
    ) -> None:
        self.contract = contract
        self.rank = rank
        self.distance = distance
        self.benchmark = benchmark
        self.projection = projection
        self.legsStr = legsStr

    def __str__(self) -> str:
        return (
            "Rank: %d, Symbol: %s, SecType: %s, Currency: %s, Distance: %s, Benchmark: %s, Projection: %s, Legs String: %s"
            % (
                self.rank,
                self.contract.symbol,
                self.contract.secType,
                self.contract.currency,
                self.distance,
                self.benchmark,
                self.projection,
                self.legsStr,
            )
        )


NO_ROW_NUMBER_SPECIFIED = -1


class ScannerSubscription(Object):
    def __init__(self) -> None:
        self.numberOfRows = NO_ROW_NUMBER_SPECIFIED
        self.instrument = ""
        self.locationCode = ""
        self.scanCode = ""
        self.abovePrice = UNSET_DOUBLE
        self.belowPrice = UNSET_DOUBLE
        self.aboveVolume = UNSET_INTEGER
        self.marketCapAbove = UNSET_DOUBLE
        self.marketCapBelow = UNSET_DOUBLE
        self.moodyRatingAbove = ""
        self.moodyRatingBelow = ""
        self.spRatingAbove = ""
        self.spRatingBelow = ""
        self.maturityDateAbove = ""
        self.maturityDateBelow = ""
        self.couponRateAbove = UNSET_DOUBLE
        self.couponRateBelow = UNSET_DOUBLE
        self.excludeConvertible = False
        self.averageOptionVolumeAbove = UNSET_INTEGER
        self.scannerSettingPairs = ""
        self.stockTypeFilter = ""

    def __str__(self) -> str:
        return f"Instrument: {self.instrument}, LocationCode: {self.locationCode}, ScanCode: {self.scanCode}"
