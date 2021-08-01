#!/usr/bin/env python3
"""
Define a type-annotated function that takes a float as argument and
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    return (lambda a: a * multiplier)
