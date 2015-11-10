
Put brief description of the REST api here

# Enrollment

 |  | 
:----------- | :----------- 
__Description__         | Using this API call, you need only supply the survey identifier and createdOn timestamp, as well as an optional array of answers, in order to create a survey response object. You may either supply an identifier for this survey response (the identifier must be unique in the scope of an individual study participant), or else the survey will create an identifier for you. The identifier is returned in either case.
__Endpoint__         | /enrollment       
__Method__         | POST
__Response Codes__         | 200 - Sucessful<br/>403 - Request failed validation        

Request
```
{   
    "username":"participant@mycompany.com",
    "password":"aadfadfdf",
    "firstname": "Jane",
    "lastname": "Doe",
    "gender": "Female",
    "dob": "9/15/1985"
}

```


# Authenticate

|  | 
:----------- | :----------- 
__Description__         | This is used to create a session
__Endpoint__         | /authenticate/loginin 
Method         | GET       
__Authentication__         | Center        


Request
```
{   
    "username":"participant@mycompany.com",
    "password":"aadfadfdf"
}
```

# Consent

|  | 
:----------- | :----------- 
__Endpoint__         | /consent   
Method         | GET     
__Authentication__         | Center        
__Description__         | Using this API call, you need only supply the survey identifier and createdOn timestamp, as well as an optional array of answers, in order to create a survey response object. You may either supply an identifier for this survey response (the identifier must be unique in the scope of an individual study participant), or else the survey will create an identifier for you. The identifier is returned in either case.

Request
```
def fn():
 pass
```


# Survey Response

|  | 
:----------- | :----------- 
__Endpoint__         | /submission/  
Method         | PUT        
__Authentication__         | Center        
__Description__         | Using this API call, you need only supply the survey identifier and createdOn timestamp, as well as an optional array of answers, in order to create a survey response object. You may either supply an identifier for this survey response (the identifier must be unique in the scope of an individual study participant), or else the survey will create an identifier for you. The identifier is returned in either case.
Request
```
def fn():
 pass
```


