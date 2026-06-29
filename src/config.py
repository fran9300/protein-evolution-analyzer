from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"


FASTA_FILE = "p53.fasta"

FASTA_PATH = DATA_DIR / FASTA_FILE


RESULTS_DIR = PROJECT_ROOT / "results"

FIGURES_DIR = RESULTS_DIR / "figures"

