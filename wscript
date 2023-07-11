#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

APPNAME = 'KeymanwebOsk'
DESC_SHORT = "Keyman Web Onscreen Keyboard"
DEBPKG = 'fonts-sil-keymanweb-osk'

getufoinfo('source/KeymanwebOsk-Regular.ufo')

fontfamily=APPNAME

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
)
