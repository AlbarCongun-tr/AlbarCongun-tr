#!/usr/bin/env python3
"""
build_readme.py

Reads config.yml (the single source of truth) and regenerates README.md
from scratch. Nothing in README.md is hand-written or hardcoded — every
value comes from config.yml. Run this locally or let the GitHub Actions
workflow run it on every push to config.yml.
"""

import urllib.parse
import yaml

with open("config.yml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

user = cfg["github_username"]
theme = cfg["theme"]


def badge(name, slug, color, logo_color):
    label = urllib.parse.quote(name.replace(" ", "_"))
    slug_q = urllib.parse.quote(slug) if slug else ""
    logo_part = f"&logo={slug_q}" if slug_q else ""
    return (
        f'<img src="https://img.shields.io/badge/{label}-{color}'
        f'?style=for-the-badge{logo_part}&logoColor={logo_color}" alt="{name}"/>'
    )


def stack_row(title, items):
    badges = "\n".join(
        badge(i["name"], i.get("slug", ""), i["color"], i.get("logoColor", "white"))
        for i in items
    )
    return f"**{title}**\n\n{badges}\n"


typing_lines = ";".join(
    urllib.parse.quote_plus(line) for line in cfg["typing_lines"]
)

about_lines = "\n".join(f"- {line}" for line in cfg["about"])
now_lines = "\n".join(f"- {line}" for line in cfg["now"])

stack = cfg["tech_stack"]
stack_sections = "\n<br/><br/>\n\n".join(
    [
        stack_row("Languages", stack["languages"]),
        stack_row("Frontend", stack["frontend"]),
        stack_row("Backend & Database", stack["backend"]),
        stack_row("Infrastructure & Cloud", stack["infrastructure"]),
        stack_row("Tools & Platforms", stack["tools"]),
        stack_row("Minecraft Platforms", stack["minecraft"]),
    ]
)

project = cfg["project"]
contact = cfg["contact"]

readme = f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:{theme['gradient_from']},100:{theme['gradient_to']}&height=200&section=header&text={urllib.parse.quote(cfg['display_name'])}&fontSize=55&fontColor=FFFFFF&fontAlignY=35&desc={urllib.parse.quote(cfg['tagline'])}&descAlignY=52&descSize=18&descColor=FFFFFF&animation=fadeIn" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=21&pause=1000&color={theme['accent']}&center=true&vCenter=true&width=650&lines={typing_lines}" alt="Typing SVG" />

<br/>

<img src="https://komarev.com/ghpvc/?username={user}&label=Profile+Views&color={theme['accent']}&style=for-the-badge" alt="Profile Views"/>
<img src="https://img.shields.io/github/followers/{user}?label=Followers&style=for-the-badge&color={theme['accent']}" alt="Followers"/>
<img src="https://img.shields.io/github/stars/{user}?label=Stars&style=for-the-badge&color={theme['accent']}" alt="Stars"/>

<br/>
<br/>

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=dark" alt="Random Dev Quote"/>

</div>

<br/>

<div align="center">

## About Me

</div>

{about_lines}

<br/>

<div align="center">

## Right Now

<!--START_SECTION:now-->
{now_lines}
<!--END_SECTION:now-->

*(Edit the `now:` list in `config.yml` to update this — no need to touch README.md.)*

</div>

<br/>

<div align="center">

## {project['name']}

<img src="https://api.loohpjames.com/serverbanner.png?ip={project['banner_ip_for_image']}&width=1836" alt="{project['name']} Server Banner" width="100%"/>

<br/>
<br/>

<img src="https://img.shields.io/badge/Role-{urllib.parse.quote(project['role'])}-{theme['gradient_from']}?style=for-the-badge&logo=minecraft&logoColor=white" alt="Role"/>
<img src="https://img.shields.io/badge/Server%20IP-{project['server_ip']}-{theme['accent']}?style=for-the-badge&logo=minecraft&logoColor=white" alt="Server IP"/>
<img src="https://img.shields.io/badge/Version-{urllib.parse.quote(project['version'])}-{theme['accent']}?style=for-the-badge&logo=minecraft&logoColor=white" alt="Version"/>

<br/>
<br/>

<a href="{project['discord_invite']}">
  <img src="https://img.shields.io/badge/Discord-{urllib.parse.quote(project['name'])}%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="{project['name']} Discord"/>
</a>

</div>

<br/>

<div align="center">

## GitHub Stats

</div>

<div align="center">

<table>
<tr>
<td width="50%">
<img src="https://github-stats-extended.vercel.app/api?username={user}&show_icons=true&count_private=false&bg_color={theme['bg']}&title_color={theme['accent']}&icon_color={theme['accent']}&text_color={theme['text']}&border_color={theme['accent']}&border_radius=10" alt="GitHub Stats" width="100%"/>
</td>
<td width="50%">
<img src="https://github-stats-extended.vercel.app/api/top-langs/?username={user}&layout=compact&langs_count=8&bg_color={theme['bg']}&title_color={theme['accent']}&text_color={theme['text']}&border_color={theme['accent']}&border_radius=10" alt="Top Languages" width="100%"/>
</td>
</tr>
</table>

<img src="https://streak-stats.demolab.com/?user={user}&background={theme['bg']}&ring={theme['accent']}&fire={theme['accent']}&currStreakLabel={theme['accent']}&currStreakNum={theme['text']}&sideNums={theme['text']}&sideLabels=8B949E&dates=8B949E&stroke={theme['accent']}&border={theme['accent']}" alt="GitHub Streak" width="70%"/>

</div>

<br/>

<div align="center">

## Recent Activity

<!--START_SECTION:activity-->
<!-- filled in automatically by the activity-feed workflow -->
<!--END_SECTION:activity-->

</div>

<br/>

<div align="center">

## Weekly Code Tip

<!--START_SECTION:tip-->
<!-- filled in automatically by the weekly-tip workflow, sourced from weekly_tips in config.yml -->
<!--END_SECTION:tip-->

</div>

<br/>

<div align="center">

## Contribution Activity Graph

<img src="https://github-readme-activity-graph.vercel.app/graph?username={user}&bg_color={theme['bg']}&color={theme['accent']}&line={theme['accent']}&point=FFFFFF&area=true&hide_border=true" alt="Activity Graph" width="100%"/>

</div>

<br/>

<div align="center">

## Contribution Snake

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{user}/{user}/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{user}/{user}/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/{user}/{user}/output/github-contribution-grid-snake.svg" width="90%"/>
</picture>

</div>

<br/>

<div align="center">

## Tech Stack

</div>

<div align="center">

{stack_sections}

</div>

<br/>

<div align="center">

## Contact

</div>

<div align="center">

Open to collaborating on Minecraft projects — feel free to reach out.

<a href="{contact['discord_user']}"><img src="https://img.shields.io/badge/Discord-{urllib.parse.quote(contact['discord_label'])}-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"/></a>
<a href="{contact['github']}"><img src="https://img.shields.io/badge/GitHub-{urllib.parse.quote(user)}-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
<a href="mailto:{contact['email']}"><img src="https://img.shields.io/badge/Gmail-{urllib.parse.quote(contact['email'].split('@')[0])}-{theme['accent']}?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>

</div>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:{theme['gradient_from']},100:{theme['gradient_to']}&height=150&section=footer&animation=fadeIn" width="100%"/>

</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md generated from config.yml")
