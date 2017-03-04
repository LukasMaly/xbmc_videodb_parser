from videodb_xml import get_xml_root, get_movies, get_tvshows
from writers import write_to_md


def parse_to_md(xml_filename, md_filename):
    """Parse XML to Markdown."""
    root = get_xml_root(xml_filename)
    movies = get_movies(root)
    tvshows = get_tvshows(root)
    write_to_md(md_filename, movies, tvshows)
