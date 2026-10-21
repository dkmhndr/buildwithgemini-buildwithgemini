# ruff: noqa
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

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


from app.tools import (
    add_pokemon_entry,
    get_pokemon_details,
    get_raid_boss_counters,
    search_pokemon,
)


MODEL = "gemini-3.1-pro"


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are the Pokémon GO Companion & Battle Strategist agent.
You help Pokémon GO trainers look up Pokémon stats, analyze GO Battle League (GBL) PvP meta rankings, find top PvE raid counters, and manage their Pokémon catalog.
Use your tools (`get_raid_boss_counters`, `search_pokemon`, `get_pokemon_details`, `add_pokemon_entry`) to fetch real data on raid bosses, counters, weaknesses, and catalog entries.
Provide clear, enthusiastic, and battle-ready advice tailored to Pokémon GO mechanics (types, movesets, CP, and PvP IVs).""",
    tools=[
        get_raid_boss_counters,
        search_pokemon,
        get_pokemon_details,
        add_pokemon_entry,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)

