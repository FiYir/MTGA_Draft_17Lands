import pytest
import os
from src.dataset import Dataset
from src.utils import Result
from src.constants import DATA_FIELD_GIHWR

# 17Lands OTJ data from 2024-4-16 to 2024-5-3
OTJ_PREMIER_SNAPSHOT = os.path.join(os.getcwd(), "tests", "data","OTJ_PremierDraft_Data_2024_5_3.json")

OTJ_GET_IDS_BY_NAME_TESTS_PASS = [
    (["Rest in Peace", "Thoughtseize", "Djinn of Fool's Fall", "Slick Sequence"], False, ["87050", "90718", "90389", "90579"]),
    (["Rest in Peace", "Thoughtseize", "Djinn of Fool's Fall", "Slick Sequence"], True, [87050, 90718, 90389, 90579]),
    (["Brazen Borrower", "Fake Card", "Mentor of the Meek", "Crime /// Punishment"], False, ["90652", "90737"]),
    (["Brazen Borrower", "Fake Card", "Mentor of the Meek", "Crime /// Punishment"], True, [90652, 90737]),
    (["Consign /// Oblivion", "Shock", "Enlisted Wurm"], False, []),
    (["Consign /// Oblivion", "Shock", "Enlisted Wurm"], True, []),
    ([], False, []),
    ([], True, []),
]

OTJ_GET_NAMES_BY_ID_TESTS_PASS = [
    (["73807", "73905", "90389", "90579"], ["Rest in Peace", "Thoughtseize", "Djinn of Fool's Fall", "Slick Sequence"]),
    ([73807, 73905, 90389, 90579], ["Rest in Peace", "Thoughtseize", "Djinn of Fool's Fall", "Slick Sequence"]),
    (["70186", "90737"], ["Brazen Borrower", "Crime /// Punishment"]),
    ([70186, 90737], ["Brazen Borrower", "Crime /// Punishment"]),
    (["73807", "73905", "ABCD", 90579], ["Rest in Peace", "Thoughtseize", "Slick Sequence"]),
    (["73807", "73905", "", 90579], ["Rest in Peace", "Thoughtseize", "Slick Sequence"]),
    ([], []),
]

OTJ_GET_DATA_BY_ID_TEST_PASS = [
    (["73807"], [{"name": "Rest in Peace", "cmc": 2, "mana_cost": "{1}{W}"}]),
    ([73807], [{"name": "Rest in Peace", "cmc": 2, "mana_cost": "{1}{W}"}]),
    ([90389], [{"name": "Djinn of Fool's Fall", "cmc": 5, "mana_cost": "{4}{U}"}]),
    (["73905", 90389], [{"name": "Thoughtseize", "cmc": 1, "mana_cost": "{B}"},{"name": "Djinn of Fool's Fall", "cmc": 5, "mana_cost": "{4}{U}"}]),
    ([], []),
]

OTJ_GET_DATA_BY_NAME_TEST_PASS = [
    (["Rest in Peace"], [{"name": "Rest in Peace", "cmc": 2, "mana_cost": "{1}{W}"}]),
    (["Djinn of Fool's Fall"], [{"name": "Djinn of Fool's Fall", "cmc": 5, "mana_cost": "{4}{U}"}]),
    (["Thoughtseize", "Djinn of Fool's Fall"], [{"name": "Thoughtseize", "cmc": 1, "mana_cost": "{B}"},{"name": "Djinn of Fool's Fall", "cmc": 5, "mana_cost": "{4}{U}"}]),
    ([], []),
]

OTJ_HARDBRISTLE_BANDIT_ARCHETYPE_DATA = [
    ["", "All Decks", 55.88, 76984],
    ["Selesnya", "WG", 55.73, 18851],
    ["Golgari", "BG", 57.23, 17442],
    ["Gruul", "RG", 54.26, 10838],
    ["Simic", "UG", 55.59, 8925],
    ["Sultai", "UBG", 58.9, 4175],
    ["Naya", "WRG", 55.73, 3734],
    ["Abzan", "WBG", 54.6, 3590],
    ["Bant", "WUG", 53.63, 2657],
    ["Jund", "BRG", 54.84, 2336],
    ["Temur", "URG", 55.69, 1968],
    ["Green", "G", 60.09, 917]
]

