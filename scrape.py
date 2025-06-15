import praw
import time
from datetime import datetime

# === CONFIGURATION === #
REDDIT_CLIENT_ID = 'your-client-id'
REDDIT_CLIENT_SECRET = 'your-client-secret'
REDDIT_USER_AGENT = 'your user agent name'

KEYWORDS = ["for hire", "developer", "fresh grad","hiring","job","python"]
FETCH_LIMIT = 20
SCRAPE_INTERVAL = 5 * 60  # every 5 minutes

# === INIT REDDIT API === #
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def matches_keywords(text, keywords):
    text_lower = text.lower()
    return any(kw in text_lower for kw in keywords)

def fetch_posts():
    print(f"[{datetime.now()}] Scraping posts...")

    posts = []
    for submission in reddit.subreddit("all").new(limit=100):
        if matches_keywords(submission.title, KEYWORDS) or matches_keywords(submission.selftext, KEYWORDS):
            posts.append({
                "title": submission.title,
                "url": submission.url,
                "score": submission.score,
                "subreddit": str(submission.subreddit),
                "created": datetime.fromtimestamp(submission.created_utc),
                "text": submission.selftext[:200]  # Trim long posts
            })
            if len(posts) >= FETCH_LIMIT:
                break

    print(f"✅ Fetched {len(posts)} relevant posts.")
    return posts

# === MAIN LOOP === #
while True:
    try:
        relevant_posts = fetch_posts()
        for post in relevant_posts:
            print(f"- [{post['subreddit']}] {post['title']} ({post['url']})")
        print("🔁 Waiting for next cycle...\n")
        time.sleep(SCRAPE_INTERVAL)
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        time.sleep(60)  # wait 1 min on failure
