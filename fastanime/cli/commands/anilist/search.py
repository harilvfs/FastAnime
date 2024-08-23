import click

from ...completion_functions import anime_titles_shell_complete

tags_available = {
    "Cast": ["Polyamorous"],
    "Cast Main Cast": [
        "Anti-Hero",
        "Elderly Protagonist",
        "Ensemble Cast",
        "Estranged Family",
        "Female Protagonist",
        "Male Protagonist",
        "Primarily Adult Cast",
        "Primarily Animal Cast",
        "Primarily Child Cast",
        "Primarily Female Cast",
        "Primarily Male Cast",
        "Primarily Teen Cast",
    ],
    "Cast Traits": [
        "Age Regression",
        "Agender",
        "Aliens",
        "Amnesia",
        "Angels",
        "Anthropomorphism",
        "Aromantic",
        "Arranged Marriage",
        "Artificial Intelligence",
        "Asexual",
        "Butler",
        "Centaur",
        "Chimera",
        "Chuunibyou",
        "Clone",
        "Cosplay",
        "Cowboys",
        "Crossdressing",
        "Cyborg",
        "Delinquents",
        "Demons",
        "Detective",
        "Dinosaurs",
        "Disability",
        "Dissociative Identities",
        "Dragons",
        "Dullahan",
        "Elf",
        "Fairy",
        "Femboy",
        "Ghost",
        "Goblin",
        "Gods",
        "Gyaru",
        "Hikikomori",
        "Homeless",
        "Idol",
        "Kemonomimi",
        "Kuudere",
        "Maids",
        "Mermaid",
        "Monster Boy",
        "Monster Girl",
        "Nekomimi",
        "Ninja",
        "Nudity",
        "Nun",
        "Office Lady",
        "Oiran",
        "Ojou-sama",
        "Orphan",
        "Pirates",
        "Robots",
        "Samurai",
        "Shrine Maiden",
        "Skeleton",
        "Succubus",
        "Tanned Skin",
        "Teacher",
        "Tomboy",
        "Transgender",
        "Tsundere",
        "Twins",
        "Vampire",
        "Veterinarian",
        "Vikings",
        "Villainess",
        "VTuber",
        "Werewolf",
        "Witch",
        "Yandere",
        "Zombie",
    ],
    "Demographic": ["Josei", "Kids", "Seinen", "Shoujo", "Shounen"],
    "Setting": ["Matriarchy"],
    "Setting Scene": [
        "Bar",
        "Boarding School",
        "Circus",
        "Coastal",
        "College",
        "Desert",
        "Dungeon",
        "Foreign",
        "Inn",
        "Konbini",
        "Natural Disaster",
        "Office",
        "Outdoor",
        "Prison",
        "Restaurant",
        "Rural",
        "School",
        "School Club",
        "Snowscape",
        "Urban",
        "Work",
    ],
    "Setting Time": [
        "Achronological Order",
        "Anachronism",
        "Ancient China",
        "Dystopian",
        "Historical",
        "Time Skip",
    ],
    "Setting Universe": [
        "Afterlife",
        "Alternate Universe",
        "Augmented Reality",
        "Omegaverse",
        "Post-Apocalyptic",
        "Space",
        "Urban Fantasy",
        "Virtual World",
    ],
    "Technical": [
        "4-koma",
        "Achromatic",
        "Advertisement",
        "Anthology",
        "CGI",
        "Episodic",
        "Flash",
        "Full CGI",
        "Full Color",
        "No Dialogue",
        "Non-fiction",
        "POV",
        "Puppetry",
        "Rotoscoping",
        "Stop Motion",
    ],
    "Theme Action": [
        "Archery",
        "Battle Royale",
        "Espionage",
        "Fugitive",
        "Guns",
        "Martial Arts",
        "Spearplay",
        "Swordplay",
    ],
    "Theme Arts": [
        "Acting",
        "Calligraphy",
        "Classic Literature",
        "Drawing",
        "Fashion",
        "Food",
        "Makeup",
        "Photography",
        "Rakugo",
        "Writing",
    ],
    "Theme Arts-Music": [
        "Band",
        "Classical Music",
        "Dancing",
        "Hip-hop Music",
        "Jazz Music",
        "Metal Music",
        "Musical Theater",
        "Rock Music",
    ],
    "Theme Comedy": ["Parody", "Satire", "Slapstick", "Surreal Comedy"],
    "Theme Drama": [
        "Bullying",
        "Class Struggle",
        "Coming of Age",
        "Conspiracy",
        "Eco-Horror",
        "Fake Relationship",
        "Kingdom Management",
        "Rehabilitation",
        "Revenge",
        "Suicide",
        "Tragedy",
    ],
    "Theme Fantasy": [
        "Alchemy",
        "Body Swapping",
        "Cultivation",
        "Fairy Tale",
        "Henshin",
        "Isekai",
        "Kaiju",
        "Magic",
        "Mythology",
        "Necromancy",
        "Shapeshifting",
        "Steampunk",
        "Super Power",
        "Superhero",
        "Wuxia",
        "Youkai",
    ],
    "Theme Game": ["Board Game", "E-Sports", "Video Games"],
    "Theme Game-Card & Board Game": [
        "Card Battle",
        "Go",
        "Karuta",
        "Mahjong",
        "Poker",
        "Shogi",
    ],
    "Theme Game-Sport": [
        "Acrobatics",
        "Airsoft",
        "American Football",
        "Athletics",
        "Badminton",
        "Baseball",
        "Basketball",
        "Bowling",
        "Boxing",
        "Cheerleading",
        "Cycling",
        "Fencing",
        "Fishing",
        "Fitness",
        "Football",
        "Golf",
        "Handball",
        "Ice Skating",
        "Judo",
        "Lacrosse",
        "Parkour",
        "Rugby",
        "Scuba Diving",
        "Skateboarding",
        "Sumo",
        "Surfing",
        "Swimming",
        "Table Tennis",
        "Tennis",
        "Volleyball",
        "Wrestling",
    ],
    "Theme Other": [
        "Adoption",
        "Animals",
        "Astronomy",
        "Autobiographical",
        "Biographical",
        "Body Horror",
        "Cannibalism",
        "Chibi",
        "Cosmic Horror",
        "Crime",
        "Crossover",
        "Death Game",
        "Denpa",
        "Drugs",
        "Economics",
        "Educational",
        "Environmental",
        "Ero Guro",
        "Filmmaking",
        "Found Family",
        "Gambling",
        "Gender Bending",
        "Gore",
        "Language Barrier",
        "LGBTQ+ Themes",
        "Lost Civilization",
        "Marriage",
        "Medicine",
        "Memory Manipulation",
        "Meta",
        "Mountaineering",
        "Noir",
        "Otaku Culture",
        "Pandemic",
        "Philosophy",
        "Politics",
        "Proxy Battle",
        "Psychosexual",
        "Reincarnation",
        "Religion",
        "Royal Affairs",
        "Slavery",
        "Software Development",
        "Survival",
        "Terrorism",
        "Torture",
        "Travel",
        "War",
    ],
    "Theme Other-Organisations": [
        "Assassins",
        "Criminal Organization",
        "Cult",
        "Firefighters",
        "Gangs",
        "Mafia",
        "Military",
        "Police",
        "Triads",
        "Yakuza",
    ],
    "Theme Other-Vehicle": [
        "Aviation",
        "Cars",
        "Mopeds",
        "Motorcycles",
        "Ships",
        "Tanks",
        "Trains",
    ],
    "Theme Romance": [
        "Age Gap",
        "Bisexual",
        "Boys' Love",
        "Female Harem",
        "Heterosexual",
        "Love Triangle",
        "Male Harem",
        "Matchmaking",
        "Mixed Gender Harem",
        "Teens' Love",
        "Unrequited Love",
        "Yuri",
    ],
    "Theme Sci Fi": [
        "Cyberpunk",
        "Space Opera",
        "Time Loop",
        "Time Manipulation",
        "Tokusatsu",
    ],
    "Theme Sci Fi-Mecha": ["Real Robot", "Super Robot"],
    "Theme Slice of Life": [
        "Agriculture",
        "Cute Boys Doing Cute Things",
        "Cute Girls Doing Cute Things",
        "Family Life",
        "Horticulture",
        "Iyashikei",
        "Parenthood",
    ],
}
tags_available_list = []
for tag_category, tags_in_category in tags_available.items():
    tags_available_list.extend(tags_in_category)


