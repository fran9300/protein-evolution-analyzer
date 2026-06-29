import json

from src.reports.csv_report import generate_report
from src.reports.json_report import generate_json_report
from src.config import RESULTS_DIR



def test_generate_csv_report():


    generate_report(

        "TEST_PROTEIN",

        10,

        0,

        0.0,

        1000.0,

        7.0,

        -0.5

    )


    files = list(
        RESULTS_DIR.glob("*.csv")
    )


    assert len(files) > 0



def test_generate_json_report():


    generate_json_report(

        "TEST_PROTEIN",

        10,

        {
            "A":2,
            "M":1
        },

        0,

        0.0,

        1000.0,

        7.0,

        -0.5

    )


    files = list(
        RESULTS_DIR.glob("*.json")
    )


    assert len(files) > 0



    with open(
        files[-1],
        "r"
    ) as file:


        data = json.load(file)



    assert data["protein"] == "TEST_PROTEIN"


    assert data["sequence_analysis"]["length"] == 10