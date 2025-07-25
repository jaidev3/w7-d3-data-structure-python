
posts = [
    {
        "id": 1,
        "username": "alice",
        "content": "Hello, world!",
        "likes": 10,
        "tags": ["tag1", "tag2", "tag3"]
    },
    {
        "id": 2,
        "username": "bob",
        "content": "Hello, world! I'm bob",
        "likes": 20,
        "tags": ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6"]
    },
    {
        "id": 3,
        "username": "alice",
        "content": "Hello, world!",
        "likes": 30,
        "tags": ["tag4", "tag5", "tag6"]
    }
]

users = { "alice":{
    "followers": 100,
    "following": 10
},
"bob":{
    "followers": 200,
    "following": 20
}}

# Most Popular Tags
from collections import Counter

tags = Counter()
for post in posts:
    tags.update(post["tags"])

print(tags.most_common(2))

# User Engagement Analysis
from collections import defaultdict

engagement = defaultdict(int)
for post in posts:
    engagement[post["username"]] += post["likes"]

print(engagement)

# Top Posts by Likes
from operator import itemgetter

top_posts = sorted(posts, key=itemgetter("likes"), reverse=True)
print(top_posts)

# User Activity Summary

user_activity = defaultdict(int)
for post in posts:
    user_activity[post["username"]] += 1

print(user_activity)