import json

# Load contributors stats
with open('stats/contributors.json') as f:
    contributors = json.load(f)

# Load languages stats
with open('stats/languages.json') as f:
    languages = json.load(f)

# Generate Markdown content
output = []

output.append("## Private Repository Stats\n")
output.append("### Top Contributors\n")
for contributor in contributors:
    output.append(f"- {contributor['author']['login']}: {contributor['total']} commits")

output.append("\n### Languages\n")
for language, lines in languages.items():
    output.append(f"- {language}: {lines} lines")

# Save output
with open('stats/output.md', 'w') as f:
    f.write("\n".join(output))
