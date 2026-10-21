#!/usr/bin/env python3
"""Seed script to populate Firestore with initial Pokémon GO catalog data."""

from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-03-f77af6ca33f4"
COLLECTION_NAME = "pokemon_catalog"

POKEMON_SEED_DATA = [
    {
        "name": "Swampert",
        "pokedex_id": 260,
        "types": ["Water", "Ground"],
        "fast_moves": ["Mud Shot", "Water Gun"],
        "charged_moves": ["Hydro Cannon", "Earthquake", "Sludge Wave"],
        "best_pvp_league": "Great League / Ultra League",
        "pvp_tier": "Meta S-Tier",
        "best_pve_role": "Top Water & Ground Raid Attacker (Mega/Shadow)",
        "max_cp": 3362,
        "recommended_iv_spread": "0/14/14 (Rank 1 Great League)",
        "weaknesses": ["Grass (2.56x)"],
    },
    {
        "name": "Lucario",
        "pokedex_id": 448,
        "types": ["Fighting", "Steel"],
        "fast_moves": ["Counter", "Bullet Punch", "Force Palm"],
        "charged_moves": ["Aura Sphere", "Power-Up Punch", "Shadow Ball", "Close Combat"],
        "best_pvp_league": "Ultra League",
        "pvp_tier": "A-Tier (Fighter & Shield Pressure)",
        "best_pve_role": "Top Fighting Raid Attacker & Team GO Rocket Sweeper",
        "max_cp": 3056,
        "recommended_iv_spread": "1/15/15 (Rank 1 Ultra League)",
        "weaknesses": ["Fighting", "Ground", "Fire"],
    },
    {
        "name": "Charizard",
        "pokedex_id": 6,
        "types": ["Fire", "Flying"],
        "fast_moves": ["Fire Spin", "Wing Attack", "Dragon Breath"],
        "charged_moves": ["Blast Burn", "Dragon Claw", "Overheat"],
        "best_pvp_league": "Great League / Ultra League",
        "pvp_tier": "A+ Tier (Wing Attack + Blast Burn)",
        "best_pve_role": "Premier Fire & Dragon Mega Attacker (Mega Charizard Y/X)",
        "max_cp": 3266,
        "recommended_iv_spread": "0/15/13 (Rank 1 Great League)",
        "weaknesses": ["Rock (2.56x)", "Water", "Electric"],
    },
    {
        "name": "Giratina (Altered)",
        "pokedex_id": 487,
        "types": ["Ghost", "Dragon"],
        "fast_moves": ["Shadow Claw", "Dragon Breath"],
        "charged_moves": ["Dragon Claw", "Shadow Sneak", "Ancient Power"],
        "best_pvp_league": "Ultra League / Master League",
        "pvp_tier": "Meta S-Tier (Ultra League Tank King)",
        "best_pve_role": "PvP Specialist & Ultra League Safe Swap",
        "max_cp": 3820,
        "recommended_iv_spread": "1/12/15 (Rank 1 Ultra League)",
        "weaknesses": ["Ghost", "Dark", "Dragon", "Ice", "Fairy"],
    },
    {
        "name": "Metagross",
        "pokedex_id": 376,
        "types": ["Steel", "Psychic"],
        "fast_moves": ["Bullet Punch", "Zen Headbutt"],
        "charged_moves": ["Meteor Mash", "Psychic", "Earthquake"],
        "best_pvp_league": "Master League",
        "pvp_tier": "Meta S-Tier (Premier Master League Anchor)",
        "best_pve_role": "Undisputed #1 Non-Mega Steel Raid Attacker",
        "max_cp": 4286,
        "recommended_iv_spread": "15/15/15 (Rank 1 Master League - 100% IV)",
        "weaknesses": ["Ground", "Fire", "Ghost", "Dark"],
    },
    {
        "name": "Togekiss",
        "pokedex_id": 468,
        "types": ["Fairy", "Flying"],
        "fast_moves": ["Charm", "Air Slash", "Hidden Power"],
        "charged_moves": ["Ancient Power", "Flamethrower", "Dazzling Gleam", "Aura Sphere"],
        "best_pvp_league": "Master League / Ultra League",
        "pvp_tier": "A-Tier (Charm Specialist & Dragon Slayer)",
        "best_pve_role": "Top Tier Fairy Raid Attacker",
        "max_cp": 3767,
        "recommended_iv_spread": "15/15/15 (Rank 1 Master League)",
        "weaknesses": ["Rock", "Steel", "Ice", "Electric", "Poison"],
    },
    {
        "name": "Machamp",
        "pokedex_id": 68,
        "types": ["Fighting"],
        "fast_moves": ["Counter", "Karate Chop", "Bullet Punch"],
        "charged_moves": ["Cross Chop", "Rock Slide", "Close Combat", "Payback"],
        "best_pvp_league": "Great League / Ultra League",
        "pvp_tier": "A-Tier (Classic Fighter & Gym Breaker)",
        "best_pve_role": "Top Gym Attacker & Fighting Raid Anchor (Shadow)",
        "max_cp": 3455,
        "recommended_iv_spread": "0/14/11 (Rank 1 Great League)",
        "weaknesses": ["Psychic", "Flying", "Fairy"],
    },
    {
        "name": "Dragonite",
        "pokedex_id": 149,
        "types": ["Dragon", "Flying"],
        "fast_moves": ["Dragon Breath", "Dragon Tail", "Steel Wing"],
        "charged_moves": ["Dragon Claw", "Superpower", "Outrage", "Hurricane"],
        "best_pvp_league": "Master League / Great League",
        "pvp_tier": "Meta S-Tier (Master League Powerhouse)",
        "best_pve_role": "Top Non-Legendary Dragon Attacker",
        "max_cp": 4287,
        "recommended_iv_spread": "15/15/15 (Rank 1 Master League)",
        "weaknesses": ["Ice (2.56x)", "Dragon", "Fairy", "Rock"],
    },
]


def seed_database():
    print(f"Connecting to Firestore for project '{PROJECT_ID}'...")
    db = firestore.Client(project=PROJECT_ID)
    collection_ref = db.collection(COLLECTION_NAME)

    print(f"Seeding {len(POKEMON_SEED_DATA)} entries into '{COLLECTION_NAME}' collection...")
    for item in POKEMON_SEED_DATA:
        doc_id = item["name"].lower().replace(" ", "_").replace("(", "").replace(")", "")
        collection_ref.document(doc_id).set(item)
        print(f"  ✓ Seeded: {item['name']} (ID: {doc_id})")

    print("\n✅ Firestore seeding completed successfully!")


if __name__ == "__main__":
    seed_database()
