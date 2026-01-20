def read_sales_file(filepath):
    records = []
    try:
        with open(filepath, 'r', encoding='latin-1') as file:
            lines = file.readlines()

        header = lines[0].strip().split('|')

        for line in lines[1:]:
            if not line.strip():
                continue
            parts = line.strip().split('|')
            if len(parts) != len(header):
                continue
            record = dict(zip(header, parts))
            records.append(record)

        print(f"Total records parsed: {len(records)}")
        return records

    except Exception as e:
        print("Error reading file:", e)
        return []
