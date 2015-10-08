A ResearchKit Backed
=====================


This document describes the requirement allowing to easily run the components for the RTI ResearchNET server using [docker](https://www.docker.com/) containers.

Prerequisites
-------------

* [install Docker Compose](https://docs.docker.com/compose/ "Documentation") 

Getting Started
----------------
`docker-compose up` to start the docker containers.  Your application will be available.  If you want to run this outside of docker, just make sure that you have an entry for `db` that points to your postgressql database and `mongo` to your mongo database.

Front-end assets
----------------

Front-end assets are managed by [Bower](http://bower.io). You have to run this in order to make the dashboard work `python manage.py bower install`


Bugs, new requests or contribution
--------------
Please submit bugs, gripes and feature requests at https://bitbucket.org/adam704a/researchnet/issues

Any other questions contact Adam Preston on Twitter at @adam704a, email at apreston@rti.org