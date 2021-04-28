# auxiliary-goose

A home for additional story-providers for [Goosepaper](https://github.com/j6k4m8/goosepaper) that require nonstandard imports


StoryProviders may incubate here before making their way to the main repo, if I (BDFL) decide that they ought to be moved. If you have a story provider that requires new or nonstandard imports, it's more likely to be merged in here than the main repo.

## Usage

You can use `auxiliarygoose` story providers alongside standardlib story providers. For example:

```python
from goosepaper import Goosepaper
from goosepaper.rss import RSSFeedStoryProvider
# nonstandard story provider:
from auxiliarygoose import Ao3StoryProvider

Goosepaper([
  RSSFeedStoryProvider("..."),
  Ao3StoryProvider(search="Bob Belcher")
]).to_pdf("my-goosepaper.pdf")
```


## Story Providers

| Story Provider | Description | Why is it not in the standard library? |
|----------------|-------------|----------------------------------------|
| `Ao3StoryProvider` | Archive of our Own fanfiction | `AO3` special import (`pip install ao3_api`) |
| `HackerNewsStoryProvider` | Downloaded articles linked from HackerNews | Hacker News is bad |
