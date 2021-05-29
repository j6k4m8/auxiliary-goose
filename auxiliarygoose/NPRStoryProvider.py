from goosepaper.rss import RSSFeedStoryProvider

_LOOKUP = [
    {"title": "Africa", "code": 1126, "description": "Africa"},
    {
        "title": "Analysis",
        "code": 1059,
        "description": "Analysis by NPR commentators, including Ted Koppel. Subscribe to our free podcast.",
    },
    {"title": "Animals", "code": 1132, "description": "Animals"},
    {"title": "Architecture", "code": 1142, "description": "Architecture"},
    {
        "title": "Art & Design",
        "code": 1047,
        "description": "NPR explores the visual arts including design, photography, sculpture, and architecture. Interviews, commentary, and audio. Subscribe to the RSS feed.",
    },
    {
        "title": "Arts & Life",
        "code": 1008,
        "description": "Art and entertainment commentary plus interviews, book reviews, movie reviews, music reviews, comedy, and visual art. Subscribe to podcasts and follow trends in music, painting, art, architecture, photography, and design.",
    },
    {"title": "Asia", "code": 1125, "description": "Asia"},
    {
        "title": "Author Interviews",
        "code": 1033,
        "description": "NPR interviews with top authors and the NPR Book Tour, a weekly feature and podcast where leading authors read and discuss their writing. Subscribe to the RSS feed.",
    },
    {
        "title": "Book News & Features",
        "code": 1161,
        "description": "Headlines, trends and profiles from the world of publishing.",
    },
    {
        "title": "Book Reviews",
        "code": 1034,
        "description": "Summary judgment on books of note, from NPR personalities, independent booksellers and critics from across the public-radio spectrum.",
    },
    {
        "title": "Books",
        "code": 1032,
        "description": "NPR's brings you news about books and authors along with our picks for great reads. Interviews, reviews, and much more.",
    },
    {
        "title": "Business",
        "code": 1006,
        "description": "Find the latest business news with reports on Wall Street, interest rates, banking, companies, and U.S. and world financial markets. Subscribe to the Business Story of the Day podcast.",
    },
    {
        "title": "Children's Health",
        "code": 1030,
        "description": "NPR reports on children's health and medical news including health insurance, new treatments for diseases, and child product safety recalls. Subscribe to the RSS feed.",
    },
    {"title": "Dance", "code": 1145, "description": "Dance"},
    {
        "title": "Diversions",
        "code": 1051,
        "description": "Irrestible and odd stories from news, culture, sports, and literature. Subscribe to the Diversions RSS feed.",
    },
    {
        "title": "Economy",
        "code": 1017,
        "description": "NPR news on the U.S. and world economy, the World Bank, and Federal Reserve. Commentary on economic trends. Subscribe to NPR Economy podcasts and RSS feeds.",
    },
    {
        "title": "Education",
        "code": 1013,
        "description": "We've been to school. We know how education works. Right? In fact, many aspects of learning — in homes, at schools, at work and elsewhere — are evolving rapidly, along with our understanding of learning. Join us as we explore how learning happens.",
    },
    {
        "title": "Elections",
        "code": 139482413,
        "description": "Explore NPR's latest election coverage.",
    },
    {"title": "Energy", "code": 1131, "description": "Energy"},
    {
        "title": "Environment",
        "code": 1025,
        "description": "Breaking news on the environment, climate change, pollution, and endangered species. Also featuring Climate Connections, a special series on climate change co-produced by NPR and National Geographic.",
    },
    {"title": "Europe", "code": 1124, "description": "Europe"},
    {"title": "Family", "code": 1164, "description": "Family"},
    {"title": "Fine Art", "code": 1141, "description": "Fine Art"},
    {
        "title": "Fitness & Nutrition",
        "code": 1134,
        "description": "Fitness & Nutrition",
    },
    {
        "title": "Food",
        "code": 1053,
        "description": "Stories on food, nutrition, recipes, cooking, cookbook reviews, and health. Download Food and Hidden Kitchen podcasts and subscribe to RSS feeds.",
    },
    {"title": "Games", "code": 820593993, "description": "Games"},
    {
        "title": "Games & Humor",
        "code": 1052,
        "description": "Games, puzzles, and contests plus odd stories from comedy, art, and society.",
    },
    {
        "title": "Gardening",
        "code": 1054,
        "description": "NPR stories about gardening, plants, and food crops. Read interviews and commentary and subscribe to the Gardening RSS feed.",
    },
    {
        "title": "Global Health",
        "code": 1031,
        "description": "NPR news on world health issues, disease control, public health and sanitation, and health education. Subscribe to the RSS feed.",
    },
    {"title": "Health", "code": 1128, "description": "Health"},
    {
        "title": "Health Care",
        "code": 1027,
        "description": "The state of health care, health insurance, new medical research, disease prevention, and drug treatments. Interviews, news, and commentary from NPR's correspondents. Subscribe to podcasts.",
    },
    {"title": "History", "code": 1136, "description": "History"},
    {
        "title": "Home Page Top Stories",
        "code": 1002,
        "description": "NPR delivers breaking national and world news. Also top stories from business, politics, health, science, technology, music, arts and culture. Subscribe to podcasts and RSS feeds.",
    },
    {
        "title": "House & Senate Races",
        "code": 139545299,
        "description": "Explore NPR's latest coverage of the 2012 congressional contests.",
    },
    {
        "title": "Investigations",
        "code": 1150,
        "description": "Read the latest from NPR's investigative team. If you have solid tips or documents on stories we should probe, please send them to us.",
    },
    {"title": "Latin America", "code": 1127, "description": "Latin America"},
    {
        "title": "Law",
        "code": 1070,
        "description": "NPR stories on legal issues, court rulings, Supreme Court hearings, new laws and government investigations. Download the NPR Justice Talking podcast and subscribe to the Legal Affairs RSS feed.",
    },
    {
        "title": "Lost & Found Sound",
        "code": 1074,
        "description": "NPR's Lost & Found Sound series explores newly discovered audio and music sessions, home audio, and listener submitted sounds and interviews. Subscribe to the RSS feed of never before played audio and sounds.",
    },
    {
        "title": "Low-Wage America",
        "code": 1076,
        "description": "NPR stories about low-wage America, the income gap between rich and poor, affordable housing, welfare, medicaid, social security, and healthcare for the working poor.",
    },
    {
        "title": "Media",
        "code": 1020,
        "description": "News about the state of the media. Trends in broadcast and print media, television, and radio journalism. Download podcasts and RSS feeds.",
    },
    {"title": "Medical Treatments", "code": 1135, "description": "Medical Treatments"},
    {
        "title": "Mental Health",
        "code": 1029,
        "description": "NPR covers mental health, happiness, depression, and treatment options. Subscribe to the RSS feed.",
    },
    {
        "title": "Middle East",
        "code": 1009,
        "description": "Middle East news, arts, culture, and politics. Updates on Iraq, Israel, Palestine, Iran, OPEC, and the Persian Gulf states NPR streaming audio. Subscribe to the Middle East RSS feed.",
    },
    {"title": "Movie Interviews", "code": 1137, "description": "Movie Interviews"},
    {
        "title": "Movie Reviews",
        "code": 4467349,
        "description": "Reviews of new movies, classic and art films, foreign films, and popular movies. Featuring Bob Mondello, Kenneth Turan, David Edelstein, and Mark Jenkins.",
    },
    {
        "title": "Movies",
        "code": 1045,
        "description": "NPR Movies podcast, movie reviews, and commentary on new and classic films. Interviews with filmmakers, actors, and actresses.",
    },
    {
        "title": "National",
        "code": 1003,
        "description": "NPR coverage of national news, U.S. politics, elections, business, arts, culture, health and science, and technology. Subscribe to the NPR Nation RSS feed.",
    },
    {"title": "National Security", "code": 1122, "description": "National Security"},
    {
        "title": "News",
        "code": 1001,
        "description": "NPR news, audio, and podcasts. Coverage of breaking stories, national and world news, politics, business, science, technology, and extended coverage of major national and world events.",
    },
    {
        "title": "Obituaries",
        "code": 1062,
        "description": "NPR remembrances of remarkable individuals.",
    },
    {
        "title": "On Aging",
        "code": 1028,
        "description": "NPR stories and audio on aging, longevity, retirement, and senior issues. More articles on health care, leisure, disease prevention, and housing. Subscribe to the RSS feed.",
    },
    {"title": "On Disabilities", "code": 1133, "description": "On Disabilities"},
    {
        "title": "Opinion",
        "code": 1057,
        "description": "Editorial opinions and commentary on news events and world events. Download podcasts and subscribe to RSS feeds.",
    },
    {
        "title": "Performing Arts",
        "code": 1046,
        "description": "News, interviews, and commentary on theater, the arts, music, and dance.",
    },
    {"title": "Photography", "code": 1143, "description": "Photography"},
    {
        "title": "Politics",
        "code": 1014,
        "description": "NPR's expanded coverage of U.S. and world politics, the latest news from Congress and the White House, and elections.",
    },
    {
        "title": "Pop Culture",
        "code": 1048,
        "description": "News and commentary on popular culture trends. Download the Pop Culture podcast.",
    },
    {
        "title": "Presidential Race",
        "code": 139544303,
        "description": "Explore NPR's latest coverage of the race for the White House.",
    },
    {
        "title": "Race",
        "code": 1015,
        "description": "NPR stories on race and ethnicity and race's effects on politics, culture, society.",
    },
    {
        "title": "Radio Expeditions",
        "code": 1023,
        "description": "A co-production of NPR and the National Geographic Society. Explore our world's environments, cultures, and wildlife through interviews, narrative, and sounds. Subscribe to the Radio Expeditions RSS feed.",
    },
    {"title": "Recipes", "code": 1139, "description": "Recipes"},
    {
        "title": "Religion",
        "code": 1016,
        "description": "NPR's stories on U.S. and world religion, spirituality, ethics, and moral issues affecting society and culture. Subscribe to NPR Religion RSS feeds.",
    },
    {
        "title": "Research News",
        "code": 1024,
        "description": "New advances in science, medicine, health, and technology.Stem cell research, drug research, and new treatments for disease.",
    },
    {
        "title": "Science",
        "code": 1007,
        "description": "The latest health and science news. Updates on medicine, healthy living, nutrition, drugs, diet, and advances in science and technology. Subscribe to the Health & Science podcast.",
    },
    {
        "title": "Sen. Barack Obama (D-IL)",
        "code": 1117,
        "description": "Browse NPR coverage of Democratic presidential candidate Illinois Sen. Barack Obama.",
    },
    {
        "title": "Sen. Hillary Clinton (D-NY)",
        "code": 1116,
        "description": "Browse NPR coverage of Democratic presidential candidate New York Sen. Hillary Clinton.",
    },
    {
        "title": "Sen. John McCain (R-AZ)",
        "code": 1118,
        "description": "Browse NPR coverage of Republican presidential candidate Arizona Sen. John McCain.",
    },
    {
        "title": "Sen. Joseph Biden (D-DE)",
        "code": 1119,
        "description": "Browse NPR coverage of Democratic vice-presidential candidate Delaware Sen. Joseph Biden.",
    },
    {
        "title": "Social Security Debate",
        "code": 1083,
        "description": "News and analysis on the Social Security debate. Pending legislation, political viewpoints, and news about retirement. Subscribe to the Social Security RSS feed.",
    },
    {
        "title": "Space",
        "code": 1026,
        "description": "NPR coverage of space exploration, space shuttle missions, news from NASA, private space exploration, satellite technology, and new discoveries in astronomy and astrophysics.",
    },
    {"title": "Sports", "code": 1055, "description": "NPR sports news and interviews."},
    {
        "title": "Statewide Races",
        "code": 139545485,
        "description": "Explore NPR's coverage of gubernatorial contests, ballot issues and other statewide elections in 2012.",
    },
    {
        "title": "Strange News",
        "code": 1146,
        "description": "Unlikely stories from around the nation and the world.",
    },
    {
        "title": "Summer",
        "code": 1088,
        "description": "NPR stories about summer. Living, eating, diversions, health, and summer traditions. Subscribe to the Summer RSS feed.",
    },
    {
        "title": "Summer Reading: Cooking",
        "code": 1087,
        "description": "Fresh recipes and cookbooks for summer reading. Subscribe to the RSS feed.",
    },
    {
        "title": "Summer Reading: Fiction",
        "code": 1085,
        "description": "Selections for great summer fiction. Book reviews, excerpts, and author interviews. Suscribe to the Summer Fiction RSS feed.",
    },
    {
        "title": "Summer Reading: Kids",
        "code": 1086,
        "description": "NPR's selections of summer reading for kids. Excerpts, interviews, and reviews. Subscribe to RSS feeds.",
    },
    {
        "title": "Summer Reading: Nonfiction",
        "code": 1089,
        "description": "Selections for great summer nonfiction. Book reviews, excerpts, and author interviews. Suscribe to the Summer Reading Nonfiction RSS feed.",
    },
    {
        "title": "Technology",
        "code": 1019,
        "description": "Latest technology news and breakthroughs in technology, science, and industry. Download the NPR Technology podcast and Technology RSS feed.",
    },
    {"title": "Television", "code": 1138, "description": "Television"},
    {
        "title": "The Second Term",
        "code": 1077,
        "description": "NPR stories about George W. Bush's second term as 43rd President of the United States",
    },
    {"title": "Theater", "code": 1144, "description": "Theater"},
    {"title": "TV Reviews", "code": 1163, "description": "TV Reviews"},
    {"title": "Weather", "code": 1165, "description": "Weather"},
    {
        "title": "World",
        "code": 1004,
        "description": "NPR world news, international art and culture, world business and financial markets, world economy, and global trends in health, science and technology. Subscribe to the World Story of the Day podcast and RSS feed.",
    },
    {
        "title": "Your Health",
        "code": 1066,
        "description": "News and commentary about personal health, medicine, healthcare, drugs, diet, recipes, and nutrition. Download the Your Health podcast and subscribe to our RSS feed.",
    },
    {
        "title": "Your Money",
        "code": 1018,
        "description": "NPR coverage of personal finance, money, investing, taxes, retirement, mortgages and housing markets, wealth management, and stock market news. Download NPR podcasts and RSS feeds.",
    },
    {
        "title": "Blues",
        "code": 139998151,
        "description": "NPR Music stories that feature blues music.",
    },
    {
        "title": "Classical",
        "code": 10003,
        "description": "Classical music performances and features from NPR news, NPR cultural programs, and NPR Music stations.",
    },
    {
        "title": "Concerts",
        "code": 1109,
        "description": "Performances from today's top artists, filmed at venues and festivals across the country.",
    },
    {
        "title": "Country",
        "code": 92792712,
        "description": "Performances and stories featuring traditions and innovations in American roots and country music.",
    },
    {
        "title": "Electronic/Dance",
        "code": 135408474,
        "description": "Explore NPR Music's collection of stories and songs in the electronica/dance genre.",
    },
    {
        "title": "Folk",
        "code": 139999257,
        "description": "NPR Music stories featuring folk music.",
    },
    {"title": "Gospel", "code": 735750628, "description": "NPR Gospel"},
    {
        "title": "Hip-Hop",
        "code": 10005,
        "description": "The home of NPR's hip-hop coverage.",
    },
    {
        "title": "In Performance",
        "code": 1040,
        "description": "Listen to new music, podcasts, live concerts and studio sessions. Watch video sessions. Read interviews with musicians and music reviews. NPR covers the best new songs from rock, pop, folk, jazz, urban, world, and classical music.",
    },
    {
        "title": "Jazz",
        "code": 10002,
        "description": "Jazz and blues music performances and features from NPR news, NPR cultural programs, and NPR Music stations.",
    },
    {
        "title": "Latin",
        "code": 139996449,
        "description": "NPR Music stories featuring Latin Alternative music.",
    },
    {"title": "Mixed Format", "code": 853031894, "description": "Mixed Format music"},
    {
        "title": "Music",
        "code": 1039,
        "description": "NPR Music features, streams, live concerts and music news.",
    },
    {
        "title": "Music Features",
        "code": 613820055,
        "description": "In-depth storytelling from the NPR Music team.",
    },
    {
        "title": "Music Interviews",
        "code": 1105,
        "description": "Interviews with top musicians from jazz, blues, rock, pop, folk, classical, urban, and world music. Listen online to live studio sessions and musician interviews and watch video sessions.",
    },
    {
        "title": "Music Lists",
        "code": 1107,
        "description": "Lists of top artists and top songs compiled by musicians, critics, and noted NPR hosts.",
    },
    {
        "title": "Music News",
        "code": 1106,
        "description": "Current music news, artist interviews, album reviews, and music industry news from NPR Music.",
    },
    {
        "title": "Music Quizzes",
        "code": 1151,
        "description": "Puzzlers from the NPR Music team.",
    },
    {
        "title": "Music Reviews",
        "code": 1104,
        "description": "Music reviews of new albums in pop, rock, folk, jazz, blues, classical, world, and hip-hop.",
    },
    {
        "title": "Music Videos",
        "code": 1110,
        "description": "Watch new music videos and live NPR studio sessions featuring top musicians. Discover songs and listen online. NPR covers the best pop, rock, urban, jazz, folk, blues, world, and classical music.",
    },
    {
        "title": "New Music",
        "code": 1108,
        "description": "Here's what we're listening to.",
    },
    {
        "title": "Other",
        "code": 10006,
        "description": "Songs that don't fit into other categories",
    },
    {
        "title": "Pop",
        "code": 139997200,
        "description": "NPR Music stories that discuss pop music.",
    },
    {
        "title": "R&B/Soul",
        "code": 139998808,
        "description": "NPR Music stories that feature R&B and soul music.",
    },
    {"title": "Reggae", "code": 740095648, "description": "ENTER TEASER"},
    {
        "title": "Rock",
        "code": 10001,
        "description": "Rock, pop, and folk music performances and features from NPR news, NPR cultural programs, and NPR Music stations.",
    },
    {
        "title": "Studio Sessions",
        "code": 1103,
        "description": "Musicians perform and discuss their work in the studios of NPR and NPR Music station partners. Live music sessions, interviews, and the best new songs in rock, pop, folk, classical, jazz, blues, urban, and world music. Watch video sessions.",
    },
    {
        "title": "World",
        "code": 10004,
        "description": "World music and features from NPR news, NPR cultural programs, and NPR Music stations.",
    },
]


class NPRStoryProvider(RSSFeedStoryProvider):
    def __init__(self, feed_title: str, limit: int = 5, parallel: bool = True) -> None:
        self.limit = limit
        self._parallel = parallel
        for category in _LOOKUP:
            if feed_title == category["title"]:
                self.feed_url = f"https://feeds.npr.org/{category['code']}/rss.xml"
                break
        else:
            raise ValueError(
                f"Could not find a NPR feed with the title '{feed_title}'.\n"
                "Try searching for a category here: https://legacy.npr.org/api/mappingCodes.php"
            )
