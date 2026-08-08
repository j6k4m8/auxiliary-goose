from goosepaper.storyprovider.rss import RSSFeedStoryProvider


class HackerNewsStoryProvider(RSSFeedStoryProvider):
    def __init__(self, limit: int = 5, **kwargs) -> None:
        """
        Get a set of stories from Hacker News.

        Arguments:
          limit (int: 5): The maximum number of stories to download

        Extra keyword arguments (since_days_ago, byline, body_source) are passed
        through to RSSFeedStoryProvider.
        """
        super().__init__("https://news.ycombinator.com/rss", limit=limit, **kwargs)
