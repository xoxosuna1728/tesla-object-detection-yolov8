import os

folders = [
    "dataset/labels/train",
    "dataset/labels/val"
]

for folder in folders:
    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(folder, file)

        with open(path, "r") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]

        # YOLO expects 5 values in ONE line
        if len(lines) == 5:
            new_line = " ".join(lines)
            with open(path, "w") as f:
                f.write(new_line + "\n")

print("All label files converted to YOLO format!")
