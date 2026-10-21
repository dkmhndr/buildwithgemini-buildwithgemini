# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Raid Boss counter tools for Pokémon GO."""

from __future__ import annotations

from typing import Any

# Curated reference database for popular legendary and mega raid bosses
RAID_BOSS_DATABASE: dict[str, dict[str, Any]] = {
    "rayquaza": {
        "boss": "Rayquaza (Tier 5 / Mega)",
        "types": ["Dragon", "Flying"],
        "weaknesses": ["Ice (Double 2.56x)", "Dragon", "Fairy", "Rock"],
        "top_counters": [
            {"pokemon": "Mamoswine", "fast_move": "Powder Snow", "charged_move": "Avalanche"},
            {"pokemon": "Baxcalibur", "fast_move": "Ice Fang", "charged_move": "Avalanche"},
            {"pokemon": "Glaceon", "fast_move": "Frost Breath", "charged_move": "Avalanche"},
            {"pokemon": "Galarian Darmanitan", "fast_move": "Ice Fang", "charged_move": "Avalanche"},
            {"pokemon": "Mega Rayquaza / Dragonite", "fast_move": "Dragon Breath", "charged_move": "Outrage / Dragon Claw"},
        ],
        "tactical_advice": "Rayquaza has a fatal 2.56x vulnerability to Ice. Bring full Ice teams for an easy duo/trio.",
    },
    "kyogre": {
        "boss": "Kyogre (Tier 5 / Primal)",
        "types": ["Water"],
        "weaknesses": ["Electric", "Grass"],
        "top_counters": [
            {"pokemon": "Kartana", "fast_move": "Razor Leaf", "charged_move": "Leaf Blade"},
            {"pokemon": "Zekrom", "fast_move": "Charge Beam", "charged_move": "Fusion Bolt"},
            {"pokemon": "Xurkitree", "fast_move": "Thunder Shock", "charged_move": "Discharge"},
            {"pokemon": "Mega Sceptile", "fast_move": "Bullet Seed", "charged_move": "Frenzy Plant"},
            {"pokemon": "Raikou (Shadow)", "fast_move": "Thunder Shock", "charged_move": "Wild Charge"},
        ],
        "tactical_advice": "Beware of Blizzard as Kyogre's charged move which can wipe Grass counters. In Rainy weather, Electric types shine.",
    },
    "groudon": {
        "boss": "Groudon (Tier 5 / Primal)",
        "types": ["Ground"],
        "weaknesses": ["Water", "Grass", "Ice"],
        "top_counters": [
            {"pokemon": "Primal Kyogre / Swampert", "fast_move": "Water Gun", "charged_move": "Origin Pulse / Hydro Cannon"},
            {"pokemon": "Kartana", "fast_move": "Razor Leaf", "charged_move": "Leaf Blade"},
            {"pokemon": "Mega Blastoise", "fast_move": "Water Gun", "charged_move": "Hydro Cannon"},
            {"pokemon": "Zarude", "fast_move": "Vine Whip", "charged_move": "Power Whip"},
            {"pokemon": "Mamoswine", "fast_move": "Powder Snow", "charged_move": "High Horsepower / Avalanche"},
        ],
        "tactical_advice": "Water types dominate especially under Rainy weather; beware of Solar Beam from Groudon.",
    },
    "mewtwo": {
        "boss": "Mewtwo (Tier 5 / Shadow / Mega)",
        "types": ["Psychic"],
        "weaknesses": ["Dark", "Ghost", "Bug"],
        "top_counters": [
            {"pokemon": "Mega Tyranitar / Hydreigon", "fast_move": "Bite", "charged_move": "Brutal Swing / Crunch"},
            {"pokemon": "Mega Gengar", "fast_move": "Shadow Claw", "charged_move": "Shadow Ball"},
            {"pokemon": "Giratina (Origin)", "fast_move": "Shadow Claw", "charged_move": "Shadow Force"},
            {"pokemon": "Darkrai", "fast_move": "Snarl", "charged_move": "Dark Pulse / Shadow Ball"},
            {"pokemon": "Chandelure", "fast_move": "Hex", "charged_move": "Shadow Ball"},
        ],
        "tactical_advice": "Dark-types resist Mewtwo's Psychic moves, while Ghost-types deal maximum burst DPS.",
    },
    "dialga": {
        "boss": "Dialga (Tier 5 / Origin)",
        "types": ["Steel", "Dragon"],
        "weaknesses": ["Fighting", "Ground"],
        "top_counters": [
            {"pokemon": "Lucario (Mega/Standard)", "fast_move": "Force Palm / Counter", "charged_move": "Aura Sphere"},
            {"pokemon": "Primal Groudon / Landorus (Therian)", "fast_move": "Mud Shot", "charged_move": "Precipice Blades / Sandsear Storm"},
            {"pokemon": "Terrakion", "fast_move": "Double Kick", "charged_move": "Sacred Sword"},
            {"pokemon": "Machamp (Shadow)", "fast_move": "Counter", "charged_move": "Dynamic Punch"},
            {"pokemon": "Conkeldurr", "fast_move": "Counter", "charged_move": "Dynamic Punch"},
        ],
        "tactical_advice": "Steel removes Dialga's Dragon and Ice weaknesses. Focus strictly on top-tier Fighting and Ground attackers.",
    },
    "kartana": {
        "boss": "Kartana (Tier 5 Ultra Beast)",
        "types": ["Grass", "Steel"],
        "weaknesses": ["Fire (Double 2.56x)", "Fighting"],
        "top_counters": [
            {"pokemon": "Mega Charizard Y", "fast_move": "Fire Spin", "charged_move": "Blast Burn"},
            {"pokemon": "Reshiram", "fast_move": "Fire Fang", "charged_move": "Fusion Flare"},
            {"pokemon": "Heatran", "fast_move": "Fire Spin", "charged_move": "Magma Storm"},
            {"pokemon": "Blaziken (Mega)", "fast_move": "Fire Spin", "charged_move": "Blast Burn"},
            {"pokemon": "Chandelure", "fast_move": "Fire Spin", "charged_move": "Overheat"},
        ],
        "tactical_advice": "Kartana takes 2.56x damage from Fire attacks and has a low stamina stat. A single high-level Fire team can easily solo it in Sunny weather.",
    },
}


