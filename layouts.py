from base import FieldVariant

F = FieldVariant.FreeSpace
C = FieldVariant.Common
U = FieldVariant.Uncommon
R = FieldVariant.Rare

SimpleLayout = [
    [R, U, C, U, R],
    [U, C, U, C, U],
    [C, U, F, U, C],
    [U, C, U, C, U],
    [R, U, C, U, R],
]

SimpleLayoutV2 = [
    [U, C, R, C, U],
    [C, U, C, U, C],
    [R, C, F, C, R],
    [C, U, C, U, C],
    [U, C, R, C, U],
]
