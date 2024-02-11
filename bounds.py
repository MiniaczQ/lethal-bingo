from typing import List
from base import Bound, BoundResult, Env, Planet


class MoonBound(Bound):
    moons: List[Planet]

    def __check(self, env: Env) -> BoundResult:
        if env.planet is None:
            return BoundResult.Unknown
        for moon in self.moons:
            if env.planet == moon:
                return BoundResult.Passed
        return BoundResult.Failed

    def __init__(self, *planets: List[Planet]):
        self.moons = planets
        self.check = lambda env: self.__check(env)
