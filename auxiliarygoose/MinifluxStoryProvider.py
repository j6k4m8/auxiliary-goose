from goosepaper.storyprovider import StoryProvider
from goosepaper.story import Story

from typing import List
import miniflux


class MinifluxStoryProvider(StoryProvider):
    """
    A story provider for miniflux feeds based on the  feed ID.
    """

    def __init__(
        self,
        url: str,
        userName: str,
        password: str,
        feedID: int,
        limit: int = 1,
        markRead: bool = True,
    ):
        try:
            self._client = miniflux.Client(url, userName, password)
            self._feedID = feedID
            self.limit = limit
            self.markRead = markRead
        except:
            raise ValueError("Check server url and credentials again. ")

    def get_stories(self) -> List[Story]:
        if self.limit == 0:
            return []

        feedEntries = self._client.get_feed_entries(
            self._feedID,
            direction="desc",
            order="published_at",
            limit=self.limit,
            status=["unread"],
        )

        # Merge all articles texts
        content = "<br />".join(
            [entry["content"].strip() for entry in feedEntries["entries"]]
        )

        # Optionally, mark retrieved articles as read on the server
        if self.markRead:
            ids = [entry["id"] for entry in feedEntries["entries"]]
            self._client.update_entries(ids, "read")
        return [
            Story(
                headline=self._client.get_feed(self._feedID)["title"], body_html=content
            ),
        ]
