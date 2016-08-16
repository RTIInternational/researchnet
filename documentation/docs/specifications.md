


## Application Architecture

To be as portable as possible, the entire Researchnet applicaiton stack has been "containerized" with Docker.  For more information on Docker containers, go [here](https://linuxcontainers.org/).  Currently there are three containers including the Python Django web application, the PostgresSQl database, and the NGINX proxy server.  As an option the database can be configure to run as a seperate service by overriding the database connection information in the Django settings.
 

The following diagram depicts a typical process flow.  Starting with the onboarding, the user initiates account creation, which ultimately results in a fully provisioned study participant. Once the study participant subsequently logs in, they receive a non-expiring token which is required for all further interactions including submitting survey responses and authorizing study consent.

![flow](images/flow.png )



## Data Model

Researchnet extends the Django User Model to support an entity called the 'Participant' which serves as the study participant.  See the [data model diagram](images/models.png) for more information.



## Deployment

Currently we are working towards a HIPAA compliant configuration on Amazon Web Services (AWS).