@click.command(
    help="Search for anime using anilists api and get top ~50 results",
    short_help="Search for anime",
)
@click.option("--title", "-t", shell_complete=anime_titles_shell_complete)
@click.option(
    "--dump-json",
    "-d",
    is_flag=True,
    help="Only print out the results dont open anilist menu",
)
@click.option(
    "--season",
    help="The season the media was released",
    type=click.Choice(["WINTER", "SPRING", "SUMMER", "FALL"]),
)
@click.option(
    "--status",
    "-S",
    help="The media status of the anime",
    multiple=True,
    type=click.Choice(
        ["FINISHED", "RELEASING", "NOT_YET_RELEASED", "CANCELLED", "HIATUS"]
    ),
)
@click.option(
    "--sort",
    "-s",
    help="What to sort the search results on",
    type=click.Choice(
        [
            "ID",
            "ID_DESC",
            "TITLE_ROMAJI",
            "TITLE_ROMAJI_DESC",
            "TITLE_ENGLISH",
            "TITLE_ENGLISH_DESC",
            "TITLE_NATIVE",
            "TITLE_NATIVE_DESC",
            "TYPE",
            "TYPE_DESC",
            "FORMAT",
            "FORMAT_DESC",
            "START_DATE",
            "START_DATE_DESC",
            "END_DATE",
            "END_DATE_DESC",
            "SCORE",
            "SCORE_DESC",
            "POPULARITY",
            "POPULARITY_DESC",
            "TRENDING",
            "TRENDING_DESC",
            "EPISODES",
            "EPISODES_DESC",
            "DURATION",
            "DURATION_DESC",
            "STATUS",
            "STATUS_DESC",
            "CHAPTERS",
            "CHAPTERS_DESC",
            "VOLUMES",
            "VOLUMES_DESC",
            "UPDATED_AT",
            "UPDATED_AT_DESC",
            "SEARCH_MATCH",
            "FAVOURITES",
            "FAVOURITES_DESC",
        ]
    ),
)
@click.option(
    "--genres",
    "-g",
    multiple=True,
    help="the genres to filter by",
    type=click.Choice(
        [
            "Action",
            "Adventure",
            "Comedy",
            "Drama",
            "Ecchi",
            "Fantasy",
            "Horror",
            "Mahou Shoujo",
            "Mecha",
            "Music",
            "Mystery",
            "Psychological",
            "Romance",
            "Sci-Fi",
            "Slice of Life",
            "Sports",
            "Supernatural",
            "Thriller",
            "Hentai",
        ]
    ),
)
@click.option(
    "--tags",
    "-T",
    multiple=True,
    help="the tags to filter by",
    type=click.Choice(tags_available_list),
)
@click.option(
    "--media-format",
    "-f",
    multiple=True,
    help="Media format",
    type=click.Choice(
        ["TV", "TV_SHORT", "MOVIE", "SPECIAL", "OVA", "MUSIC", "NOVEL", "ONE_SHOT"]
    ),
)
@click.option(
    "--year",
    "-y",
    type=click.Choice(
        [
            "1900",
            "1910",
            "1920",
            "1930",
            "1940",
            "1950",
            "1960",
            "1970",
            "1980",
            "1990",
            "2000",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "2023",
            "2024",
        ]
    ),
    help="the year the media was released",
)
@click.option(
    "--on-list/--not-on-list",
    "-L/-no-L",
    help="Whether the anime should be in your list or not",
    type=bool,
)
@click.pass_obj
def search(
    config,
    title,
    dump_json,
    season,
    status,
    sort,
    genres,
    tags,
    media_format,
    year,
    on_list,
):
    from ....anilist import AniList

    success, search_results = AniList.search(
        query=title,
        sort=sort,
        status_in=list(status),
        genre_in=list(genres),
        season=season,
        tag_in=list(tags),
        seasonYear=year,
        format_in=list(media_format),
        on_list=on_list,
    )
    if success:
        if dump_json:
            import json

            print(json.dumps(search_results))
        else:
            from ...interfaces.anilist_interfaces import anilist_results_menu
            from ...utils.tools import FastAnimeRuntimeState

            fastanime_runtime_state = FastAnimeRuntimeState()
            fastanime_runtime_state.anilist_results_data = search_results
            anilist_results_menu(config, fastanime_runtime_state)
    else:
        from sys import exit

        exit(1)
