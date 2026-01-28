import os

folders = [
    "dataset/images/train",
    "dataset/images/val",
    "dataset/labels/train",
    "dataset/labels/val"
]

for folder in folders:
    if not os.path.exists(folder):
        continue

    for filename in os.listdir(folder):
        if "_png.rf." in filename:
            base = filename.split("_png.rf.")[0]
            ext = ".png" if filename.endswith(".png") else ".txt"
            new_name = base + ext

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)

print("All image and label filenames fixed successfully!")
