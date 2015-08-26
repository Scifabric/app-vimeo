PyBossa demo project for Vimeo 
==============================

This project is an example about how you can do pattern recognition on
videos. The project uses the [Vimeo API](https://developer.vimeo.com/) to
get videos from channels, categories, tags, etc.

![alt screenshot](http://i.imgur.com/qSyO3fZ.png)

This project has three files:

*  project.json: a JSON file that describes the project.
*  long_description.md: a Markdown file with a long description of the project.
*  videos.py: for getting videos for the PyBossa project, and use them as tasks.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.


Testing the project
===================

You need to install the pybossa-pbs and the vimeo client libraries. Use of
a virtual environment is recommended:

```bash
    $ virtualenv env
    $ source env/bin/activate
```

```bash
    $ pip install -r requirements.txt
```

As this project uses Vimeo for getting the videos, you need to create an
application in the [Vimeo developers site](https://developer.vimeo.com/). Once
you have the developer keys, just copy and paste them into a file named
**config.py** (just copy the file **config.py.template** and rename it). Then, you 
can follow the next steps.

## Creating an account in a PyBossa server
Now that you've all the requirements installed in your system, you need
a PyBossa account:

*  Create an account in your PyBossa server (use [Crowdcrafting](https://crowdcrafting.org) if you want).
*  Copy your API-KEY (you can find it in your profile page).

## Configure pybossa-pbs command line

PyBossa-pbs command line tool can be configured with a config file in order to
avoid typing the API-KEY and the server every time you want to take an action
on your project. For this reason, we recommend you to actually create the
config file. For creating the file, follow the next steps:

```bash
    $ cd ~
    $ editorofyourchoice .pybossa.cfg
```

That will create a file. Now paste the following:

```ini
[default]
server: http://yourpybossaserver.com
apikey: yourapikey
``` 

Save the file, and you are done! From now on, pybossa-pbs will always use the
default section to run your commands.

## Create the project

Now that we've everything in place, creating the project is as simple as
running this command:

```bash
    $ pbs create_project
```

## Adding tasks

For adding the tasks you only have to run the videos.py script to create a JSON
file with the tasks in it. For example, to get videos tagged with the word:
*science* you can run:

```bash
    $ python videos.py --by-tag science
```

That command will create a file named *video_tasks_from_tags.json* with all the
videos.

**NOTE**: check the **--help** option to see all the posibilities of videos.py.

Now, that we have the tasks ready, we only have to add them to our project:

```bash
    $ pbs add_tasks --tasks-file=video_tasks_from_tags.json
```
Done!

## Finally, add the task presenter, tutorial and long description

Now that we've some data to process, let's add to our project the required
templates to show a better description of our project, to present the tasks to
our users, and a small tutorial for the volunteers:

```bash
    $ pbs update_project
```

Done! Now you can do video pattern recognition problems in the PyBossa server.

**NOTE**: we provide templates also for Bootstrap v2 in case your PyBossa
server is using Bootstrap 2 instead of Bootstrap 3. See the rest of the files.



Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This application uses the [pybossa-pbs](https://pypi.python.org/pypi/pybossa-pbs) library in order to simplify the development of the project and its usage. Check the [documentation](http://docs.pybossa.com/en/latest/user/pbs.html).


LICENSE
=======

Please, see the COPYING file.


Acknowledgments
===============
Special thanks to Ali Sajjadi and Craig Protzel for their help developing the
app.

