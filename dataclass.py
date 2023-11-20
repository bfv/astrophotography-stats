
from dataclasses import dataclass

@dataclass
class FitsFile:
    filename: str
    target: str
    exposure: int
    filter: str

file = FitsFile(filename="file1.fits", target="M31", exposure=120, filter="HaOiii")
print(f"target: {file.target}")
