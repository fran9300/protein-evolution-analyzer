from Bio import SeqIO

from sequence_analysis import (
    calculate_length,
    calculate_amino_acid_composition
)
from physicochemical import (
    calculate_molecular_weight,
    calculate_isoelectric_point,
    calculate_hydrophobicity,
    calculate_hydrophobicity_profile
)

from report import generate_report
from visualization import plot_amino_acid_composition, plot_hydrophobicity_profile
from json_report import generate_json_report

from validation import (
    validate_sequence,
    count_unknown_residues,
    calculate_unknown_percentage,
    remove_unknown_residues
)

from config import DATA_DIR



def main():

    fasta = DATA_DIR / "example.fasta"


    protein = SeqIO.read(
        fasta,
        "fasta"
    )


    sequence = str(protein.seq)


    print("=" * 40)
    print("Protein Analysis Report")
    print("=" * 40)


    print(
        "Protein ID:",
        protein.id
    )


    print(
        "Sequence length:",
        len(sequence),
        "aa"
    )


    print()



    # Validation

    if not validate_sequence(sequence):

        raise ValueError(
            "Protein sequence is invalid"
        )


    unknown = count_unknown_residues(sequence)

    unknown_percentage = calculate_unknown_percentage(sequence)


    print("Sequence quality:")

    print(
        "Unknown residues:",
        unknown
    )


    print(
        "Unknown percentage:",
        round(unknown_percentage, 2),
        "%"
    )


    print()



    # Clean sequence for physicochemical analysis

    clean_sequence = remove_unknown_residues(sequence)



    # Sequence analysis

    length = calculate_length(clean_sequence)

    composition = calculate_amino_acid_composition(sequence)


    print("Sequence analysis:")

    print(
        "Length:",
        length,
        "aa"
    )


    print(
        "Amino acid composition:"
    )

    print(
        composition
    )


    print()



    # Physicochemical properties

    weight = calculate_molecular_weight(clean_sequence)

    pI = calculate_isoelectric_point(clean_sequence)

    hydro = calculate_hydrophobicity(clean_sequence)

    hydro_profile = calculate_hydrophobicity_profile(
        clean_sequence
    )

    print("Physicochemical properties:")


    print(
        "Molecular weight:",
        round(weight,2),
        "Da"
    )


    print(
        "Isoelectric point:",
        round(pI,2)
    )


    print(
        "Hydrophobicity (GRAVY):",
        round(hydro,3)
    )

    print(
        "Hydrophobicity profile:"
    )

    print(
        hydro_profile
    )


    print()



    # Generate outputs

    generate_report(

        protein.id,
        length,
        unknown,
        round(unknown_percentage, 2),
        weight,
        pI,
        hydro

    )

    generate_json_report(

        protein.id,
        length,
        composition,
        unknown,
        round(unknown_percentage, 2),
        weight,
        pI,
        hydro

    )


    plot_amino_acid_composition(
        composition
    )

    plot_hydrophobicity_profile(
        hydro_profile
    )


    print()

    print("Analysis completed successfully")

    print("=" * 40)



if __name__ == "__main__":
    main()