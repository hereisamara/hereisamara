import json
import os

output = []

output.append("## Private Repository Language Stats\n")

repo_list_path = 'repos/repo_list.txt'
if os.path.exists(repo_list_path):
    with open(repo_list_path) as f:
        repos = f.readlines()

    for repo in repos:
        repo = repo.strip()
        output.append(f"### {repo}\n")

        languages_path = f'stats/{repo}-languages.json'
        if os.path.exists(languages_path):
            with open(languages_path) as f:
                languages = json.load(f)
            output.append("#### Languages\n")
            for language, lines in languages.items():
                output.append(f"- {language}: {lines} lines")

        output.append("\n")

# Save output
with open('stats/output.md', 'w') as f:
    f.write("\n".join(output))
