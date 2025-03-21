from operator import itemgetter
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

submissions_ids = r.json()
submission_dicts = []
for submission_id in submissions_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")