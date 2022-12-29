from typing import Iterator, TypedDict
from io import TextIOWrapper

class _Metadatum(TypedDict, total=False):
    exclude: bool

class Metadatum(_Metadatum):
    file: str
    title: str
    source: str

_metadata: list[Metadatum] = [
    {
        "file": "god_rest_ye",
        "title": "God Rest Ye Merry, Gentlemen",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/god_rest_you_merry_gentlemen.htm",
    },
    {
        "file": "what_child",
        "title": "What Child Is This?",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/what_child_is_this_version_1.htm",
    },
    {
        "file": "boars_head",
        "title": "The Boar's Head Carol",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/boars_head_carol.htm",
    },
    {
        "file": "joy_to",
        "title": "Joy to the World",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/joy_to_the_world-1.htm",
    },
    {
        "file": "fathers_love",
        "title": "Of the Father's Love Begotten",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/of_the_fathers_love_begotten-1.htm",
        "exclude": True,
    },
    {
        "file": "angel_gabriel",
        "title": "The Angel Gabriel from Heaven Came",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/gabriels_message.htm",
        "exclude": True,
    },
    {
        "file": "wenceslas",
        "title": "Good King Wenceslas",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/good_king_wenceslas.htm",
    },
    {
        "file": "ding_dong",
        "title": "Ding Dong Merrily on High",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/ding_dong_merrily_on_high.htm",
    },
    {
        "file": "puer_natus",
        "title": "Puer Natus in Bethlehem",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/NonEnglish/puer_natus_in_bethlehem-dreves.htm",
        "exclude": False,
    },
    {
        "file": "rose_eer",
        "title": "Lo, How a Rose E'er Blooming",
        "source": "",
        "exclude": True,
    },
    {
        "file": "home_alone",
        "title": "Somewhere in My Memory (Home Alone)",
        "source": "https://genius.com/John-williams-home-alone-main-title-somewhere-in-my-memory-lyrics",
        "exclude": True,
    },
    {
        "file": "dominick",
        "title": "Dominick the Donkey",
        "source": "https://www.lyrics.com/lyric/22100837/Dominick+the+Donkey",
        "exclude": True,
    },
    {
        "file": "lord_of_hosts",
        "title": "Praise Ye the Lord",
        "source": "https://hymnary.org/text/o_praise_the_blessed_lord_of_hosts",
        "exclude": True,
    },
    {
        "file": "ye_faithful",
        "title": "O Come, All Ye Faithful",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/o_come_all_ye_faithful2.htm",
    },
    {
        "file": "adeste",
        "title": "Adeste Fidelis",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/NonEnglish/adeste_fideles.htm",
    },
    {
        "file": "midnight",
        "title": "It Came Upon the Midnight Clear",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/it_came_upon_the_midnight_clear.htm",
    },
    {
        "file": "angels_we_have_heard_on_high",
        "title": "Angels We Have Heard on High",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/angels_we_have_heard_on_high_1.htm",
    },
    {
        "file": "wassail",
        "title": "Gloucestershire Wassail",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/wassail_wassail_all_over_1.htm",
    },
    {
        "file": "o_holy_night",
        "title": "O Holy Night",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/o_holy_night.htm",
    },
    {
        "file": "go_tell_it_on_the_mountain",
        "title": "Go Tell It on the Mountain",
        "source": "https://www.azlyrics.com/lyrics/forkingcountry/gotellitonthemountain.html",
        "exclude": True,
    },
    {
        "file": "we_three_kings",
        "title": "We Three Kings",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/we_three_kings_of_orient_are.htm",
    },
    {
        "file": "the_first_noel",
        "title": "The First Noel",
        "source": "https://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/first_nowel.htm",
    },
    {
        "file": "hark_the_herald",
        "title": "Hark! The Hearld Angels Sing",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/hark_the_herald_angels_sing.htm",
    },
    {
        "file": "little_drummer_boy",
        "title": "Little Drummer Boy",
        "source": "http://www.songlyrics.com/traditional-christmas/the-little-drummer-boy-lyrics/",
        "exclude": True,
    },
    {
        "file": "i_saw_three_ships",
        "title": "I Saw Three Ships",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/i_saw_three_ships.htm",
    },
    {
        "file": "silent_night",
        "title": "Silent Night, Holy Night",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/silent_night_holy_night-1.htm",
    },
    {
        "file": "away_in",
        "title": "Away in a Manger",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/away_in_a_manger.htm",
    },
    {
        "file": "good_christian_friends",
        "title": "Good Christian Men, Rejoice",
        "source": "http://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/good_christian_friends_rejoice.htm",
    },
    {
        "file": "gaudete",
        "title": "Gaudete",
        "source": "",
        "exclude": True,
    },
    {
        "file": "we_wish",
        "title": "We Wish You a Merry Christmas",
        "source": "https://www.hymnsandcarolsofchristmas.com/Hymns_and_Carols/we_wish_you_a_merry_christmas.htm",
        "exclude": False,
    },
    {
        "file": "o_little_town",
        "title": "O Little Town of Bethlehem",
        "source": "",
        "exclude": False,
    },
]

