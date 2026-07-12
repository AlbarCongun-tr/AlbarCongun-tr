#!/usr/bin/env python3
"""
pick_weekly_tip.py

Reads the `weekly_tips` list from config.yml, deterministically picks
one entry based on the current ISO week number, and injects it into
README.md between the tip markers. No values are hardcoded — the
entire tip pool lives in config.yml.
"""

import datetime
import re

import yaml

with open("config.yml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

tips = cfg["weekly_tips"]
if not tips:
    raise SystemExit("weekly_tips in config.yml is empty")

week_number = datetime.date.today().isocalendar()[1]
tip = tips[week_number % len(tips)]

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

new_readme = re.sub(
    r"(<!--START_SECTION:tip-->)(.*?)(<!--END_SECTION:tip-->)",
    lambda m: f"{m.group(1)}\n> 💡 {tip}\n{m.group(3)}",
    readme,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print(f"Injected week {week_number} tip: {tip}")
