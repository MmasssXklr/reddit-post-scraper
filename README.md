# Reddit Job Scraper Bot

A Python-based Reddit scraper that automatically scans all subreddits every 5 minutes for posts containing job-related keywords (e.g., "hiring", "developer", "fresh grad", etc.). Built using the PRAW (Python Reddit API Wrapper) library.

## Features

- Scans the newest 100 posts from r/all every 5 minutes
- Filters posts by relevant keywords
- Outputs post title, subreddit, URL, and a short text snippet
- Automatically retries on failure
- Designed for lightweight, continuous execution

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-job-scraper.git
cd reddit-job-scraper
```

### 2. Install Dependencies

Ensure you have Python 3 installed, then install the required package:

```bash
pip install praw
```

### 3. Configure Reddit API Credentials

You must set up a Reddit API application to use this bot.

1. Visit: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **Create another app**
3. Set type to **script**
4. Copy the following credentials:

- `client_id`
- `client_secret`
- `user_agent` (e.g., `job_scraper_bot by u/yourusername`)

Then, open the script and **replace the placeholders** in the configuration section:

```python
REDDIT_CLIENT_ID = 'your_client_id'
REDDIT_CLIENT_SECRET = 'your_client_secret'
REDDIT_USER_AGENT = 'your_user_agent'
```

### 4. Run the Script

```bash
python reddit_scraper.py
```

The bot will continuously fetch relevant job-related posts every 5 minutes.

## Customization

- **Keywords**: Modify the `KEYWORDS` list to match your target use case.
- **Frequency**: Adjust the `SCRAPE_INTERVAL` (in seconds) to set how often the scraper runs.
- **Fetch Limit**: Change `FETCH_LIMIT` to control how many matching posts to collect each cycle.

## Disclaimer

Use responsibly. This bot accesses Reddit via its public API and must comply with Reddit's API usage policy and rate limits.