# <script type="text/javascript">setTimeout(() => window.location.reload(true), 3000);</script>
HEADER_HTML = """
<html>
<meta charset="UTF-8">
<head>
</head>
<body>
    <h1 id="title">Brookline Carol Book</h1>
"""

FOOTER_HTML = """
</body>
</html>
"""


def make_index_html(metadata: list[Metadatum]) -> Iterator[str]:
    yield """<h2 id="top">Index</h2>"""
    yield "<ul>"
    for datum in metadata:
        yield f"<li><a href='#{datum['file']}'>{datum['title']}</a></li>"
    yield "</ul>"


def make_carol_html(datum: Metadatum) -> Iterator[str]:
    yield f"<h3 id='{datum['file']}'>{datum['title']}</h3>"
    yield "<p>"
    with open(f"carols/{datum['file']}") as fo:
        for line in fo.readlines():
            yield f"{line} <br/>"
    yield "</p>"
    yield "<br><i><a href='#top'>Back to top</a></i>"
    yield f"<br><br><i><a target='blank' href='{datum['source']}'>Source website</a></i><br/><br/>"

def make_carol_latex(datum: Metadatum) -> Iterator[str]:
    yield f"\\subsection{{{datum['title']}}}"
    yield f"\\label{{{datum['file']}}}\n"
    yield "\\begin{description}[nosep,leftmargin=\parindent,labelsep=0pt]\n"
    with open(f"carols/{datum['file']}") as fo:
        for line in fo.readlines():
            line = line.strip()
            if line:
                yield f"\\item {line.rstrip()} \n"
            else:
                yield "\\vspace{1.5ex}\n"
    yield "\\end{description}\n"


def write_gen(fo: TextIOWrapper, gen: Iterator[str]) -> None:
    for segment in gen:
        fo.write(segment)

def make_html(metadata: list[Metadatum]) -> None:
    with open("index.html", "w") as fo:
        fo.write(HEADER_HTML)
        write_gen(fo, make_index_html(metadata))
        for datum in metadata:
            if datum["file"] == "":
                continue
            write_gen(fo, make_carol_html(datum))
        fo.write(FOOTER_HTML)

def make_latex(metadata: list[Metadatum]) -> None:
    with open("latex/carols.tex", "w") as fo:
        for datum in metadata:
            if datum["file"] == "":
                continue
            write_gen(fo, make_carol_latex(datum))

def main() -> None:
    metadata = sorted(_metadata, key=lambda x: x["title"])
    metadata = [x for x in metadata if not x.get("exclude", False)]
    make_html(metadata)
    make_latex(metadata)


if __name__ == "__main__":
    main()
