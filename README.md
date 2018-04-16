# bots.charlesreid1.com

Static site for pointing the way to bot flocks
and other bot content.

This page uses the single-page single-color Pelican theme [scurvy knave](https://git.charlesreid1.com/charlesreid1/scurvy-knave-theme) for rapid templating and deployment.

scurvy knave inserts bits of html into a single-page HTML template. The bits of html are generated with Python in `pelicanconf.py`.

## Required Software

To install Pelican:

```
pip install Markdown
pip install pelican
```

## Make Site

To make the Pelican site:

```
pelican content
cd output/
python -m http.server 8080
```

then visit `localhost:8080` in your browser.

If you are running Python 2, you should run `python -m SimpleHTTPServer 8080`

But _really_ you should run `alias python='python3'`

## Modify Content

The single-site template utilizes variables defined in `pelicanconf.py` 
to customize the page content, so there is no content to edit in `content/`.

## Set Up Push to Github Pages

Start by cloning a copy of the repo at output (a repo within a repo):

```
git clone https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com output/
cd output/
git checkout --orphan gh-pages
cd ../
```

Now make the content, which will put the resulting pages into `output/`,
and commit the new version of the site to the `gh-pages` branch:

```
pelican content
cd output/
git add -A .
git commit -a -m 'Add new version of site'
git push origin gh-pages
```



