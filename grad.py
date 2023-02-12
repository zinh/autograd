from __future__ import annotations

class Value:
    def __init__(self, value: float):
        self._value = value

    def __add__(self, other: Value):
        return Value(self._value + other._value)

    def __mul__(self, other: Value):
        return Value(self._value * other._value)

    def __repr__(self) -> str:
        return str(self._value)
