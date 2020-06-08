#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown

AUTHOR = u'charlesreid1'
SITENAME = u'charlesreid1 bots'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

# bots use nginx green
INTROCOLOR  = "#fff"
ACOLOR      = "#aced00"
AHOVERCOLOR = "#84b400"
BRIGHTCOLOR = "#caf1d"

INTROBKG='theme/img/intro-bg-garage.jpg'
LINKSBKG='theme/img/links-bg-gears.jpg'

# note: custom.css is a template 
# that is defined in the THEME!
# it uses the above colors to 
# decorate the one-pager.
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

# img/ should be in content/
# it will finally end up 
# at the path <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "bots.charlesreid1.com"
SITE_DESCRIPTION = "a subdomain for charlesreid1 bots"
GITEA_URL = "https://github.com/charlesreid1-com/bots.charlesreid1.com"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about bots.charlesreid1.com"

ABOUT_TEXT = """
[charlesreid1-bots github organization](https://github.com/charlesreid1-bots)

<br />

**What is a bot?**

Broadly, a bot is an autonomous entity that executes a program.

The bots on this site are mostly Twitter bot flocks.

<br />

**What is a bot flock?**

A bot flock is a group of Twitter bots that perform a related task,
access related data, or otherwise share some structure.

See below for examples of Twitter bot flocks.

<br />

**Where can I find the bots?**

Each bot has a home page on bots.charlesreid1.com; 
see below for links.
"""


ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)



# ---


def make_links_description():
    descr = ""

    botlinks = {
        'twitter' : {
            'Apollo Space Junk Bot Flock - twitter list' : 'https://twitter.com/i/lists/1267145550496858113',
            'Paradise Lost Bot Flock - twitter list' :     'https://twitter.com/i/lists/1267145777006034944',
            'Ginsberg Bot Flock - twitter list' :          'https://twitter.com/i/lists/1267146364191817730',
        },
        'charlesreid1.com': {
            'Apollo Space Junk Bot Flock - apollo.charlesreid1.com' : 'https://apollo.charlesreid1.com/',
            'Ginsberg Bot Flock - ginsberg.charlesreid1.com' : 'https://ginsberg.charlesreid1.com/',
            'Milton Bot Flock - milton.charlesreid1.com' : 'https://milton.charlesreid1.com/',
        },
        'github.com' : {
            'Apollo Space Junk Bot Flock on Github' : 'https://github.com/charlesreid1-bots/apollo-space-junk',
            'Ginsberg Bot Flock on Github' : 'https://github.com/charlsreid1-bots/ginsberg-bot-flock',
            'Milton Bot Flock on Github' : 'https://github.com/charlsreid1-bots/milton-bot-flock'
        },
    }

    fa_icons = {
            'twitter' : '<i class="fa fa-twitter fa-fw"></i>',
            'charlesreid1.com': '<i class="fa fa-code-fork fa-fw"></i>',
            'github.com' : '<i class="fa fa-github-square fa-fw"></i>',
    }

    for key in botlinks.keys():
        descr += "<h3>charlesreid1 bots on %s:<h3>\n\n"%(key)
        fa_icon = fa_icons[key]

        links = botlinks[key]
        for bot_name in links.keys():
            bot_link = links[bot_name]
            descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(bot_link)
            descr += "%s %s"%(fa_icon, bot_name)
            descr += "</a></p>\n"
        
        descr += "\n"

    return descr

LINKS_SHORT = "Links"

LINKS_TITLE = "bot links"

LINKS_DESCRIPTION = make_links_description()


# ---


CONTACT_SHORT = "Contact"

CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>Get in touch!</p>
<p><a href="mailto:charles@charlesreid1.com">charles (at) charlesreid1.com</a></p>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
