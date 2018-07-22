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
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about bots.charlesreid1.com"

ABOUT_TEXT = """
[bots on git.charlesreid1.com](https://git.charlesreid1.com/bots)

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
            'pages.charlesreid1.com' : {
                'Rainbow Mind Machine' :        'https://pages.charlesreid1.com/rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://pages.charlesreid1.com/apollo',
                'Paradise Lost Bot Flock' :     'https://pages.charlesreid1.com/milton',
                'Ginsberg Bot Flock' :          'https://pages.charlesreid1.com/ginsberg',
                'Math Tripos Bot' :             'https://pages.charlesreid1.com/tripos'
            },

            'twitter' : {
                'Apollo Space Junk Bot Flock' : 'https://twitter.com/charlesreid1/lists/space-junk-botflock',
                'Paradise Lost Bot Flock' :     'https://twitter.com/charlesreid1/lists/miltonbotflock',
                'Ginsberg Bot Flock' :          'https://twitter.com/charlesreid1/lists/ginsbergbotflock',
                'Math Tripos Bot' :             'https://twitter.com/math_tripos'
            },

            'git.charlesreid1.com (source)' : {
                'Rainbow Mind Machine' :        'https://git.charlesreid1.com/bots/b-rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://git.charlesreid1.com/bots/b-apollo',
                'Paradise Lost Bot Flock' :     'https://git.charlesreid1.com/bots/b-milton',
                'Ginsberg Bot Flock' :          'https://git.charlesreid1.com/bots/b-ginsberg',
                'Math Tripos Bot' :             'https://git.charlesreid1.com/bots/b-tripos'
            },

            'github (source)' : {
                'Rainbow Mind Machine' :        'https://github.com/charlesreid1/rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://github.com/charlesreid1/apollospacejunk',
                'Paradise Lost Bot Flock' :     'https://github.com/charlesreid1/milton',
                'Ginsberg Bot Flock' :          'https://github.com/charlesreid1/ginsberg',
                'Math Tripos Bot' :             'https://github.com/charlesreid1/tripos-bot'
            },

            #'github pages' : {
            #    'Rainbow Mind Machine' :        'https://charlesreid1.github.io/rainbow-mind-machine',
            #    'Apollo Space Junk Bot Flock' : 'https://charlesreid1.github.io/apollospacejunk',
            #    'Paradise Lost Bot Flock' :     'https://charlesreid1.github.io/milton',
            #    'Ginsberg Bot Flock' :          'https://charlesreid1.github.io/ginsberg',
            #    'Math Tripos Bot' :             'https://charlesreid1.github.io/tripos-bot'
            #}

    }

    fa_icons = {
            'twitter' : '<i class="fa fa-twitter fa-fw"></i>',
            'git.charlesreid1.com (source)' : '<i class="fa fa-code-fork fa-fw"></i>',
            'pages.charlesreid1.com' : '<i class="fa fa-file-o fa-fw"></i>',
            'github (source)' : '<i class="fa fa-github fa-fw"></i>',
            'github pages' : '<i class="fa fa-github-square fa-fw"></i>'
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