OTJ_GET_ALL_NAMES_TEST_PASS = [
 "Another Round",
 "Archangel of Tithes",
 "Armored Armadillo",
 "Aven Interrupter",
 "Bounding Felidar",
 "Bovine Intervention",
 "Bridled Bighorn",
 "Claim Jumper",
 "Dust Animus",
 "Eriette's Lullaby",
 "Final Showdown",
 "Fortune, Loyal Steed",
 "Frontier Seeker",
 "Getaway Glamer",
 "High Noon",
 "Holy Cow",
 "Inventive Wingsmith",
 "Lassoed by the Law",
 "Mystical Tether",
 "Nurturing Pixie",
 "Omenport Vigilante",
 "One Last Job",
 "Outlaw Medic",
 "Prairie Dog",
 "Prosperity Tycoon",
 "Requisition Raid",
 "Rustler Rampage",
 "Shepherd of the Clouds",
 "Sheriff of Safe Passage",
 "Stagecoach Security",
 "Steer Clear",
 "Sterling Keykeeper",
 "Sterling Supplier",
 "Take Up the Shield",
 "Thunder Lasso",
 "Trained Arynx",
 "Vengeful Townsfolk",
 "Wanted Griffin",
 "Archmage's Newt",
 "Canyon Crab",
 "Daring Thunder-Thief",
 "Deepmuck Desperado",
 "Djinn of Fool's Fall",
 "Double Down",
 "Duelist of the Mind",
 "Emergent Haunting",
 "Failed Fording",
 "Fblthp, Lost on the Range",
 "Fleeting Reflection",
 "Geralf, the Fleshwright",
 "Geyser Drake",
 "Harrier Strix",
 "Jailbreak Scheme",
 "The Key to the Vault",
 "Loan Shark",
 "Marauding Sphinx",
 "Metamorphic Blast",
 "Nimble Brigand",
 "Outlaw Stitcher",
 "Peerless Ropemaster",
 "Phantom Interference",
 "Plan the Heist",
 "Razzle-Dazzler",
 "Seize the Secrets",
 "Shackle Slinger",
 "Shifting Grift",
 "Slickshot Lockpicker",
 "Slickshot Vault-Buster",
 "Spring Splasher",
 "Step Between Worlds",
 "Stoic Sphinx",
 "Stop Cold",
 "Take the Fall",
 "This Town Ain't Big Enough",
 "Three Steps Ahead",
 "Visage Bandit",
 "Ambush Gigapede",
 "Binding Negotiation",
 "Blacksnag Buzzard",
 "Blood Hustler",
 "Boneyard Desecrator",
 "Caustic Bronco",
 "Consuming Ashes",
 "Corrupted Conviction",
 "Desert's Due",
 "Desperate Bloodseeker",
 "Fake Your Own Death",
 "Forsaken Miner",
 "Gisa, the Hellraiser",
 "Hollow Marauder",
 "Insatiable Avarice",
 "Kaervek, the Punisher",
 "Lively Dirge",
 "Mourner's Surprise",
 "Neutralize the Guards",
 "Nezumi Linkbreaker",
 "Overzealous Muscle",
 "Pitiless Carnage",
 "Rakish Crew",
 "Rattleback Apothecary",
 "Raven of Fell Omens",
 "Rictus Robber",
 "Rooftop Assassin",
 "Rush of Dread",
 "Servant of the Stinger",
 "Shoot the Sheriff",
 "Skulduggery",
 "Tinybones Joins Up",
 "Tinybones, the Pickpocket",
 "Treasure Dredger",
 "Unfortunate Accident",
 "Unscrupulous Contractor",
 "Vadmir, New Blood",
 "Vault Plunderer",
 "Brimstone Roundup",
 "Calamity, Galloping Inferno",
 "Caught in the Crossfire",
 "Cunning Coyote",
 "Deadeye Duelist",
 "Demonic Ruckus",
 "Discerning Peddler",
 "Explosive Derailment",
 "Ferocification",
 "Gila Courser",
 "Great Train Heist",
 "Hell to Pay",
 "Hellspur Brute",
 "Hellspur Posse Boss",
 "Highway Robbery",
 "Irascible Wolverine",
 "Iron-Fist Pulverizer",
 "Longhorn Sharpshooter",
 "Magda, the Hoardmaster",
 "Magebane Lizard",
 "Mine Raider",
 "Outlaws' Fury",
 "Prickly Pair",
 "Quick Draw",
 "Quilled Charger",
 "Reckless Lackey",
 "Resilient Roadrunner",
 "Return the Favor",
 "Rodeo Pyromancers",
 "Scalestorm Summoner",
 "Scorching Shot",
 "Slickshot Show-Off",
 "Stingerback Terror",
 "Take for a Ride",
 "Terror of the Peaks",
 "Thunder Salvo",
 "Trick Shot",
 "Aloe Alchemist",
 "Ankle Biter",
 "Beastbond Outcaster",
 "Betrayal at the Vault",
 "Bristlepack Sentry",
 "Bristly Bill, Spine Sower",
 "Cactarantula",
 "Colossal Rattlewurm",
 "Dance of the Tumbleweeds",
 "Drover Grizzly",
 "Freestrider Commando",
 "Freestrider Lookout",
 "Full Steam Ahead",
 "Giant Beaver",
 "Gold Rush",
 "Goldvein Hydra",
 "Hardbristle Bandit",
 "Intrepid Stablemaster",
 "Map the Frontier",
 "Ornery Tumblewagg",
 "Outcaster Greenblade",
 "Outcaster Trailblazer",
 "Patient Naturalist",
 "Railway Brawler",
 "Rambling Possum",
 "Raucous Entertainer",
 "Reach for the Sky",
 "Rise of the Varmints",
 "Smuggler's Surprise",
 "Snakeskin Veil",
 "Spinewoods Armadillo",
 "Spinewoods Paladin",
 "Stubborn Burrowfiend",
 "Throw from the Saddle",
 "Trash the Town",
 "Tumbleweed Rising",
 "Voracious Varmint",
 "Akul the Unrepentant",
 "Annie Flash, the Veteran",
 "Annie Joins Up",
 "Assimilation Aegis",
 "At Knifepoint",
 "Badlands Revival",
 "Baron Bertram Graywater",
 "Bonny Pall, Clearcutter",
 "Breeches, the Blastmaker",
 "Bruse Tarl, Roving Rancher",
 "Cactusfolk Sureshot",
 "Congregation Gryff",
 "Doc Aurlock, Grizzled Genius",
 "Eriette, the Beguiler",
 "Ertha Jo, Frontier Mentor",
 "Form a Posse",
 "Ghired, Mirror of the Wilds",
 "The Gitrog, Ravenous Ride",
 "Honest Rutstein",
 "Intimidation Campaign",
 "Jem Lightfoote, Sky Explorer",
 "Jolene, Plundering Pugilist",
 "Kambal, Profiteering Mayor",
 "Kellan Joins Up",
 "Kellan, the Kid",
 "Kraum, Violent Cacophony",
 "Laughing Jasper Flint",
 "Lazav, Familiar Stranger",
 "Lilah, Undefeated Slickshot",
 "Make Your Own Luck",
 "Malcolm, the Eyes",
 "Marchesa, Dealer of Death",
 "Miriam, Herd Whisperer",
 "Obeka, Splitter of Seconds",
 "Oko, the Ringleader",
 "Pillage the Bog",
 "Rakdos Joins Up",
 "Rakdos, the Muscle",
 "Riku of Many Paths",
 "Roxanne, Starfall Savant",
 "Ruthless Lawbringer",
 "Satoru, the Infiltrator",
 "Selvala, Eager Trailblazer",
 "Seraphic Steed",
 "Slick Sequence",
 "Taii Wakeen, Perfect Shot",
 "Vial Smasher, Gleeful Grenadier",
 "Vraska Joins Up",
 "Vraska, the Silencer",
 "Wrangler of the Damned",
 "Wylie Duke, Atiin Hero",
 "Bandit's Haul",
 "Boom Box",
 "Gold Pan",
 "Lavaspur Boots",
 "Luxurious Locomotive",
 "Mobile Homestead",
 "Oasis Gardener",
 "Redrock Sentinel",
 "Silver Deputy",
 "Sterling Hound",
 "Tomb Trawler",
 "Abraded Bluffs",
 "Arid Archway",
 "Bristling Backwoods",
 "Conduit Pylons",
 "Creosote Heath",
 "Eroded Canyon",
 "Festering Gulch",
 "Forlorn Flats",
 "Jagged Barrens",
 "Lonely Arroyo",
 "Lush Oasis",
 "Mirage Mesa",
 "Sandstorm Verge",
 "Soured Springs",
 "Jace Reawakened",
 "Bucolic Ranch",
 "Blooming Marsh",
 "Botanical Sanctum",
 "Concealed Courtyard",
 "Inspiring Vantage",
 "Spirebluff Canal",
 "Stoneforge Mystic",
 "Brazen Borrower",
 "Desertion",
 "Morbid Opportunist",
 "Port Razer",
 "Scapeshift",
 "Mystic Snake",
 "Notion Thief",
 "Desert",
 "Prismatic Vista",
 "Collector's Cage",
 "Grand Abolisher",
 "Oltec Matterweaver",
 "Rest in Peace",
 "Esoteric Duplicator",
 "Simulacrum Synthesizer",
 "Worldwalker Helm",
 "Greed's Gambit",
 "Harvester of Misery",
 "Hostile Investigator",
 "Generous Plunderer",
 "Legion Extruder",
 "Memory Vessel",
 "Molten Duplication",
 "Territory Forge",
 "Ancient Cornucopia",
 "Bristlebud Farmer",
 "Omenpath Journey",
 "Sandstorm Salvager",
 "Vaultborn Tyrant",
 "Loot, the Key to Everything",
 "Pest Control",
 "Lost Jitte",
 "Lotus Ring",
 "Nexus of Becoming",
 "Sword of Wealth and Power",
 "Torpor Orb",
 "Transmutation Font",
 "Fomori Vault",
 "Tarnation Vista",
 "Fell the Mighty",
 "Fierce Retribution",
 "Journey to Nowhere",
 "Leyline Binding",
 "Pariah",
 "Path to Exile",
 "Archive Trap",
 "Archmage's Charm",
 "Commandeer",
 "Essence Capture",
 "Mana Drain",
 "Mindbreak Trap",
 "Repulse",
 "Heartless Pillage",
 "Imp's Mischief",
 "Murder",
 "Overwhelming Forces",
 "Reanimate",
 "Surgical Extraction",
 "Thoughtseize",
 "Collective Defiance",
 "Crackle with Power",
 "Electrodominance",
 "Fling",
 "Indomitable Creativity",
 "Skewer the Critics",
 "Skullcrack",
 "Clear Shot",
 "Force of Vigor",
 "Pest Infestation",
 "Primal Command",
 "Primal Might",
 "Thornado",
 "Abrupt Decay",
 "Anguished Unmaking",
 "Back for More",
 "Bedevil",
 "Buried in the Garden",
 "Crime /// Punishment",
 "Cruel Ultimatum",
 "Decimate",
 "Decisive Denial",
 "Detention Sphere",
 "Endless Detour",
 "Fractured Identity",
 "Hindering Light",
 "Humiliate",
 "Hypothesizzle",
 "Ionize",
 "Oko, Thief of Crowns",
 "Outlaws' Merriment",
 "Ride Down",
 "Savage Smash",
 "Siphon Insight",
 "Terminal Agony",
 "Tyrant's Scorn",
 "Vanishing Verse",
 "Villainous Wealth",
 "Void Rend",
 "Voidslime",
 "Contagion Engine",
 "Grindstone",
 "Mindslaver",
 "Unlicensed Hearse",
 "Dust Bowl"
]

