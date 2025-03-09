import os

OUTPUT_FILE = "backend/database_merged.db"
PARTS_DIR = "backend/"  # Change this if the parts are in a different directory

# Get all part files sorted by number
part_files = sorted(
    [f for f in os.listdir(PARTS_DIR) if f.startswith("database.part")],
    key=lambda x: int(x.split("part")[-1])
)

# Merge all parts
with open(OUTPUT_FILE, "wb") as merged:
    for part_file in part_files:
        with open(os.path.join(PARTS_DIR, part_file), "rb") as part:
            merged.write(part.read())

print(f"Database reassembled as {OUTPUT_FILE}")
