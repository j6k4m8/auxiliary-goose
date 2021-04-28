from goosepaper.rss import RSSFeedStoryProvider

class HackerNewsStoryProvider(RSSFeedStoryProvider):
    
    def __init__(self, limit: int = 5) -> None:
        """
        Get a set of stories from Hacker News.
        
        Arguments:
          limit (int: 5): The maximum number of stories to download
         
        """
        self.limit = limit
        self.feed_url = "https://news.ycombinator.com/rss"