@pytest.fixture(name="otj_dataset", scope="module")
def fixture_otj_dataset():
    dataset = Dataset()
    dataset.open_file(OTJ_PREMIER_SNAPSHOT)
    return dataset
    
@pytest.mark.parametrize("name_list, return_int, expected_ids", OTJ_GET_IDS_BY_NAME_TESTS_PASS)
def test_otj_get_ids_by_name(otj_dataset, name_list, return_int, expected_ids):
    assert otj_dataset.get_ids_by_name(name_list, return_int) == expected_ids
    
@pytest.mark.parametrize("id_list, expected_names", OTJ_GET_NAMES_BY_ID_TESTS_PASS)
def test_otj_get_names_by_id(otj_dataset, id_list,  expected_names):
    assert otj_dataset.get_names_by_id(id_list) == expected_names
    
@pytest.mark.parametrize("id_list, expected_data", OTJ_GET_DATA_BY_ID_TEST_PASS)
def test_otj_get_data_by_id(otj_dataset, id_list, expected_data):
    data_list = otj_dataset.get_data_by_id(id_list)
    assert len(data_list) == len(expected_data)
    
    for i in range(len(data_list)):
        # Compare the matching fields, ignoring all of the other fields
        assert all(data_list[i].get(key) == expected_data[i].get(key) for key in data_list[i].keys() & expected_data[i].keys()), f"Get Data by ID: Collected:{data_list[i]}, Expected:{expected_data[i]}"
    
