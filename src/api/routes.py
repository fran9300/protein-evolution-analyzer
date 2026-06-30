from Bio import SeqIO
from fastapi import FastAPI, APIRouter, UploadFile, File

from io import StringIO

from src.api.schemas import AnalysisResponse
from src.services.protein_service import analyze_sequence

app = FastAPI()

router = APIRouter()


@router.get("/status")
def status():

    return {

        "service": "Protein Evolution Analyzer",

        "status": "running"

    }



@router.post("/analyze", response_model=AnalysisResponse)
async def analyze(file: UploadFile = File(...)):


    content = await file.read()


    fasta_content = content.decode(
        "utf-8"
    )


    record = SeqIO.read(
        StringIO(fasta_content),
        "fasta"
    )


    sequence = str(record.seq)



    result = analyze_sequence(
        sequence
    )


    protein = result.protein_result

    return {

        "protein": {

            "protein_id": record.id,

            "length": protein.length,

            "molecular_weight": round(
                protein.weight,
                2
            ),

            "pI": round(
                protein.pI,
                2
            ),

            "hydrophobicity": round(
                protein.hydrophobicity,
                3
            ),

            "instability_index": round(
                protein.instability_index,
                2
            ),

            "aliphatic_index": round(
                protein.aliphatic_index,
                2
            )

        },

        "composition": protein.composition,

        "structure": {

            "alphaHelix": round(
                protein.secondary_structure["alpha_helix"] * 100,
                2
            ),

            "turn": round(
                protein.secondary_structure["turn"] * 100,
                2
            ),

            "betaSheet": round(
                protein.secondary_structure["beta_sheet"] * 100,
                2
            )

        }

    }