#!/usr/bin/env python3

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    # This method can take a “target” parameter if you wish
    def heal(self) -> str:
        pass


# An attribute is used to make the state persistent and it impacts
#  the attack implementation of Creature with this capability.
class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed = False

# rhese methods will return simple strings that describe the
# action (just like the attack method)
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
