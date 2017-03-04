import xml.etree.ElementTree as ET
from videos import Movie
from videos import TVShow


def get_xml_root(filename):
    """Return the root element of XML document's element tree."""
    tree = ET.parse(filename)  # parse XML document into element tree
    root = tree.getroot()  # returns the root element for this tree
    return root


def get_movies(root):
    """Return the list of Movie objects."""
    movies = []  # list of Movies
    for movie in root.findall('movie'):  # finds all matching subelements
        title = movie.find('title').text
        year = movie.find('year').text
        movies.append(Movie(title, year))
    movies.sort(key=lambda x: x.title)  # sort by title
    return movies


def get_tvshows(root):
    """Return the list of TVShows objects."""
    tvshows = []  # list of TVShows
    for tvshow in root.findall('tvshow'):
        title = tvshow.find('title').text
        year = tvshow.find('year').text
        seasons = []
        for episode in tvshow.iter('episodedetails'):  # creates a tree iterator
            if int(episode.find('season').text) not in seasons:
                seasons.append(int(episode.find('season').text))
            seasons.sort()
        tvshows.append(TVShow(title, year, seasons))
    tvshows.sort(key=lambda x: x.title)  # sort by title
    return tvshows
