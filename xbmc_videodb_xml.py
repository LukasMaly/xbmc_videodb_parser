import xml.etree.ElementTree as ET


def load_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for movie in root.findall('movie'):
        title = movie.find('title').text
        year = movie.find('year').text
        print(title, year)
    for tvshow in root.findall('tvshow'):
        title = tvshow.find('title').text
        year = tvshow.find('year').text
        print(title, year)
