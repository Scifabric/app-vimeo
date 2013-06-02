PyBossa demo application Vimeo 

This application has three files:

*  createTasks.py: for creating the application in PyBossa, and fill it with some tasks.
*  template.html: the view for every task and deal with the data of the answers.

Testing the application
=======================

You need to install the pybossa-client and vimeo first (use a virtualenv):

```bash
    $ pip install pybossa-client
    $ pip install vimeo
```
Then, you can follow the next steps:

*  Create an account in PyBossa
*  Copy under your account profile your API-KEY
*  Run python createTasks.py -u http://crowdcrafting.org -k API-KEY
*  Open with your browser the Applications section and choose the FlickrPerson app. This will open the presenter for this demo application.

Please, check the full documentation here for a tutorial:

http://docs.pybossa.com/en/latest/user/create-application-tutorial.html
