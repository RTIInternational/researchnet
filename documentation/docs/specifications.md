## Deployment Architecture

Containers include the application and all of its dependencies, but share the kernel with other containers. They run as an isolated process in userspace on the host operating system. They’re also not tied to any specific infrastructure – Docker containers run on any computer, on any infrastructure and in any cloud.  In our case here we maintain 3 linked containers, one for the web application and API with Python Django, one for the user database with Postgres SQL, and finally one for the survey response database with MongoDB.

![Screenshot](images/docker.png)
