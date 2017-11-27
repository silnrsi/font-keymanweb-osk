#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file

# set the default output folders
out = "results"
DOCDIR = ["documentation", "web"]
OUTDIR = "installers"
ZIPDIR = "releases"
TESTDIR = "tests"
TESTRESULTSDIR = 'results/tests'
STANDARDS = 'tests/reference'

# set the version control system
VCS = 'git'

# set the font name, version, licensing and description
APPNAME = 'KeymanwebOsk'
FILENAMEBASE = 'KeymanwebOsk'
VERSION = '1.951'
TTF_VERSION = '1.951'
BUILDLABEL = ""
COPYRIGHT = "Copyright (c) 2013-2017 SIL International (http://www.sil.org) with Reserved Font Names 'Keyman' and 'SIL."
LICENSE = "OFL.txt"
RESERVEDOFL = "KeymanwebOsk"

DESC_SHORT = "Keyman Web Onscreen Keyboard"
DESC_LONG = """
KeymanWeb-OSK is a font used for interface elements of KeymanWeb and
Keyman's mobile software. (http://keyman.com/)
"""

# packaging
DESC_NAME = "KeymanwebOsk"
DEBPKG = 'fonts-sil-keymanweb-osk'

font(target='keymanweb-osk.ttf',
     source=create('keymanweb-osk-src.ttf', cmd('psfufo2ttf ${SRC} ${TGT}', ['source/KeymanwebOsk.ufo'])),
     version=VERSION,
     #license=ofl('Sevda'),
     #opentype=fea('source/' + fname + '.ufo/' + 'features.fea', no_make=1)
     )
