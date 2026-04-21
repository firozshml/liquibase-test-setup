def generate_tlqrt_file_100k(
    output_file="TLQRT_100K.del",
    start_age=53,
    total_rows=100_000
):
    """
    Generates exactly 100,000 Liquibase-friendly rows for TLQRT.
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
        # Write header
        f.write(",".join(header) + "\n")

        rows_written = 0
        age = start_age

        while rows_written < total_rows:
            for sex in ("M", "F"):
                if rows_written >= total_rows:
                    break

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
                    str(age),                    # ✅ RTBL_AGE_DUR (NOT NULL)
                    " ",
                    f"{80.0 + age % 100:.5f}",   # RTBL_1_RT
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                    "0.00000",
                ]

                quoted = [f"\"{value}\"" for value in row]
                f.write(",".join(quoted) + "\n")

                rows_written += 1

            age += 1


if __name__ == "__main__":
    generate_tlqrt_file_100k("C:\\Users\\firozsh\\liquibase-test-setup\\Data\\TLQRT_100K.del")