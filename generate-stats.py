import json
import os

# Function to calculate language percentages
def calculate_percentages(language_data):
    total_lines = sum(language_data.values())
    return {lang: (lines / total_lines) * 100 for lang, lines in language_data.items()}

# Function to generate a chart URL using quickchart.io
def generate_chart_url(language_percentages):
    labels = ",".join(language_percentages.keys())
    data = ",".join(str(round(value, 2)) for value in language_percentages.values())
    chart_url = (
        "https://quickchart.io/chart/render/zm-cd1c40c6-291e-4317-9f6e-528e56c02bdb"
        f"?title=Language%20Distribution&labels={labels}&data1={data}"
    )
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
                lang_ = lang.replace(' ','-')
                if lang in overall_language_data:
                    overall_language_data[lang] += lines
                else:
                    overall_language_data[lang] = lines

# Calculate percentages and generate chart URL
language_percentages = calculate_percentages(overall_language_data)
chart_url = generate_chart_url(language_percentages)

# Generate Markdown output
output = []
output.append("## My Languages\n")
output.append(f"![Language Stats]({chart_url})\n")

# Save output
with open('stats/output.md', 'w') as f:
    f.write("\n".join(output))
