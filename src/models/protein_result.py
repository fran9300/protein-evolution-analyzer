from dataclasses import dataclass


@dataclass
class ProteinResult:

    length: int

    composition: dict

    weight: float

    pI: float

    hydrophobicity: float

    hydro_profile: list

    window_profile: list

    instability_index: float

    extinction_coefficient: dict

    secondary_structure: dict

    aliphatic_index: float