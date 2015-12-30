
# Token Authenticate

|  | 
:----------- | :----------- 
__Description__         | A mechanism for clients to obtain a token given a username and password.
__Endpoint__         | /api-token-auth/
__Method__        | POST  
__Authentication__         | None       
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request        

Request Object
```
{   
    "username":"participant",
    "password":"aadfadfdf"
}
```

Response Object
```
{
    "token": "ffc0479b0021eed19271d51a803558e7d10ff286"
}
```


# Enrollment

 |  | 
:----------- | :----------- 
__Description__         | Using this API call, you need to supply the required fields for enrolling a study participant.
__Endpoint__         | /participant/       
__Method__         | POST
__Authentication__         | Token  
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request        

Request Object
```
{   
    "username":"joeschmoe",
    "password":"secretpassword",
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "joe@gmail.com",
    "gender": "Male",
    "dob": "9/15/1985"
}

```



# Consent

|  | 
:----------- | :----------- 
__Description__         | This API establishes user consent to use submitted data within a scope (to be defined by study)
__Endpoint__         | /consent/   
__Method__         | POST, PUT 
__Authentication__         | Token          
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request

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
__Description__         | Using this API call, as well as an optional array of answers.
__Endpoint__         | /submission/  
Method         | POST       
__Authentication__         | Token        
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request


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


