# auxiliary-goose
Additional story-providers for Goosepaper that require nonstandard imports


StoryProviders may incubate here before making their way to the main repo, if I (BDFL) decide that they ought to be moved.

## Story Providers

| Story Provider | Description | Why is it not in the standard library? |
|----------------|-------------|----------------------------------------|
| `Ao3StoryProvider` | Archive of our Own fanfiction | `AO3` special import (`pip install ao3_api`) |
| `HackerNewsStoryProvider` | Downloaded articles linked from HackerNews | Hacker News is bad |