@pytest.mark.parametrize("name_list, expected_data", OTJ_GET_DATA_BY_NAME_TEST_PASS)
def test_otj_get_data_by_name(otj_dataset, name_list, expected_data):
    data_list = otj_dataset.get_data_by_name(name_list)
    assert len(data_list) == len(expected_data)
    
    for i in range(len(data_list)):
        # Compare the matching fields, ignoring all of the other fields
        assert all(data_list[i].get(key) == expected_data[i].get(key) for key in data_list[i].keys() & expected_data[i].keys()), f"Get Data by Name: Collected:{data_list[i]}, Expected:{expected_data[i]}"
    
def test_open_file_fail():
    dataset = Dataset()
    assert Result.ERROR_MISSING_FILE == dataset.open_file("fake_location")
    
def test_get_all_names(otj_dataset):
    name_list = otj_dataset.get_all_names()
    assert set(name_list) == set(OTJ_GET_ALL_NAMES_TEST_PASS)

def test_get_card_archetypes_by_field_fail_invalid_name(otj_dataset):
    """
    Verify that an empty list is returned if the card name is not in the dataset
    """
    archetype_list = otj_dataset.get_card_archetypes_by_field("FakeCard", DATA_FIELD_GIHWR)
    assert not archetype_list
    
def test_get_card_archetypes_by_field_fail_invalid_field(otj_dataset):
    """
    Verify that an empty list is returned if the field doesn't exist
    """
    archetype_list = otj_dataset.get_card_archetypes_by_field("Hardbristle Bandit", "fakefield")
    assert not archetype_list
    
def test_get_card_archetypes_by_field_fail_empty(otj_dataset):
    """
    Verify that an empty list is returned when the arguments are valid, but no archetype data is available
    """
    archetype_list = otj_dataset.get_card_archetypes_by_field("Rest in Peace", DATA_FIELD_GIHWR)
    assert not archetype_list
    
def test_get_card_archetypes_by_field_pass(otj_dataset):
    """
    Verify that a list of archetypes is returned 
    """
    archetype_list = otj_dataset.get_card_archetypes_by_field("Hardbristle Bandit", DATA_FIELD_GIHWR)
    assert archetype_list == OTJ_HARDBRISTLE_BANDIT_ARCHETYPE_DATA
    
