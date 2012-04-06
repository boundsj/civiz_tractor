What is this?
-------------
This is a python application that uses [tweetstreamwrapper](https://github.com/boundsj/tweetstreamwrapper) to capture geobounded tweets and push them to a [redis pub/sub](http://redis.io/topics/pubsub). From there, they can be picked up and used by any application that can subscribe to the redis pub/sub instance (i.e. [civis_server](https://github.com/boundsj/civiz_server)). 

Installation Instructions
-------------------------
These instructions assume that you have got git (and GitHub), Python, [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/), [Redis](http://redis.io/), the [foreman Ruby gem](http://rubygems.org/gems/foreman), and the [heroku Ruby gem](http://devcenter.heroku.com/articles/using-the-cli) (if you want to run the app on heroku and not just locally). Install them on your development environment if you have not done so already before continuing. If you are on a Mac, you should be able to use [Homebrew](http://mxcl.github.com/homebrew/) to install almost everything you need. Ubuntu users can use [apt-get](https://help.ubuntu.com/8.04/serverguide/C/apt-get.html). For reference, this applications works and was tested with the following software versions:
Python 2.7
redis-2.4.9

First, using virtualenvwrapper, create a working directory with mkvirtualenv and cdvirtualenv into it. Then, clone this repo:

    $ git clone https://github.com/boundsj/civiz_tractor 
    $ cd civiz_tractor

This application uses the tweetstreamwrapper submodule to handle pushing tweets from the python process that captures them into redis. Install and load the submodule now:

    $ git submodule init
    $ git submodule update

Environment variables are used to store twitter and redis connection details. To make env variables available for your local testing, create a file called .env and add the following lines:
    $ TWITTER_USER=your_twitter_id
    $ TWITTER_PASSWORD=your_twitter_password
    $ REDISTOGO_URL=redis://localhost:6379

Finally, install the python library requirements by issuing the command:

    $ pip install -r requirements.txt

Running Locally
---------------
Assuming all requisite packages installed fine and your environment is set up as described above, you should be able to run the application now. Before we run the python script though, make sure that redis is running on your local environment. If you installed redis with brew on a Mac, you should be able to start it by using:

    $ redis-server /usr/local/etc/redis.conf

Note that this will start redis in the foreground in your shell so run it as a background process or switch to a new shell (remember to run virtualenvwrapper workon command to activate your environment if you do). 

Now, start the python program by running:

    $ foreman start

Note that we use foreman (and the Procfile) to run the Python program because it effortlessly picks up the environment variables we stored in the .env file. This pattern matches the way heroku handles environment variables and sets us up nicely to deploy to heroku.

Deploy to Heroku
----------------
heroku create -s cedar YOUR_APP_NAME
heroku addons:add redistogo:nano
heroku plugins:install git://github.com/ddollar/heroku-config.git
heroku config:add TWITTER_USER=YOUR_TWITTER_USER_NAME
heroku config:add TWITTER_PASSWORD=YOUR_TWITTER_USER_NAME

