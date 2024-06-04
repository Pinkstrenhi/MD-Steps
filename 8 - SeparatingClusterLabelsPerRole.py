import os
import shutil

directory = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterLabel/"
directoryToSave = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterLabelPerRole/"
roles = ["TOP", "MIDDLE", "BOTTOM", "JUNGLE", "UTILITY"]

for role in roles:
    roleFile = os.path.join(directoryToSave, role)
    if not os.path.exists(roleFile):
        os.makedirs(roleFile)

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        roleFileName = filename.split("_")[3]
        if roleFileName in roles:
            source = os.path.join(directory, filename)
            directoryFinal = os.path.join(directoryToSave, roleFileName, filename)
            shutil.copy(source, directoryFinal)
            print(f"File {filename} moved to {roleFileName}")
