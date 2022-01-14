from goosepaper.storyprovider import StoryProvider
from goosepaper.story import Story

import requests
from bs4 import BeautifulSoup

_SUPPORTED_NEWSLETTERS = {
    "NYC Briefing": "https://static.nytimes.com/email-content/UR_sample.html",
    "Morning Briefing": "https://static.nytimes.com/email-content/NN_sample.html",
}


class NYTNewsletterStoryProvider(StoryProvider):
    """
    A story provider for  New York Times newsletters.
    """

    def __init__(self, newsletter_name: str = "Morning Briefing"):
        if newsletter_name not in _SUPPORTED_NEWSLETTERS:
            raise ValueError(
                f"{newsletter_name} is not a supported newsletter. Supported newsletters are: {[i for i in _SUPPORTED_NEWSLETTERS.keys()]}"
            )

        self._newsletter_name = newsletter_name

    def get_stories(self, limit: int = 1):
        if limit == 0:
            return []

        url = _SUPPORTED_NEWSLETTERS[self._newsletter_name]
        html = requests.get(url).content.decode("utf-8")
        soup = BeautifulSoup(
            html.replace("margin:0 auto;max-width:600px;width:100%", ""), "html.parser"
        )

        # Get the html of all the paragraphs
        paragraphs = [p for p in soup.find_all("p")]
        p_filtered = []
        for p in paragraphs:
            # get rid of footer:
            if "Need help? Review" in p.text:
                break
            p_filtered.append(p)

        return [
            Story(
                headline=self._newsletter_name,
                body_html="<br />".join([str(p) for p in p_filtered]),
            )
        ]
