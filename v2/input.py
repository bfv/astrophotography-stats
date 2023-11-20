
from dataclass import dataclass

@dataclass
class InputData:
    rootdir: str
    excludes: []


bla = InputData(rootdir="a", excludes=["m31"])

bla.rootdir = "b"

print(f"root: {bla.rootdir}")