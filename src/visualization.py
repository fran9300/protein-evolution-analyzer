import matplotlib.pyplot as plt

from src.config import FIGURES_DIR


def create_output_folder():

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def plot_amino_acid_composition(composition):

    create_output_folder()


    amino_acids = list(composition.keys())

    counts = list(composition.values())


    plt.figure(figsize=(10,5))


    plt.bar(
        amino_acids,
        counts
    )


    plt.xlabel(
        "Amino acid"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.title(
        "Amino Acid Composition"
    )


    plt.savefig(
        "../results/figures/amino_acid_composition.png",
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()