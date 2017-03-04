from xbmc_videodb_xml import get_xml_root, get_movies, get_tvshows
from writers import write_to_md

xml_filename = r"/Users/lukasmaly/Desktop/videodb.xml"
md_filename = r"/Users/lukasmaly/Desktop/videodb.md"

root = get_xml_root(xml_filename)
movies = get_movies(root)
tvshows = get_tvshows(root)

write_to_md(md_filename, movies, tvshows)
