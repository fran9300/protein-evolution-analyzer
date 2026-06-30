from pydantic import BaseModel


class ProteinSummary(BaseModel):

    protein_id: str

    length: int

    molecular_weight: float

    pI: float

    hydrophobicity: float

    instability_index: float

    aliphatic_index: float



class StructureResult(BaseModel):

    alphaHelix: float

    turn: float

    betaSheet: float



class AnalysisResponse(BaseModel):

    protein: ProteinSummary

    composition: dict

    structure: StructureResult