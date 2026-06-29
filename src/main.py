from Bio import SeqIO

from sequence_analysis import *
from physicochemical import *
from report import *
from visualization import *
from json_report import generate_json_report

from config import DATA_DIR


def main():

    fasta = DATA_DIR / "example.fasta"


    protein = SeqIO.read(
        fasta,
        "fasta"
    )


    sequence = str(protein.seq)


    length = calculate_length(sequence)

    composition = calculate_amino_acid_composition(sequence)


    weight = calculate_molecular_weight(sequence)

    pI = calculate_isoelectric_point(sequence)

    hydro = calculate_hydrophobicity(sequence)


    generate_report(

        protein.id,
        length,
        weight,
        pI,
        hydro

    )

    generate_json_report(

        protein.id,
        length,
        composition,
        weight,
        pI,
        hydro

    )


    plot_amino_acid_composition(
        composition
    )



if __name__ == "__main__":
    main()