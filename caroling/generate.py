metadata = [
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
    # {
    #     "file": "",
    #     "title": "",
    #     "source": "",
    # },
]

# <script type="text/javascript">setTimeout(() => window.location.reload(true), 3000);</script>
HEADER = """
<html>
<head>
</head>
<body>
    <h1 id="title">Brookline Carol Book</h1>
"""

FOOTER = """
</body>
</html>
"""


def make_index():
    yield """<h2 id="top">Index</h2>"""
    yield "<ul>"
    for datum in metadata:
        yield f"<li><a href='#{datum['file']}'>{datum['title']}</a></li>"
    yield "</ul>"


def make_carol(datum):
    yield f"<h3 id='{datum['file']}'>{datum['title']}</h3>"
    with open(f"carols/{datum['file']}") as fo:
        for line in fo.readlines():
            yield f"{line} <br/>"
    yield "<br><i><a href='#top'>Back to top</a></i>"
    yield "<br><br><i><a href='{datum['source']}'>Source website</a></i>"


def write_gen(fo, gen):
    for segment in gen:
        fo.write(segment)


def main():
    global metadata
    metadata = sorted(metadata, key=lambda x: x["title"])
    with open("index.html", "w") as fo:
        fo.write(HEADER)
        write_gen(fo, make_index())
        for datum in metadata:
            write_gen(fo, make_carol(datum))
        fo.write(FOOTER)


if __name__ == "__main__":
    main()
