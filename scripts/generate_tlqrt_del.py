def generate_tlqrt_file(
    output_file="TLQRT_test.del",
    start_age=53,
    rows_per_age=2,
    total_ages=50
):
    """
    Generates a Liquibase-friendly DEL/CSV file for TLQRT.
    """

    header = [
        "CO_ID",
        "RTBL_ID",
        "RTBL_RT_TYP_CD",
        "RTBL_SMKR_CD",
        "RTBL_PAR_CD",
        "RTBL_SEX_CD",
        "RTBL_STBL_CD",
        "LOC_GR_ID",
        "RTBL_DB_OPT_CD",
        "RTBL_PNSN_QUALF_CD",
        "RTBL_JNT_LIFE_CD",
        "DPOS_TRM_MO_DUR",
        "DPOS_TRM_DY_DUR",
        "RTBL_AGE",
        "RTBL_IDT_NUM",
        "RTBL_AGE_DUR",
        "RTBL_REASN_CD",
        "RTBL_1_RT",
        "RTBL_2_RT",
        "RTBL_3_RT",
        "RTBL_4_RT",
        "RTBL_5_RT",
        "RTBL_6_RT",
        "RTBL_7_RT",
        "RTBL_8_RT",
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(",".join(header) + "\n")

        for i in range(total_ages):
            age = start_age + i

            for sex in ["M", "F"]:
                row = [
                    "CP",
                    "CSUS3D",
                    "ULVAL",
                    " ",
                    " ",
                    sex,
                    "            ",
                    "   ",
                    " ",
                    " ",
                    " ",
                    "000",
                    "000",
                    f"{age:03d}",
                    "7748884",
                    str(age),              # ✅ RTBL_AGE_DUR (DECIMAL, NOT NULL)
                    " ",
                    f"{80.0 + i:.5f}",     # RTBL_1_RT
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                ]

                quoted = [f"\"{col}\"" for col in row]
                f.write(",".join(quoted) + "\n")


if __name__ == "__main__":
    generate_tlqrt_file("C:\\Users\\firozsh\\liquibase-test-setup\\Data\\TLQRT_Test.del")