def get_raid_boss_counters(boss_name: str, weather_condition: str = "Clear/Extreme") -> dict[str, Any]:
    """Fetch the top Pokemon GO raid counters, elemental weaknesses, and battle strategies against a raid boss.

    Args:
        boss_name: The name of the Raid Boss (e.g. 'Rayquaza', 'Kyogre', 'Dialga', 'Mewtwo', 'Kartana').
        weather_condition: Optional in-game weather condition (e.g. 'Sunny/Clear', 'Rainy', 'Windy', 'Snowy', 'Cloudy', 'Fog').

    Returns:
        A dictionary containing the boss profile, critical weaknesses, top 5 counter Pokemon with optimal movesets, and weather tactical tips.
    """
    key = boss_name.strip().lower().replace("mega ", "").replace("primal ", "").replace("origin ", "").strip()

    # Direct match or partial match in database
    for db_key, data in RAID_BOSS_DATABASE.items():
        if key in db_key or db_key in key:
            weather_tip = ""
            if "sunny" in weather_condition.lower() or "clear" in weather_condition.lower():
                weather_tip = "Sunny/Clear weather boosts Fire and Ground attackers by 20%."
            elif "rain" in weather_condition.lower():
                weather_tip = "Rainy weather boosts Water, Electric, and Bug attackers by 20%."
            elif "snow" in weather_condition.lower():
                weather_tip = "Snowy weather boosts Ice and Steel attackers by 20%."
            elif "cloud" in weather_condition.lower():
                weather_tip = "Cloudy weather boosts Fighting, Poison, and Fairy attackers by 20%."
            elif "wind" in weather_condition.lower():
                weather_tip = "Windy weather boosts Dragon, Flying, and Psychic attackers by 20%."

            result = dict(data)
            result["active_weather"] = weather_condition
            if weather_tip:
                result["weather_boost_effect"] = weather_tip
            return result

    # Generic fallback for any other boss
    return {
        "boss": boss_name.title(),
        "status": "custom_lookup",
        "note": f"Boss '{boss_name}' analyzed dynamically. Recommend using super-effective STAB attackers matching its typing vulnerabilities.",
        "active_weather": weather_condition,
    }
