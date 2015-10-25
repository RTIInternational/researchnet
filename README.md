A ResearchKit Backed
=====================


This document describes the requirement allowing to easily run the components for the RTI ResearchNET server using [docker](https://www.docker.com/) containers.

Prerequisites
-------------

* [install Docker Compose](https://docs.docker.com/compose/ "Documentation") 

Getting Started
----------------
Type this `docker-compose up` to start the docker containers.  Your application will be available via docker IP address on port 8000.  If you want to run this outside of docker, just make sure that you have an entry in your /etc/hosts for `db` that points to your postgressql database and `mongo` to your mongo database.  When you have all of that set up you can run `python manage.py runserver_plus 0.0.0.0:8000 --settings=config.settings.local`

PRO TIP: Because python is running as a container, anytime you install a module you will have to rebuild the container, which you can do like this: `docker-compose build`.


Documentation
----------------
We use MkDocs for our documentation.  Just go to the documentation folder and run `mkdocs serve`

Front-end assets
----------------

Front-end assets are managed by [Bower](http://bower.io). You have to run this in order to make the dashboard work `python manage.py bower install`


Bugs, new requests or contribution
--------------
Please submit bugs, gripes and feature requests at https://bitbucket.org/rcdrti/researchnet/issues

Any other questions contact Adam Preston at apreston@rti.org or on Twitter here @adam704a 

![research_sm.png](https://bitbucket.org/repo/B6bG6n/images/661596335-research_sm.png)

