


## Application Architecture

In summary, the Researchnet backend application has been implemented in Pythion Django and utilizes Django User Authentication and Django Rest Framework (DRF) as core components with many of the popular JavaScript libraries on the front end including D3.js and foundation.js.     However, the main purpose of this backend is to provide a REST API.  More detail on the API can be found on the documentation site.  


![flow](images/flow.png )


## Deployment Architecture

Containers include the application and all of its dependencies, but share the kernel with other containers. They run as an isolated process in userspace on the host operating system. They’re also not tied to any specific infrastructure – Docker containers run on any computer, on any infrastructure and in any cloud.  In our case here we maintain 2 linked containers, one for the web application and API with Python Django, one for the user database with Postgres SQL.

![docker](images/docker.png )

## Data Model

Researchnet extends the Django User Model to support an entity called the 'Participant' which serves as the study participant.  See the [data model diagram](images/models.png) for more information.



## Deployment

Currently we certify a HIPPA compliant configuration with using Docker containers and support the following cloud service providers: Amazon Web Services (AWS), Digital Ocean, Microsoft Azure, and IBM Softlayer.



