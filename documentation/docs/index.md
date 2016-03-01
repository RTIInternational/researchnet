
## Overview

![research](images/research.png )
Apple launched its ResearchKit framework for iOS on March 9, 2015. This open source software framework was designed to aid in the creation of mobile apps for biomedical and health research. ResearchKit simplifies construction of highly functional apps by providing support for various app modules, including informed consent, passive data collection, active tasks, surveys and data dashboards. 

Apple iOS currently controls a little over 43% of the US smartphone market, providing access to more than 79 million iPhone users in the US. The ResearchKit platform immediately garnered a great deal of interest within the biomedical research community.   
 
As exciting as this new framework is Apple provided no guidance on how the data collected was to be stored and managed.  This is where the Biomedical Data as a Service Internal Research and Development (IR&D) project comes in.  Designed and implmented by the Research Computing Division, this solution includes the following basic components: an iOS code library, a cloud-based data host, a service layer implementing data exchange application programming interfaces, and a dashboard UI for management.  Instrument developers simply include the iOS library in their IOS application code to connect to the data service via the REST based web API.  Study managers manage their datasets and perform exploratory analytics via the dashboard UI. The system design and implementation incorporates US legal and regulatory compliance with respect to data privacy and security. 



