
This is the core API for to be used primarily within a mobile client.




# Enrollment

 |  | 
:----------- | :----------- 
__Description__         | Using this API call, you need to supply the required fields for enrolling a user, which is usually what you see below
__Endpoint__         | /enrollment       
__Method__         | POST
__Response Codes__         | 200 - Sucessful<br/>403 - Request failed validation        

Request Object
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
__Description__         | This is used to create a session.  The session token will be required for operations for an authenticated user.
__Endpoint__         | /authenticate/loginin 
__Method__        | GET       
__Response Codes__          | 200 - Sucessful<br/>403 - Invalid Credentials


Request Object
```
{   
    "username":"participant@mycompany.com",
    "password":"aadfadfdf"
}
```

# Consent

|  | 
:----------- | :----------- 
__Description__         | This API establishes user consent to use submitted data within a scope (to be defined by study)
__Endpoint__         | /consent   
__Method__         | POST           
__Response Codes__          | 200 - Sucessful<br/>403 - Invalid Credentials

Request Object
```
{   
    "userid":"participant@mycompany.com",
    "imageData":"aadfadfdfadfadfafasdfas", // signature image
    "scope": "no_sharing"
}
```


# Survey Response

|  | 
:----------- | :----------- 
__Endpoint__         | /submission/  
Method         | PUT        
__Authentication__         | Center        
__Description__         | Using this API call, as well as an optional array of answers.

Request Object
```
{   
    "userid": 12222,
    "time_start": "2015-12-17T18:52:49.963458Z",
    "time_complete": "2015-12-17T18:52:49.963458Z",
    "device_id": "ADAMS_ANDROID",
    "response": {
    	"mood": "pretty good",
    	"wake_up_time": "7:10:00am"
	}

    
}
```


