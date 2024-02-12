from base import Entry

FreeSpaces = []
with open("entries/free-spaces.txt", "r") as f:
    FreeSpaces.extend(Entry(l.strip()) for l in f.readlines() if len(l.strip()) > 0)
    
Commons = []
with open("entries/commons.txt", "r") as f:
    Commons.extend(Entry(l.strip()) for l in f.readlines() if len(l.strip()) > 0)
    
Uncommons = []
with open("entries/uncommons.txt", "r") as f:
    Uncommons.extend(Entry(l.strip()) for l in f.readlines() if len(l.strip()) > 0)

Rares = []
with open("entries/rares.txt", "r") as f:
    Rares.extend(Entry(l.strip()) for l in f.readlines() if len(l.strip()) > 0)
