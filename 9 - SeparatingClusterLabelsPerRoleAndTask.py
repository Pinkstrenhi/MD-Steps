import os
import shutil

directory = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterLabelPerRole/"
directoryToSave = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterLabelPerRoleAndTask/"
roles = ["TOP", "MIDDLE", "BOTTOM", "JUNGLE", "UTILITY"]

for role in roles:
    roleFile = os.path.join(directory, role)
    if os.path.exists(roleFile):
        for filename in os.listdir(roleFile):
            if filename.endswith(".csv"):
                value = filename.split("_")[4]
                
                directoryTask = os.path.join(directoryToSave, role, value)
                os.makedirs(directoryTask, exist_ok=True)
                
                shutil.copy(os.path.join(roleFile, filename), directoryTask)
    else:
        print(f"A pasta {role} não existe em {directory}")


