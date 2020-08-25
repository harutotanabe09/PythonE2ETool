from pathlib import Path
import csv

dldir_name = 'download1/225.csv'
dldir_path = Path(dldir_name)
dldir_new_name = 'download1/226.csv'

# Read CSV file
with open(dldir_path, mode="r", encoding="utf-8") as rf:
    reader = csv.reader(rf)
    # Header Skip
    next(reader)
    # Output File
    with open(dldir_new_name, mode="w", encoding="utf-8") as wf:
        writer = csv.writer(wf)
        writer.writerow(["id"])
        # Output Row
        for line in reader:
            writer.writerow([line[0]*2])
