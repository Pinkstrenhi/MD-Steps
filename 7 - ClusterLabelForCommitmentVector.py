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
def ClusterMean(cluster,column):
    dfCluster = df[df["Cluster"] == cluster]
    mean = dfCluster[column].mean()
    return mean
        
source = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterResult/"
directoryToSave = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/ClusterLabel/"

columns = ["Player","Week","Task","AmountPerWeek","sMin","sMax","Delta","Cluster"]

columnMean = "sMax"

for file in os.listdir(source):
    filePath = os.path.join(source,file)
    fileName = file.split(".")[0]
    
    CreateCSV(f"{directoryToSave}{fileName}_Label.csv",columns + ["Label"])
    
    df = pd.read_csv(filePath,encoding = "utf-16")
    
    dfClusterMean00 = ClusterMean(0,columnMean)
    dfClusterMean01 = ClusterMean(1,columnMean)
    dfClusterMean02 = ClusterMean(2,columnMean)
    
    label = {
                "0" : [dfClusterMean00],
                "1" : [dfClusterMean01],
                "2" : [dfClusterMean02]
            }
    
    label = dict(sorted(label.items(),key = lambda item: item[1]))
    
    print(fileName)
    print("\n")
    
    for index,key in enumerate(label.keys()):
        if index == 0: 
            label[key] += ["Low"]
        elif index == 1: 
            label[key] += ["Average"]
        elif index == 2: 
            label[key] += ["High"]
        
        print(f"Cluster {key} -> {label[key]}")
    print("-"*60)
    
    for i in range(len(df)):
        if df["Cluster"][i] == 0:
            df["Label"] = label["0"][1]
            
        elif df["Cluster"][i] == 1:
            df["Label"] = label["1"][1]
            
        elif df["Cluster"][i] == 2:
            df["Label"] = label["2"][1]
        
        UpdateCSV(f"{directoryToSave}{fileName}_Label.csv",[
                                                            df["Player"][i],
                                                            df["Week"][i],
                                                            df["Task"][i],
                                                            df["AmountPerWeek"][i],
                                                            df["sMin"][i],
                                                            df["sMax"][i],
                                                            df["Delta"][i],
                                                            df["Cluster"][i],
                                                            df["Label"][i]
                                                         ])
            
            
            
            
            
            
            
            
            