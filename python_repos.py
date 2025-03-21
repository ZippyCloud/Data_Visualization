import requests
import plotly.express as px


url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers)
response_dict = r.json()
repo_dicts = response_dict["items"]
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, labels=labels, title="Most-Starred Python Projects on GitHub",  hover_name=hover_texts)
fig.update_layout(title_font_size=24, xaxis_title_font_size=14, yaxis_title_font_size=14)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()