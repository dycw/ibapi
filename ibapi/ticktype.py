"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""


"""
TickType type
"""

from ibapi.enum_implem import Enum


# TickType
TickType = int
TickTypeEnum = Enum(
    "BID_SIZE",
    "BID",
    "ASK",
    "ASK_SIZE",
    "LAST",
    "LAST_SIZE",
    "HIGH",
    "LOW",
    "VOLUME",
    "CLOSE",
    "BID_OPTION_COMPUTATION",
    "ASK_OPTION_COMPUTATION",
    "LAST_OPTION_COMPUTATION",
    "MODEL_OPTION",
    "OPEN",
    "LOW_13_WEEK",
    "HIGH_13_WEEK",
    "LOW_26_WEEK",
    "HIGH_26_WEEK",
    "LOW_52_WEEK",
    "HIGH_52_WEEK",
    "AVG_VOLUME",
    "OPEN_INTEREST",
    "OPTION_HISTORICAL_VOL",
    "OPTION_IMPLIED_VOL",
    "OPTION_BID_EXCH",
    "OPTION_ASK_EXCH",
    "OPTION_CALL_OPEN_INTEREST",
    "OPTION_PUT_OPEN_INTEREST",
    "OPTION_CALL_VOLUME",
    "OPTION_PUT_VOLUME",
    "INDEX_FUTURE_PREMIUM",
    "BID_EXCH",
    "ASK_EXCH",
    "AUCTION_VOLUME",
    "AUCTION_PRICE",
    "AUCTION_IMBALANCE",
    "MARK_PRICE",
    "BID_EFP_COMPUTATION",
    "ASK_EFP_COMPUTATION",
    "LAST_EFP_COMPUTATION",
    "OPEN_EFP_COMPUTATION",
    "HIGH_EFP_COMPUTATION",
    "LOW_EFP_COMPUTATION",
    "CLOSE_EFP_COMPUTATION",
    "LAST_TIMESTAMP",
    "SHORTABLE",
    "FUNDAMENTAL_RATIOS",
    "RT_VOLUME",
    "HALTED",
    "BID_YIELD",
    "ASK_YIELD",
    "LAST_YIELD",
    "CUST_OPTION_COMPUTATION",
    "TRADE_COUNT",
    "TRADE_RATE",
    "VOLUME_RATE",
    "LAST_RTH_TRADE",
    "RT_HISTORICAL_VOL",
    "IB_DIVIDENDS",
    "BOND_FACTOR_MULTIPLIER",
    "REGULATORY_IMBALANCE",
    "NEWS_TICK",
    "SHORT_TERM_VOLUME_3_MIN",
    "SHORT_TERM_VOLUME_5_MIN",
    "SHORT_TERM_VOLUME_10_MIN",
    "DELAYED_BID",
    "DELAYED_ASK",
    "DELAYED_LAST",
    "DELAYED_BID_SIZE",
    "DELAYED_ASK_SIZE",
    "DELAYED_LAST_SIZE",
    "DELAYED_HIGH",
    "DELAYED_LOW",
    "DELAYED_VOLUME",
    "DELAYED_CLOSE",
    "DELAYED_OPEN",
    "RT_TRD_VOLUME",
    "CREDITMAN_MARK_PRICE",
    "CREDITMAN_SLOW_MARK_PRICE",
    "DELAYED_BID_OPTION",
    "DELAYED_ASK_OPTION",
    "DELAYED_LAST_OPTION",
    "DELAYED_MODEL_OPTION",
    "LAST_EXCH",
    "LAST_REG_TIME",
    "FUTURES_OPEN_INTEREST",
    "AVG_OPT_VOLUME",
    "DELAYED_LAST_TIMESTAMP",
    "SHORTABLE_SHARES",
    "DELAYED_HALTED",
    "REUTERS_2_MUTUAL_FUNDS",
    "ETF_NAV_CLOSE",
    "ETF_NAV_PRIOR_CLOSE",
    "ETF_NAV_BID",
    "ETF_NAV_ASK",
    "ETF_NAV_LAST",
    "ETF_FROZEN_NAV_LAST",
    "ETF_NAV_HIGH",
    "ETF_NAV_LOW",
    "SOCIAL_MARKET_ANALYTICS",
    "ESTIMATED_IPO_MIDPOINT",
    "FINAL_IPO_LAST",
    "DELAYED_YIELD_BID",
    "DELAYED_YIELD_ASK",
    "NOT_SET",
)
