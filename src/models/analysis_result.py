from dataclasses import dataclass

from src.models.protein_result import ProteinResult


@dataclass
class AnalysisResult:

    unknown: int

    unknown_percentage: float

    protein_result: ProteinResult