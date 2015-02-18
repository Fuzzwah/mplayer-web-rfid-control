import sqlite3

db = sqlite3.connect("cards.sqlite")
c = db.cursor()

playlists = [["0006912739", "False", "StarshipAmazing-ThePowerofScienceisStaggering"],
["0006922093", "False", "RegularFries-AccepttheSignal"],
["0006709949", "False", "QueensOfTheStoneAge-LikeClockwork"],
["0006910231", "False", "UNKLE-NeverNeverLand"],
["0006913839", "False", "Gorillaz-Gorillaz"],
["0006905341", "False", "BobMarley-OneLoveTheVeryBestOf"],
["0006765127", "False", "Avalanches-SinceILeftYou"],
["0006753787", "False", "BlissNEso-FlyingColours"],
["0006923076", "False", "ArcadeFire-Funeral"],
["0006925210", "False", "AtTheDrive-in-AcrobaticTenement"],
["0006670642", "False", "Juggling"],
["0006326173", "False", "HilltopHoods-TheHardRoadRestrung"],
["0006317732", "True", "BestOfBootie"],
["0006313006", "False", "JimmyCliff-TheBestOfJimmyCliff"],
["0006312818", "True", "Dubstep"],
["0006316016", "False", "MumfordAndSons-SighNoMore"],
["0006322562", "True", "Muse"],
["0006322742", "True", "NiN"],
["0006311303", "True", "Prodigy"],
["0006158454", "True", "Radiohead"],
["0006108366", "True", "DanceAroundHappyMusic"],
["0006680517", "False", "1GiantLeap-1GiantLeap"],
["0006679456", "False", "Blackalicious-BlazingArrow"],
["0005918219", "False", "BustaRhymes-FromTheComingToTheBigBang"],
["0006221843", "False", "Cake-FashionNugget"],
["0006242709", "False", "CatEmpire-TwoShoes"],
["0006255299", "True", "Chopin"],
["0005935473", "False", "Clubroot"],
["0006237059", "False", "DaftPunk-RandomAccessMemories"],
["0006014741", "False", "DeathInVegas-ScorpioRising"],
["0005942214", "True", "DeepForest"],
["0006021183", "True", "Summer"],
["0006014555", "True", "Tricky"],
["0006009903", "True", "Portishead"],
["0005922567", "False", "QueensOfTheStoneAge-RatedR"],
["0005931146", "True", "RageAgainstTheMachine"],
["0005919576", "True", "TameImpala"],
["0005928678", "True", "DJShadow"],
["0006240931", "False", "TheBeatles-Love"],
["0006203330", "False", "Soundtrack-LifeAquatic"],
["0006111963", "True", "SoulCoughing"],
["0006239976", "True", "RJD2"],
["0006228641", "False", "PrimalScream-XTRMNTR"],
["0006676335", "True", "Primus"],
["0006925066", "True", "Jazz"],
["0006246862", "False", "FuzzysPlaylist"],
["0006014901", "True", "KaiserChiefs"],
["0006008784", "True", "ChemicalBrothers"],
["0006045328", "False", "ImagineDragons-NightVisions"],
["0005939805", "True", "Bowie"],
["0006781375", "True", "BeastieBoys"],
["0006803473", "True", "BasementJaxx"],
["0006812794", "False", "Bond"],
["0006795193", "True", "CrystalMethod"],
["0006795462", "False", "AtTheDrive-in-RelationshipOfCommand"],
["0006799020", "False", "AtTheDrive-in-InCasinoOut"],
["0006795704", "False", "ArcadeFire-NeonBible"],
["0006809682", "True", "MeFirstAndTheGimmeGimmes"],
["0006807218", "True", "RichardCheese"],
["0006797042", "False", "ArcadeFire-Suburbs"],
["0006776979", "True", "EasyStarAllStars"],
["0006799679", "True", "PearlJam"],
["0006796144", "False", "Emancipator-SoonItWillBeColdEnough"],
["0006799939", "True", "DandyWarhols"],
["0006802741", "True", "Deftones"],
["0006769896", "True", "CafeDelMar"],
["0006789469", "True", "Blockhead"],
["0006777565", "True", "EsbjornSvenssonTrio"],
["0006790555", "True", "Faithless"],
["0006783161", "True", "Goldfrapp"],
["0006781949", "True", "Gomez"],
["0006811337", "True", "GrooveArmada"],
["0006779308", "False", "RegularFries-WarOnPlasticPlants"],
["0006811788", "True", "RodrigoyGabriela"],
["0006782530", "True", "RXBandits"],
["0006782724", "False", "FearandLoathinginLasVegas"],
["0006777367", "True", "BlackKeys"],
["0006779781", "False", "ThemCrookedVultures"],
["0006807072", "True", "ThieveryCorporation"],
["0006815538", "True", "Tool"],
["0006783495", "True", "Wolfmother"],
["0006785607", "True", "Pixies"],
["0006808584", "False", "TheMarsVolta-De-lousedInTheComatorium"]]

for pl in playlists:
	query = "INSERT OR REPLACE INTO Cards (cardnum, item, type, shuffle) values ('%s', '%s.m3u', 'playlist', '%s')" % (pl[0], pl[2], pl[1])
	print(query)
	c.execute(query)
	db.commit()
	
db.close()
