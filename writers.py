def write_to_md(filename, movies, tvshows):
    f = open(filename, 'w')
    if movies:
        f.write('# Movies\n')
        for m in movies:
            f.write('- **{0}** ({1})\n'.format(m.title, m.year))
        f.write('\n')
    if tvshows:
        f.write('# TV Shows\n')
        for t in tvshows:
            f.write('- **{0}** ({1}) {2}\n'.format(t.title, t.year, t.seasons))
    f.close()
