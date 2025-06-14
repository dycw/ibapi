"""Copyright (C) 2024 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

import inspect
import logging
import sys
from decimal import Decimal

from ibapi.const import (
    DOUBLE_INFINITY,
    INFINITY_STR,
    UNSET_DECIMAL,
    UNSET_DOUBLE,
    UNSET_INTEGER,
    UNSET_LONG,
)

"""
Collection of misc tools
"""

logger = logging.getLogger(__name__)


# I use this just to visually emphasize it's a wrapper overridden method
def iswrapper(fn):
    return fn


class BadMessage(Exception):
    def __init__(self, text) -> None:
        self.text = text


class ClientException(Exception):
    def __init__(self, code, msg, text) -> None:
        self.code = code
        self.msg = msg
        self.text = text


class LogFunction:
    def __init__(self, text, logLevel) -> None:
        self.text = text
        self.logLevel = logLevel

    def __call__(self, fn):
        def newFn(origSelf, *args, **kwargs) -> None:
            if logger.isEnabledFor(self.logLevel):
                argNames = [
                    argName
                    for argName in inspect.getfullargspec(fn)[0]
                    if argName != "self"
                ]
                logger.log(
                    self.logLevel,
                    "{} {} {} kw:{}",
                    self.text,
                    fn.__name__,
                    [
                        arg
                        for arg in zip(argNames, args, strict=False)
                        if arg[1] is not origSelf
                    ],
                    kwargs,
                )
            fn(origSelf, *args)

        return newFn


def current_fn_name(parent_idx=0):
    # depth is 1 bc this is already a fn, so we need the caller
    return sys._getframe(1 + parent_idx).f_code.co_name


def setattr_log(self, var_name, var_value) -> None:
    # import code; code.interact(local=locals())
    logger.debug("%s %s %s=|%s|", self.__class__, id(self), var_name, var_value)
    super(self.__class__, self).__setattr__(var_name, var_value)


SHOW_UNSET = True


def decode(the_type, fields, show_unset=False, use_unicode=False):
    try:
        s = next(fields)
    except StopIteration:
        msg = "no more fields"
        raise BadMessage(msg)

    logger.debug("decode %s %s", the_type, s)

    if the_type is Decimal:
        if (
            s is None
            or len(s) == 0
            or s.decode() == "2147483647"
            or s.decode() == "9223372036854775807"
            or s.decode() == "1.7976931348623157E308"
        ):
            return UNSET_DECIMAL
        return the_type(s.decode())

    if the_type is str:
        if type(s) is str:
            return s
        if type(s) is bytes:
            return s.decode(
                "unicode-escape" if use_unicode else "UTF-8", errors="backslashreplace"
            )
        raise TypeError(
            "unsupported incoming type " + type(s) + " for desired type 'str"
        )

    orig_type = the_type
    if the_type is bool:
        the_type = int

    if the_type is float and s.decode() == INFINITY_STR:
        return DOUBLE_INFINITY

    if show_unset:
        if s is None or len(s) == 0:
            if the_type is float:
                n = UNSET_DOUBLE
            elif the_type is int:
                n = UNSET_INTEGER
            else:
                raise TypeError("unsupported desired type for empty value" + the_type)
        else:
            n = the_type(s)
    else:
        n = the_type(s or 0)

    if orig_type is bool:
        n = n != 0

    return n


def ExerciseStaticMethods(klass) -> None:
    import types

    # import code; code.interact(local=dict(globals(), **locals()))
    for _, var in inspect.getmembers(klass):
        # print(name, var, type(var))
        if type(var) == types.FunctionType:
            pass


def floatMaxString(val: float):
    return (
        f"{val:.8f}".rstrip("0").rstrip(".").rstrip(",") if val != UNSET_DOUBLE else ""
    )


def longMaxString(val):
    return str(val) if val != UNSET_LONG else ""


def intMaxString(val):
    return str(val) if val != UNSET_INTEGER else ""


def isAsciiPrintable(val):
    return all(
        (ord(c) >= 32 and ord(c) < 127) or ord(c) == 9 or ord(c) == 10 or ord(c) == 13
        for c in val
    )


def decimalMaxString(val: Decimal) -> str:
    return f"{val:f}" if val != UNSET_DECIMAL else ""


def isPegBenchOrder(orderType: str):
    return orderType in ("PEG BENCH", "PEGBENCH")


def isPegMidOrder(orderType: str):
    return orderType in ("PEG MID", "PEGMID")


def isPegBestOrder(orderType: str):
    return orderType in ("PEG BEST", "PEGBEST")


def log_(func, params, action) -> None:
    if logger.isEnabledFor(logging.INFO):
        if "self" in params:
            params = dict(params)
            del params["self"]
        logger.info(f"{action} {func} {params}")
