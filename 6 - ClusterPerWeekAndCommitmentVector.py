import os
import csv
import pandas as pd
from sklearn.cluster import KMeans

def CreateCSV(filePath,fieldnames):
    with open(filePath, mode="w",encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
def UpdateCSV(csvPath,write):
    with open(csvPath, mode="a",encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(write)
def ClusterKmeans(df):
    k = 3
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(df)
    df["Cluster"] = kmeans.labels_
    return df

source = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeekClusterWithoutNaN/"
directoryToSave = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterResult/"

columns = ["Player","Week","Task","AmountPerWeek","sMin","sMax","Delta"]

for file in os.listdir(source):
    filePath = os.path.join(source,file)
    fileName = file.split(".")[0]
    print(fileName)
    print("-"*60)
    
    df = pd.read_csv(filePath,encoding = "utf-16")
    
    if not df.empty:
        dfId = df[["Player","Week","Task"]]
        dfClusterColumns = df[["AmountPerWeek","sMin","sMax","Delta"]]
            
        csvName = f"{directoryToSave}/{fileName}_Cluster.csv"
        
        CreateCSV(csvName,columns + ["Cluster"])
        
        dfCluster = ClusterKmeans(dfClusterColumns)
        
        dfFinal = pd.merge(dfId,dfCluster,left_index = True,right_index = True)
        
        for index,row in dfFinal.iterrows():
            UpdateCSV(csvName,row)
    else: 
        print(f"File {fileName} is null")
        print("-"*60)


    
    