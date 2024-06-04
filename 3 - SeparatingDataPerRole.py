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
        
source = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeek/"
directoryToSave = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeekAndRole/"

inCommon = [
                "abilityUses","assists","baronTakedowns","deaths","deathsByEnemyChamps","inhibitorKills","inhibitorTakedowns",
                "inhibitorsLost","longestTimeSpentLiving","magicDamageTaken","physicalDamageTaken","pickKillWithAlly",
                "skillshotsDodged","skillshotsHit","takedowns","teamBaronKills","teamRiftHeraldKills","totalDamageTaken",
                "trueDamageDealtToChampions","trueDamageTaken","turretsLost","teamElderDragonKills","objectivesStolenAssists",
                "spell1Casts","spell2Casts","spell3Casts","spell4Casts","legendaryCount","multiKillOneSpell"
                
           ]
columnsId = [
                "region","regionCode",
                "puuid","accountId","matchId","gameCreation","gameDuration",
                "gameStartTimestamp","gameEndTimestamp","gameEndTimestampToDate","gameMode","gameType","platformId","win"
            ]
roles = {
            "TOP" : [
                        "bountyGold","damageDealtToBuildings","damageDealtToTurrets","damageSelfMitigated",
                        "enemyChampionImmobilizations","goldEarned","kills","largestKillingSpree","largestMultiKill",
                        "magicDamageDealt","multikills","physicalDamageDealt","physicalDamageDealtToChampions","soloKills",
                        "totalDamageDealt","totalDamageDealtToChampions","totalMinionsKilled","turretKills","turretPlatesTaken",
                        "turretTakedowns","turretsTakenWithRiftHerald","tookLargeDamageSurvived","multikillsAfterAggressiveFlash"
                    ],
            "MIDDLE" : [
                            "bountyGold","damageDealtToBuildings","damageDealtToTurrets","enemyChampionImmobilizations",
                            "goldEarned","kills","largestKillingSpree","largestMultiKill","magicDamageDealt",
                            "magicDamageDealtToChampions","multikills","physicalDamageDealt","physicalDamageDealtToChampions",
                            "soloKills","totalDamageDealt","totalDamageDealtToChampions","totalMinionsKilled","turretKills",
                            "turretPlatesTaken","multikillsAfterAggressiveFlash"
                    ],
            "BOTTOM" : [
                            "bountyGold","damageDealtToBuildings","damageDealtToObjectives","damageDealtToTurrets","goldEarned",
                            "kills","largestCriticalStrike","largestKillingSpree","largestMultiKill","multikills",
                            "physicalDamageDealt","physicalDamageDealtToChampions","soloKills","totalDamageDealt",
                            "totalDamageDealtToChampions","totalMinionsKilled","turretKills","turretPlatesTaken","turretTakedowns",
                            "multikillsAfterAggressiveFlash"
                            
                    ],
            "JUNGLE" : [
                           "baronKills","bountyGold","controlWardsPlaced","damageDealtToObjectives","damageSelfMitigated",
                           "detectorWardsPlaced","dragonKills","enemyChampionImmobilizations","enemyJungleMonsterKills",
                           "epicMonsterSteals","goldEarned","kills","killsWithHelpFromEpicMonster","largestKillingSpree",
                           "largestMultiKill","magicDamageDealt","multikills","neutralMinionsKilled","physicalDamageDealt",
                           "physicalDamageDealtToChampions","soloBaronKills","soloKills","totalDamageDealt",
                           "totalDamageDealtToChampions","totalHeal","totalTimeCCDealt","trueDamageDealt","wardTakedowns",
                           "wardsGuarded","objectivesStolen","elderDragonKillsWithOpposingSoul","elderDragonMultikills",
                           "multikillsAfterAggressiveFlash"
                       ],
            "UTILITY" : [
                            "completeSupportQuestInTime","controlWardsPlaced","detectorWardsPlaced","enemyChampionImmobilizations",
                            "totalHeal","totalUnitsHealed","visionScore","visionWardsBoughtInGame","wardTakedowns","wardsGuarded",
                            "wardsKilled","wardsPlaced"
                        ]
        }

for file in os.listdir(source):
    filePath = os.path.join(source,file)
    filePathCsv = f"{filePath}/{file}.csv"
    for role, columnsRoles in roles.items():
        csvPath = f"{directoryToSave}/{file}_{role}.csv"
        
        df = pd.read_csv(filePathCsv,encoding = "utf-16")
        df = df[df["individualPosition"] == role]        
        
        columnsPlayerActions = columnsRoles + inCommon
        
        dfId = df[columnsId]
        
        columnsToCsv = []
        for column in df.columns:
            columnsToCsv.append(column)

        CreateCSV(csvPath,columnsId + columnsToCsv)
        
        dfFinal = pd.merge(dfId, df, left_index=True, right_index=True)
        
        for index,row in dfFinal.iterrows():
            UpdateCSV(csvPath,row)
        