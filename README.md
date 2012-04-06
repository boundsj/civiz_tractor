What is this?
-------------
This is a python application that uses [tweetstreamwrapper](https://github.com/boundsj/tweetstreamwrapper) to capture geobounded tweets and push them to a [redis pub/sub](http://redis.io/topics/pubsub). From there, they can be picked up and used by any application that can subscribe to the redis pub/sub instance (i.e. [civis_server](https://github.com/boundsj/civiz_server)). 

Installation Instructions
-------------------------
These instructions assume that you have a twitter account, git (and GitHub), Python, [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/), [Redis](http://redis.io/), the [foreman Ruby gem](http://rubygems.org/gems/foreman), and the [heroku Ruby gem](http://devcenter.heroku.com/articles/using-the-cli) (if you want to run the app on heroku and not just locally). Install them on your development environment if you have not done so already before continuing. If you are on a Mac, you should be able to use [Homebrew](http://mxcl.github.com/homebrew/) to install almost everything you need. Ubuntu users can use [apt-get](https://help.ubuntu.com/8.04/serverguide/C/apt-get.html). For reference, this applications works and was tested with the following software versions:
Python 2.7
redis-2.4.9

First, using virtualenvwrapper, create a working directory with mkvirtualenv and cdvirtualenv into it. Then, clone this repo:

    $ git clone https://github.com/boundsj/civiz_tractor 
    $ cd civiz_tractor

This application uses the tweetstreamwrapper submodule to handle pushing tweets from the python process that captures them into redis. Install and load the submodule now:

    $ git submodule init
    $ git submodule update

Environment variables are used to store twitter and redis connection details. To make env variables available for your local testing, create a file called .env and add the following lines:

    TWITTER_USER=your_twitter_id
    TWITTER_PASSWORD=your_twitter_password
    REDISTOGO_URL=redis://localhost:6379

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

At this point, your process should be running as a foreman job. It's probably catching tweets! You can confirm this by opening a new shell, starting a redis client and subscribing to the channel - like this:

    $ redis-cli
    $ subscribe tweets

Wait patiently and you should see tweets scroll by eventually. If so, it's working!

Deploy to Heroku
----------------
If you haven't [signed up for Heroku](https://api.heroku.com/signup), go
ahead and do that. You should then be able to [add your SSH key to
Heroku](http://devcenter.heroku.com/articles/quickstart), and also
`heroku login` from the commandline.

Now, to upload your application, you'll first need to do the
following -- and obviously change `app_name` to the name of your
application:

    $ heroku create app_name -s cedar

Before we can start the app, we need to take care of some administrative items.
First, add redistogo to your account (note that even though you will be adding
the free version of redistogo, it will still require you to give heroku a 
credit card - don't worry though, you won't actually have to pay a dime). So, go 
ahead and tell heroku that you want redistogo:nano:

    $ heroku addons:add redistogo:nano

Also, we need to tell redis about our custom env variables for our twitter user
and pass. To do this, you will need to make sure you install the heroku-config
plugin:

    $ heroku plugins:install git://github.com/ddollar/heroku-config.git

With this plugin installed, you can set the env variables as required:

    $ heroku config:add TWITTER_USER=YOUR_TWITTER_USER_NAME
    $ heroku config:add TWITTER_PASSWORD=YOUR_TWITTER_USER_NAME

You don't have to worry about adding the REDISTOGO_URL env variable like we have
in our local .env file because heroku will set that one up for us.

Now you can push your application up to Heroku.

    $ git push heroku master
    $ heroku scale worker=1

Finally, we can make sure the application is up and running.

    $ heroku ps

Now, we can also view the application logs.

    $ heroku logs 
