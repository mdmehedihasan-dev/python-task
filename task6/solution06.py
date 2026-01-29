import shutil
import os

# File existence check
original_file = "app.log"

if os.path.exists(original_file):
    for i in range(1, 6):  # Create 5 copies
        copy_file = f"app_{i}.log"
        shutil.copyfile(original_file, copy_file)
        print(f"Created {copy_file}")
else:
    print(f"{original_file} not found!")
