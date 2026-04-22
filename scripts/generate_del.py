def generate_del_file(output_file, start_id=11, total_rows=200_000):
    created_by = "LIQUIBASE"
    created_ts = "2024-04-16 10:00:00"

    with open(output_file, "w", encoding="utf-8") as f:
        # Write header
        f.write("ID|NAME|STATUS_CD|CREATED_BY|CREATED_TS\n")

        for i in range(total_rows):
            record_id = start_id + i

            # STATUS pattern: 10 A, then 5 I
            cycle_pos = i % 15
            status_cd = "A" if cycle_pos < 10 else "I"

            name = f"DEL Record {record_id}"

            line = (
                f"{record_id}|{name}|{status_cd}|"
                f"{created_by}|{created_ts}\n"
            )
            f.write(line)


if __name__ == "__main__":
    generate_del_file("C:\\Users\\firozsh\\liquibase-test-setup\\Data\\TLQBASE_200K.del", start_id=12)
