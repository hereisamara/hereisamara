import json
import os
import requests

# Function to calculate language percentages
def calculate_percentages(language_data):
    total_lines = sum(language_data.values())
    return {lang: (lines / total_lines) * 100 for lang, lines in language_data.items()}

# Function to generate a chart using quickchart.io
def generate_chart(language_percentages):
    labels = list(language_percentages.keys())
    data = list(language_percentages.values())
    chart_url = f"https://quickchart.io/chart?c={{type:'pie',data:{{labels:{labels},datasets:[{{data:{data}}}]}}}}"
    return chart_url

# Gather and process language stats
overall_language_data = {}
repo_list_path = 'repos/repo_list.txt'
if os.path.exists(repo_list_path):
    with open(repo_list_path) as f:
        repos = f.readlines()

    for repo in repos:
        repo = repo.strip()
        repo_sanitized = repo.replace("/", "_")

        languages_path = f'stats/{repo_sanitized}/languages.json'
        if os.path.exists(languages_path):
            with open(languages_path) as f:
                languages = json.load(f)
            for lang, lines in languages.items():
                if lang in overall_language_data:
                    overall_language_data[lang] += lines
                else:
                    overall_language_data[lang] = lines

# Calculate percentages and generate chart URL
language_percentages = calculate_percentages(overall_language_data)
chart_url = generate_chart(language_percentages)

# Generate Markdown output
output = []
output.append("## Private Repository Language Stats\n")
output.append(f"![Language Stats]({chart_url})\n")

# Save output
with open('stats/output.md', 'w') as f:
    f.write("\n".join(output))
