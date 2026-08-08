from goosepaper.storyprovider.storyprovider import StoryProvider
from goosepaper.story import Story
import AO3


class Ao3StoryProvider(StoryProvider):
    """
    A story provider for An Archive of our Own.

    """

    def __init__(
        self,
        limit: int = 1,
        max_word_count: int = None,
        author: str = None,
        title: str = None,
        search: str = None,
        fandom: str = None,
    ):
        """
        You can pass any set of filtering criteria to get the set intersect.

        For example, passing an author and a word count will return works by
        that author with the requested word count (in contrast with returning
        works that are by that author OR have that word count).

        Arguments:
            limit (int: 1): The maximum number of stories to return
            max_word_count (int: None): The longest work to consider
            author (str: None): An author search filter
            title (str: None): A title search filter
            search (str: None): Any other search keywords

        """
        self.limit = limit
        self.max_word_count = max_word_count
        self.author = author
        self.title = title
        self.search = search
        self.fandom = fandom

    def get_stories(self, limit: int = None):
        """
        Get a list of stories from AO3.

        Arguments:
            limit (int: None): The maximum number of stories to return.
                Defaults to the `limit` passed at construction.

        Returns:
            List[Story]

        """
        limit = self.limit if limit is None else limit
        qry = {}
        if self.max_word_count:
            qry["word_count"] = AO3.utils.Constraint(upperbound=self.max_word_count)
        if self.author:
            qry["author"] = self.author
        if self.title:
            qry["title"] = self.title
        if self.search:
            qry["any_field"] = self.search
        if self.fandom:
            qry["fandoms"] = self.fandom

        try:
            search_results = AO3.Search(**qry)
            search_results.update()
            works = search_results.results
        except Exception as e:
            # AO3 rate-limits by IP; when throttled it returns a page the client
            # can't parse. Degrade to "no AO3 stories today" instead of raising
            # and taking down the whole paper build.
            print(f"AO3: search failed, skipping (rate-limited?) ({type(e).__name__}: {e})")
            return []

        stories = []
        for work in works:
            try:
                work.reload()
                html = work.download("html").decode("utf-8")
                # Keep from the metadata block on when present; otherwise fall
                # back to the whole document rather than dropping the work.
                parts = html.split('<div class="meta">')
                body = '<div class="meta">' + parts[1] if len(parts) > 1 else html
                stories.append(Story(headline=work.title, body_html="<body>" + body))
            except Exception as e:
                print(f"AO3: skipping a work ({type(e).__name__}: {e})")
            if len(stories) >= limit:
                break
        return stories
