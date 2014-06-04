Vimeo Search is a **demo application** for PyBossa that shows how you can
crowdsourcing a video classification/analysis problem.

This application uses the Vimeo web service as the source of the data. By
using Vimeo, we have the possibility of using its API to refine the searches,
and looking for specific tags, categories, groups, albums, channels, etc.

In this demo application, we use a very simple approach by getting 20 videos
tagged with the word "science".

The query provides information about the video like its link. This link is
used to load it and allows the user to play it with the usual Vimeo player.
Then we ask the users the following question: **Is this video showing a
scientific experiment?**

The application provides three simple answers as action buttons:

  * Yes
  * No and
  * I don't know

Based on the answer of the users, we will be able to classify the videos,
distributing the tasks (thanks to PyBossa) to different users and volunteers.

__ Note If you want to learn more about how to use this application as a
template, check the:

  * [source code](http://github.com/PyBossa/app-vimeo)
  * [the official documentation of PyBossa](http://docs.pybossa.com/) and 
  * [the step by step tutorial.](http://docs.pybossa.com/en/latest/user/tutorial.html)

* * *

