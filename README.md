PyBossa demo project for Vimeo 
==============================

This project is an example about how you can do pattern recognition on
videos. The project uses the [Vimeo API](https://developer.vimeo.com/) to
get videos from channels, categories, tags, etc.

![alt screenshot](http://i.imgur.com/qSyO3fZ.png)

This project has three files:

*  videos.py: for getting videos for the PyBossa project, and use them as tasks.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.


Testing the project
===================

You need to install the pybossa-pbs and vimeo first (use a virtualenv):

```bash
    $ pip install -r requirements.txt
```

As this project uses Vimeo for getting the videos, you need to create an
application in the [Vimeo developers site](https://developer.vimeo.com/). Once
you have the developer keys, just copy and paste them into a file named
**config.py** (just copy the file **config.py.template** and rename it). Then, you 
can follow the next steps:

*  Create an account in PyBossa
*  Copy under your account profile your API-KEY

Then you can create the project:

```bash
    $ pbs --server server --apikey yourkey create_project
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
    $ pbs add_tasks --tasks-file=video_tasks_from_tags.json --tasks-type=json
```
Done!


Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This application uses the [pybossa-pbs](https://pypi.python.org/pypi/pybossa-pbs) in order to simplify the development of the project and its usage. Check the [documentation](http://docs.pybossa.com/en/latest/user/pbs.html).


LICENSE
=======

Please, see the COPYING file.


Acknowledgments
===============
Special thanks to Ali Sajjadi and Craig Protzel for their help developing the
app.

