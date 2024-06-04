import pandas as pd
import os

directory = "/home/eloisa.oliveira/Downloads/Datasets/Final/"
csvSource = "/home/eloisa.oliveira/Downloads/Datasets/Final/withoutNaN.csv"
csvName = "preprocessing.csv"
df = pd.read_csv(csvSource)

print(f"Original: {len(df)}")
summonerName = "summonerName"
matchId = "matchId"
roles = "individualPosition"

print("-"*60)

dfInvalid = df[df[roles] == "Invalid"]
dfRoles = df[df[roles] != "Invalid"]
print(f"Invalid: {len(dfInvalid)}\nRoles: {len(dfRoles)}")
print("-"*60)

for key in df.keys():
    if (df[key] == 0).all():
        print(f"Drop: {key}")
        df = df.drop(key,axis = 1)
print("-"*60)

print(f"Without empty columns: {len(df.keys())}")

matchesToRemove_ARAM = "ARAM"
columnToRemoveInfo = "gameMode"

df = df[df[columnToRemoveInfo] != matchesToRemove_ARAM]
print("-"*60)

print(f"Without matches ARAM: {len(df)}")

matchesToRemove_TIME = 600
columnToRemoveInfo = "gameDuration"

df = df[df[columnToRemoveInfo] > matchesToRemove_TIME]

print(f"Without matches 600s or less: {len(df)}")
print("-"*60)

df = df.drop_duplicates(subset = [summonerName,matchId])

print(f"Without duplicates: {len(df)}")
print("-"*60)

dfInvalid = df[df[roles] == "Invalid"]
dfRoles = df[df[roles] != "Invalid"]
print(f"Invalid: {len(dfInvalid)}\nRoles: {len(dfRoles)}")
print("-"*60)

df = df[df[roles] != "Invalid"]

print(f"Without invalid: {len(df)}")
print("-"*60)

df = df.dropna(how = "any",axis = 0)

print(f"Without kills na: {len(df)}")
print("-"*60)

countData = df[matchId].value_counts()
countMatches = pd.DataFrame({matchId: countData.index,"Count": countData.values})
matchesBotToRemove = countMatches[countMatches["Count"] < 10][matchId]
df = df[~df[matchId].isin(matchesBotToRemove)]

print("-"*60)

print(f"Without bot matches: {len(df)}")
print("-"*60)

#df.to_csv(os.path.join(directory,csvName),index = False)        

df = df[df["gameEndedInSurrender"] == False]
print(f"Without surrender: {len(df)}")
print("-"*60)

df.to_csv(os.path.join(directory,"withoutSurrender.csv"),index = False)        





                