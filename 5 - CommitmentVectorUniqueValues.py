#Rodar esse primeiro 
#09/04
#Depois separar os valores NaN da base em novos arquivos que serao ignorados
#Depois roda ClusterPerWeekAndCommitmentVector
#Por fim, ClusterLabelForCommitmentVector
import os
import csv
import pandas as pd

def CreateCSV(filePath, fieldnames):
    with open(filePath, mode="w", encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

def UpdateCSV(csvPath, write):
    with open(csvPath, mode="a", encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(write)

directory = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeekCluster/"
filePath = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeekClusterUnique/"

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

commitment = {}

summonerName = "summonerName"

rolesKey = ["TOP", "MIDDLE", "BOTTOM", "UTILITY", "JUNGLE"]

for i in range(40):
    for role in rolesKey:
        weekInt = i + 1
        
        columnsInt = inCommon + roles[role]
        for task in columnsInt:
            fileNameCsv = f"Week_{weekInt}_CommitmentVector_{role}_{task}.csv"
            CreateCSV(os.path.join(filePath, fileNameCsv), ["Player", "Week", "AmountPerWeek", "sMin", "sMax", "Delta", "Task"])
            source = f"{directory}{fileNameCsv}"
            df = pd.read_csv(source,encoding = "utf-16")
            
            dfUnique = df.drop_duplicates(subset=["Player"])
            print(len(dfUnique))
            
            for index,value in dfUnique.iterrows():
                UpdateCSV(os.path.join(filePath, fileNameCsv), [dfUnique["Player"][index],dfUnique["Week"][index],
                                                                 dfUnique["AmountPerWeek"][index],dfUnique["sMin"][index],
                                                                 dfUnique["sMax"][index],dfUnique["Delta"][index],
                                                                 dfUnique["Task"][index]])
            
            
            
            
            
            
            
            
            
            
            
            