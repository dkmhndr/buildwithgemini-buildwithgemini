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

"""Firestore database tools for Pokémon GO catalog management."""

from __future__ import annotations

import functools
from typing import Any
from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-03-f77af6ca33f4"
COLLECTION_NAME = "pokemon_catalog"


@functools.cache
def _get_firestore_client() -> firestore.Client:
    """Returns a cached Firestore client instance using the hardcoded project ID."""
    return firestore.Client(project=PROJECT_ID)


def search_pokemon(
    query: str = "",
    type_filter: str = "",
    league_filter: str = "",
) -> list[dict[str, Any]]:
    """Search the Pokemon GO catalog for Pokemon by name, type, or PvP league.

    Args:
        query: Optional name or partial name of the Pokemon (e.g. 'Swamp', 'Charizard').
        type_filter: Optional Pokemon type to filter by (e.g. 'Water', 'Dragon', 'Steel').
        league_filter: Optional PvP league to filter by (e.g. 'Great League', 'Ultra League', 'Master League').

    Returns:
        A list of matching Pokemon entries from the catalog.
    """
    db = _get_firestore_client()
    docs = db.collection(COLLECTION_NAME).stream()

    results = []
    query_lower = query.strip().lower()
    type_lower = type_filter.strip().lower()
    league_lower = league_filter.strip().lower()

    for doc in docs:
        data = doc.to_dict()
        if not data:
            continue

        name = str(data.get("name", "")).lower()
        types = [str(t).lower() for t in data.get("types", [])]
        best_league = str(data.get("best_pvp_league", "")).lower()

        # Apply filters
        if query_lower and query_lower not in name:
            continue
        if type_lower and not any(type_lower in t for t in types):
            continue
        if league_lower and league_lower not in best_league:
            continue

        results.append(data)

    return results


def get_pokemon_details(name: str) -> dict[str, Any]:
    """Fetch complete Pokemon GO details for a specific Pokemon by name.

    Args:
        name: The exact name of the Pokemon (e.g. 'Swampert', 'Lucario', 'Metagross').

    Returns:
        The Pokemon document dictionary containing types, moves, PvP tier, IV spreads, and counters.
    """
    db = _get_firestore_client()
    doc_id = name.strip().lower().replace(" ", "_").replace("(", "").replace(")", "")
    doc_ref = db.collection(COLLECTION_NAME).document(doc_id)
    doc = doc_ref.get()

    if doc.exists:
        return doc.to_dict() or {}

    # Fallback to search if direct ID lookup fails
    matches = search_pokemon(query=name)
    if matches:
        return matches[0]

    return {"error": f"Pokemon '{name}' not found in the catalog."}


def add_pokemon_entry(
    name: str,
    pokedex_id: int,
    types: list[str],
    fast_moves: list[str],
    charged_moves: list[str],
    best_pvp_league: str,
    pvp_tier: str,
    best_pve_role: str,
    max_cp: int,
    recommended_iv_spread: str,
    weaknesses: list[str],
) -> dict[str, Any]:
    """Add or update a Pokemon entry in the Firestore Pokemon GO catalog.

    Args:
        name: Name of the Pokemon (e.g. 'Garchomp').
        pokedex_id: National Pokedex ID number.
        types: List of elemental types (e.g. ['Dragon', 'Ground']).
        fast_moves: List of optimal Fast Moves (e.g. ['Mud Shot', 'Dragon Tail']).
        charged_moves: List of optimal Charged Moves (e.g. ['Earth Power', 'Outrage']).
        best_pvp_league: Recommended PvP league (e.g. 'Master League').
        pvp_tier: Tier ranking in GO Battle League (e.g. 'Meta S-Tier').
        best_pve_role: Top PvE / Raid role (e.g. 'Top Dragon / Ground Raid Attacker').
        max_cp: Maximum Level 50 CP.
        recommended_iv_spread: Ideal PvP IV spread (e.g. '15/15/15 for Master League').
        weaknesses: List of type weaknesses (e.g. ['Ice (2.56x)', 'Fairy', 'Dragon']).

    Returns:
        Confirmation dictionary with the saved document status.
    """
    db = _get_firestore_client()
    doc_id = name.strip().lower().replace(" ", "_").replace("(", "").replace(")", "")
    entry = {
        "name": name,
        "pokedex_id": pokedex_id,
        "types": types,
        "fast_moves": fast_moves,
        "charged_moves": charged_moves,
        "best_pvp_league": best_pvp_league,
        "pvp_tier": pvp_tier,
        "best_pve_role": best_pve_role,
        "max_cp": max_cp,
        "recommended_iv_spread": recommended_iv_spread,
        "weaknesses": weaknesses,
    }
    db.collection(COLLECTION_NAME).document(doc_id).set(entry)
    return {"status": "success", "message": f"Pokemon '{name}' saved successfully.", "data": entry}
