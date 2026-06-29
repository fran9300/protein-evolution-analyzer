from fastapi import FastAPI, APIRouter

from src.services.protein_service import analyze_sequence

app = FastAPI()

router = APIRouter()


@app.post("/analyze")
def analyze_protein(file):

    result = analyze_sequence(file)

    return result


@router.get("/status")
def status():

    return {

        "service": "Protein Evolution Analyzer",

        "status": "running"

    }