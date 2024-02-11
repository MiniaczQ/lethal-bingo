from random import Random
from base import FieldVariant, generate_bingo, save_bingo
from layouts import SimpleLayout
from entries import FreeSpaces, Commons, Uncommons, Rares

if __name__ == "__main__":
    entries = {
        FieldVariant.FreeSpace: FreeSpaces,
        FieldVariant.Common: Commons,
        FieldVariant.Uncommon: Uncommons,
        FieldVariant.Rare: Rares,
    }
    bingo = generate_bingo(SimpleLayout, entries, Random(0))
    save_bingo(bingo)
