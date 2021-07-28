#!/usr/bin/env python3
"""
Define a type-annotated function that takes a float as argument and
returns a function that multiplies a float by multiplier
"""
from typing import callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """function that multiplies a float by multiplier"""
    return (lambda p : p * multiplier)
