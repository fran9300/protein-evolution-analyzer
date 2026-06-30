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


            "molecular_weight": protein.weight,


            "pI": protein.pI,


            "hydrophobicity": protein.hydrophobicity,


            "instability_index": protein.instability_index,


            "aliphatic_index": protein.aliphatic_index

        },


        "composition": protein.composition,


        "structure": {


            "alphaHelix":
                protein.secondary_structure["alpha_helix"] * 100,


            "turn":
                protein.secondary_structure["turn"] * 100,


            "betaSheet":
                protein.secondary_structure["beta_sheet"] * 100

        }

    }