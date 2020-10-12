#!/usr/bin/pythons
# encoding: utf-8
# this is a smith configuration file

APPNAME = 'KeymanwebOsk'
DESC_SHORT = "Keyman Web Onscreen Keyboard"
DEBPKG = 'fonts-sil-keymanweb-osk'

getufoinfo('source/KeymanwebOsk-Regular.ufo')

fontfamily=APPNAME

font(target='keymanweb-osk.ttf',
     source=create('keymanweb-osk-src.ttf', cmd('psfufo2ttf ${SRC} ${TGT}', ['source/KeymanwebOsk-Regular.ufo'])),
     version=VERSION,
     )

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
)
