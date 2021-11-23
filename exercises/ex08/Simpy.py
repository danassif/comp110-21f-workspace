"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """Simpy."""
    values: list[float]

    def __init__(self, values: list[float] = []):
        """Constructor."""
        self.values = values

    def __str__(self) -> str:
        """Repr."""
        return f"Simpy({self.values})"

    def fill(self, value: float, n: int = -1) -> None:
        """Fill."""
        xs: list[float] = []
        for _ in range(n):
            xs.append(value)
        self.values = xs

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arrange."""
        xs: list[float] = []
        if step > 0:
            while start < stop:
                xs.append(start)
                start += step
        elif step < 0:
            while start > stop:
                xs.append(start)
                start += step
        else:
            raise ValueError("Step cannot be 0.0.")
        self.values = xs

    def sum(self) -> float:
        """Sum."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add."""
        xs: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] + rhs.values[i])
        else:
            for item in self.values:
                xs.append(item + rhs)
        return Simpy(xs)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Pow."""
        xs: list[float] = []
        if isinstance(rhs, Simpy):    
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] ** rhs.values[i])
        else:
            for item in self.values:
                xs.append(item ** rhs)
        return Simpy(xs)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Mod."""
        xs: list[float] = []
        if isinstance(rhs, Simpy):    
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] % rhs.values[i])
        else:
            for item in self.values:
                xs.append(item % rhs)
        return Simpy(xs)
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Eq."""
        xs: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] == rhs.values[i])
        else:
            for item in self.values:
                xs.append(item == rhs)
        return xs

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading the greater than operator to produce a mask."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(rhs.values):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Getitem."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            xs: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    xs.append(self.values[i])
            return Simpy(xs)