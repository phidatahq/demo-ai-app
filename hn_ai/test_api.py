from hackernews import HackerNews
from rich.pretty import pprint

hn = HackerNews()
# top_stories = hn.top_stories(limit=10)
# pprint(top_stories)
# print(f"top_stories: {type(top_stories)}")
# print(f"top_stories: {len(top_stories)}")


item = hn.get_item(39156444)
if item.kids:
    for kid_id in item.kids[:10]:
        kid = hn.get_item(kid_id)
        pprint(kid.raw)
        print("---------------------------------------------------")
print("---------------------------------------------------")
pprint(item.raw)
