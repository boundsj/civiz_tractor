What is this?
-------------
Real time tweet vizualation for several major urban areas. It is a bit contrived in that instead of doing everything in say, node.js, it uses several python processes to capture streaming tweets for geobounded areas and passes those tweets via redis pub/sub to a node.js process that, in turn, pushes them to connected browsers. As such, it is an interesting, non-trivial application to attempt to run on a platform service like Heroku (for which instructions are supplied below) 

Installation Instructions
-------------------------
These instructions assume that you have got git (and GitHub), Python, [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/), [Redis](http://redis.io/), [NPM](http://npmjs.org/), and [Node](http://nodejs.org/) installed. Install them on your development environment if you have not done so already before continuing.

For reference, this applications works and was tested with the following software versions:
Python 2.7
:

For hosting on Heroku (described later), please check the Heroku website for instructions related to setting up an account and installing the development tools on your machine.

First, using virtualenvwrapper, create a working directory with mkvirtualenv and cdvirtualenv into it. Then, clone this repo:

    $ git@github.com:boundsj/civiz.git
    $ cd civiz

Civiz uses the tweetstreamwrapper submodule to handle pushing tweets from the python process that captures them to a node.js process via redis. Install and load the submodule now:

    $ git submodule init
    $ git submodule update

TODO: set up environment variables in .env file TWITTER USER & PASS, REDIS

Running Locally
---------------


Deploy to Heroku
----------------
heroku create -s cedar YOUR_APP_NAME
heroku addons:add redistogo:nano
heroku plugins:install git://github.com/ddollar/heroku-config.git
heroku config:add TWITTER_USER=YOUR_TWITTER_USER_NAME
heroku config:add TWITTER_PASSWORD=YOUR_TWITTER_USER_NAME

