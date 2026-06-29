from dataclasses import dataclass


@dataclass
class DashboardResult:

    protein_id: str

    length: int

    molecular_weight: float

    isoelectric_point: float

    hydrophobicity: float

    instability_index: float

    aliphatic_index: float

    composition: dict

    secondary_structure: dict
