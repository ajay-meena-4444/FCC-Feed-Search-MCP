from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FeedMCP", version="1.0")

@mcp.tool()
def fcc_news_search(query: str, max_results: int = 3):
    """Search FreecodeCamp news feed via RSS by title/description"""
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "link": entry.get("link", ""),
                "description": description
            })
        if len(results) >= max_results:
            break
    return results or [{"message": "No results found."}]

@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 3):
    """Search FreecodeCamp YouTube channel via RSS by title/description"""
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("media_description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "link": entry.get("link", ""),
                "description": description
            })
        if len(results) >= max_results:
            break
    return results or [{"message": "No results found."}]

@mcp.tool()
def fcc_secret_message():
    """Return a secret message from FreecodeCamp"""
    return "Keep exploring! and happy coding!"

if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8000)