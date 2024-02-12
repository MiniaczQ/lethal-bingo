from collections import defaultdict
from enum import Enum
from random import Random
from typing import DefaultDict, List, Callable
from pydantic import BaseModel, RootModel


class Planet(Enum):
    Experimentation = "experimentation"
    Assurance = "assurance"
    Vow = "vow"
    Offense = "offense"
    March = "march"
    Rend = "rend"
    Dine = "dine"
    Titan = "titan"


class FieldVariant(Enum):
    FreeSpace = "free-space"
    Uncommon = "uncommon"
    Common = "common"
    Rare = "rare"


class BoundResult(Enum):
    Failed = "failed"
    Passed = "passed"
    Unknown = "unknown"


class Env:
    planet: Planet | None = None
    player_count: int | None = None


class Bound:
    check: Callable[[Env], BoundResult]


class Entry:
    name: str
    bounds: List[Bound]

    def __init__(
        self,
        name: str,
        bounds: List[Bound] | None = None,
    ):
        self.name = name
        self.bounds = bounds or []

    def check(self, env: Env) -> BoundResult:
        unknown = False
        for bound in self.bounds:
            result = bound.check(env)
            if result == BoundResult.Failed:
                return BoundResult.Failed
            if result == BoundResult.Unknown:
                unknown = True
        return BoundResult.Unknown if unknown else BoundResult.Passed


def env_filter_entries(
    entries: DefaultDict[FieldVariant, List[Entry]], env: Env
) -> DefaultDict[FieldVariant, List[Entry]]:
    result = defaultdict(list)
    for key in entries.keys():
        result[key] = list(
            filter(lambda e: e.check(env) is not BoundResult.Failed, entries[key])
        )
    return result


def generate_bingo(
    layout: List[List[FieldVariant]],
    entries: DefaultDict[FieldVariant, List[Entry]],
    rng: Random | None = None,
) -> List[List[Entry]]:
    # Assert shape
    size = len(layout)
    for x in layout:
        assert size == len(x), "Layout is not square"
    # Assert there is enough entries
    layout_variant_count = dict()
    for variant in FieldVariant:
        layout_variant_count[variant] = sum(
            [1 if v == variant else 0 for x in layout for v in x]
        )
        entry_count = len(entries[variant])
        assert (
            layout_variant_count[variant] <= entry_count
        ), f"Not enough entries of variant {variant}"
    # Randomize unique entries for each layout entry
    rng = rng or Random()
    final_variant_entries = defaultdict(list)
    for variant, variant_entries in entries.items():
        k = layout_variant_count[variant]
        rng.shuffle(variant_entries)
        final_variant_entries[variant] = variant_entries[:k]
    # Assemble board
    result = []
    for layout_row in layout:
        row_result = []
        for layout_variant in layout_row:
            row_result.append(final_variant_entries[layout_variant].pop())
        result.append(row_result)
    return result


class SerEntry(BaseModel):
    name: str


def save_bingo(entries: List[List[Entry]]):
    flattened: list[Entry] = list(
        entry for entries_row in entries for entry in entries_row
    )
    mapped = RootModel(list(SerEntry(name=entry.name) for entry in flattened))
    with open("result.json", "wt") as f:
        f.write(mapped.model_dump_json(indent=4))
