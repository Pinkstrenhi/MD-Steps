import os
import csv
import pandas as pd

def CreateCSV(filePath,fieldnames):
    with open(filePath, mode="w",encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
def UpdateCSV(csvPath,write):
    with open(csvPath, mode="a",encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(write)
def FolderPath(directory,pathName):
    path = directory + pathName
    if not os.path.exists(path):
        os.mkdir(path)
    return path

csvFile = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/Anonimized/datasetAnonimized.csv"
df = pd.read_csv(csvFile)

directory = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeek/"

columnDate = "gameEndTimestampToDate"

keys = []
for key in df:
    keys.append(key)
    
df[columnDate] = pd.to_datetime(df[columnDate])
df["Week"] = df[columnDate].dt.week

for week,data in df.groupby("Week"):
    filePath = FolderPath(directory, f"Week_{week}")
    filePathWeeks = os.path.join(filePath, f"Week_{week}.csv")

    if not os.path.exists(filePathWeeks):
        CreateCSV(filePathWeeks, keys)

    dataPerWeek = data.values.tolist()
    for row in dataPerWeek:
        UpdateCSV(filePathWeeks, row[:-1])