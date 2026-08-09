"""Explicit registration of the auxiliary story providers with goosepaper.

Nothing is registered on import. Call register() yourself to opt in — either all
of them, or only the source types you want:

    import auxiliarygoose
    auxiliarygoose.register()                 # register all of them
    auxiliarygoose.register("ao3", "npr")     # or just some

Once registered, the provider is usable from a goosepaper config / the CLI as
`{"type": "ao3", ...}`, exactly like the built-in providers.
"""

# source type -> ("module:Class", {required, optional} for config validation).
# Providers are given as import strings so goosepaper imports each class (and its
# heavy optional dependency) lazily — only when a paper actually uses that source,
# not at registration time.
_SPECS = {
    "ao3": (
        "auxiliarygoose.Ao3StoryProvider:Ao3StoryProvider",
        {"optional": {"limit", "max_word_count", "author", "title", "search", "fandom"}},
    ),
    "yr": (
        "auxiliarygoose.YrStoryProvider:YrStoryProvider",
        {"optional": {"lat", "lon", "F", "locationName"}},
    ),
    "hackernews": (
        "auxiliarygoose.HackerNewsStoryProvider:HackerNewsStoryProvider",
        {"optional": {"limit", "since_days_ago", "byline", "body_source"}},
    ),
    "npr": (
        "auxiliarygoose.NPRStoryProvider:NPRStoryProvider",
        {
            "required": {"feed_title"},
            "optional": {"limit", "parallel", "since_days_ago", "byline", "body_source"},
        },
    ),
    "nyt": (
        "auxiliarygoose.NYTNewsletterStoryProvider:NYTNewsletterStoryProvider",
        {"optional": {"newsletter_name"}},
    ),
    "miniflux": (
        "auxiliarygoose.MinifluxStoryProvider:MinifluxStoryProvider",
        {
            "required": {"url", "userName", "password", "feedID"},
            "optional": {"limit", "markRead"},
        },
    ),
}


def available():
    """The source types this package can register."""
    return tuple(_SPECS)


def register(*source_types):
    """Register auxiliary providers with goosepaper.

    With no arguments, registers all of them; otherwise only the named source
    types (e.g. register("ao3", "npr")). Raises KeyError for an unknown name.
    """
    from goosepaper.util import register_story_provider

    for source_type in source_types or tuple(_SPECS):
        if source_type not in _SPECS:
            raise KeyError(
                f"Unknown auxiliary provider {source_type!r}; "
                f"available: {', '.join(_SPECS)}."
            )
        module_class, meta = _SPECS[source_type]
        register_story_provider(source_type, module_class, **meta)
