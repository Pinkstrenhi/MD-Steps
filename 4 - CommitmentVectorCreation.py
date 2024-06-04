import os
import csv
import pandas as pd
from collections import defaultdict

def CreateCSV(filePath, fieldnames):
    with open(filePath, mode="w", encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

def UpdateCSV(csvPath, write):
    with open(csvPath, mode="a", encoding="utf-16", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(write)

directory = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeekAndRole/"
filePath = r"C:/Users/pinks/Desktop/Mestrado/Master/PDM/Final/PerWeekCluster/"

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
        source = f"{directory}Week_{weekInt}_{role}.csv"
        df = pd.read_csv(source, encoding="utf-16")

        players = defaultdict(list)

        columnsInt = inCommon + roles[role]

        for index, row in df.iterrows():
            for task in columnsInt:
                key = f"{task}_{role}"
                players[key].append([row[summonerName], row["matchId"], task, row[task]])

        for task, value in players.items():
            taskName = task.split('_')[0]
            fileName = f"Week_{weekInt}_CommitmentVector_{role}_{taskName}.csv"
            CreateCSV(os.path.join(filePath, fileName), ["Player", "Week", "AmountPerWeek", "sMin", "sMax", "Delta", "Task"])
            for name, week, task, score in value:
                player_values = [entry[3] for entry in value if entry[0] == name]
                sMin = min(player_values)
                sMax = max(player_values)
                scoreDelta = sMax - sMin

                UpdateCSV(os.path.join(filePath, fileName), [name, weekInt, len(player_values), sMin, sMax, scoreDelta, task])
