#!/usr/bin/python
# this is a smith configuration file

# output folders use smith defaults and don't need to be set here

# set the version control system for srcdist
VCS = 'git'

# set the font name, version, licensing and description
APPNAME="AndikaMtihani"

DESC_SHORT = "Test font for UFO workflows"
DESC_LONG = """
Andika Mtihani is a Latin script font family for testing UFO-based workflows.
It is not intended to be generally useful as an installable font family, and
may change significantly without notice. It will always be experimental and
may not work as you expect!
"""
DESC_NAME = "AndikaMtihani"
DEBPKG = 'fonts-sil-andikamtihani'

getufoinfo('source/AndikaMtihani-Regular.ufo')

fontfamily=APPNAME
for dspace in ('Roman', 'Italic'):
    designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
                woff = woff()
    )
