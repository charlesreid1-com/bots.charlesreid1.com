# bots.charlesreid1.com

One-pager describing the charlesreid1 bot flocks.

## Repository Layout

Source branch: `master`

Live/pages branch: `gh-pages`

## Containerization

This repository contains the static content.

The containerized version is a lightweight web server.

Ideally, route traffic through krash, 
and bind http-only service to listen on mangement LAN.

The bot pod will run an nginx container
with a bot one-pager.

