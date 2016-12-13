![ResearchNet](researchnet/config/staticfiles/researchnet.png)


This document describes the process for running the Researchnet server using [docker](https://www.docker.com/) containers.

Prerequisites
-------------

* [install Docker Compose](https://docs.docker.com/compose/ "Documentation")


Getting Started
----------------
Type this `docker-compose up` to start the docker containers.  Your application will be available via docker IP address on port 8000.  If you want to run this outside of docker, just make sure that you have an entry in your /etc/hosts for `db` that points to your postgressql database .  When you have all of that set up you can run `python manage.py runserver_plus 0.0.0.0:8000 --settings=config.settings.local`.    

We're using Django Authention, which means in order to login you'll need to run 'docker-compose run web researchnet/manage.py migrate' and after that 'docker-compose run web researchnet/manage.py createsuperuser'

_PRO TIP_: Because python is running as a container, anytime you install a module you will have to rebuild the container, which you can do like this: `docker-compose build --no-cache`.


Documentation
----------------
We use MkDocs for our documentation.  Just go to the documentation folder and run `mkdocs serve`.  After you do this you can get to the documentation for this project locally here: 'http://127.0.0.1:8000' 


Front-end assets
----------------

Front-end assets are managed by [Bower](http://bower.io). You have to run this `python manage.py bower install`, then `python manage.py collectstatic` in order to make the dashboard work.


Bugs, new requests or contribution
--------------
Please submit bugs, gripes, and feature requests as an issue.



