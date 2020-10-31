from lxml import etree


class Dataparser:
    def __init__(self, data):
        self.data = data
        self.song_verses = None
        self.title = "Untitled Song"
        self.author = "Unknown"
        self.validate_data()
        self.__generate_xml()

    def validate_data(self):
        comments = self.data[0]
        if '#' in comments:
            self.song_verses = self.data[1:]
            self.parse_comments(comments)
        else:
            self.song_verses = self.data

    def parse_comments(self, data):
        lines = data.split("\n")
        for comment in lines:
            attribute, value = comment.lstrip('#').split(':')
            if attribute.strip().lower() in ("titles", "title"):
                self.title = value.strip()
            elif attribute.strip().lower() in ("author", "authors"):
                self.author = value.strip()

    def __generate_xml(self):
        txt_parser = TxtParser(self.song_verses, self.title, self.author)
        txt_parser.parse()


class TxtParser:
    def __init__(self, song_verses, title, author):
        self.song_verses = song_verses
        self.verse_map = {}
        self.song_tag = None
        self.doc = None
        self.properties = None
        self.title = title
        self.author = author

    def parse(self):
        self.construct_verse_map()
        self.construct_metadata()
        self.construct_properties()
        self.construct_lyrics()
        self.save_xml()

    def construct_verse_map(self):
        self.verse_map = {f"v{v}": verse for v, verse in zip(range(1, len(self.song_verses) + 1), self.song_verses)}

    def construct_metadata(self):
        self.song_tag = etree.Element('song', xmlns="http://openlyrics.info/namespace/2009/song", version="0.9")
        self.doc = etree.ElementTree(self.song_tag)

    def construct_properties(self):
        self.properties = etree.SubElement(self.song_tag, "properties")
        titles = etree.SubElement(self.properties, "titles")
        etree.SubElement(titles, "title").text = self.title
        authors = etree.SubElement(self.properties, "authors")
        etree.SubElement(authors, "author").text = self.author

    def construct_lyrics(self):
        lyrics = etree.SubElement(self.song_tag, "lyrics")
        for verse_key, lines in self.verse_map.items():
            verse = etree.SubElement(lyrics, "verse", name=verse_key)
            for line in lines.split("\n"):
                etree.SubElement(verse, "lines").text = line

    def save_xml(self):
        self.doc.write(f'{self.title}.xml', xml_declaration=True, encoding='utf-16')

