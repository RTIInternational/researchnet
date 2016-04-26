

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
__Description__         | Get all study participants.
__Endpoint__         | /participant/       
__Method__         | GET
__Authentication__         | Token  
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request   

Response Object
```
[
{
    "username": "testuser1",
    "first_name": "Sue",
    "last_name": "Jones",
    "email": "fakeemail@rti.org",
    "gender": "Female",
    "dob": "1979-12-19"
  },
  {
    "username": "testuser2",
    "first_name": "Jessie",
    "last_name": "Thomas",
    "email": "fakeemail@rti.org",
    "gender": "Female",
    "dob": "1979-10-06"
  }
  ...
]

```

|  | 
:----------- | :----------- 
__Description__         | Enroll a study participant.
__Endpoint__         | /participant/       
__Method__         | POST
__Authentication__         | None  
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request<br/>403 - Forbidden   

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
__Description__         | Establishes user consent to use submitted data within a scope (to be defined by study)
__Endpoint__         | /consent/   
__Method__         | POST, PUT 
__Authentication__         | Token          
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request

Request Object
```
{   
    "imageData":"aadfadfdfadfadfafasdfas", // signature image
    "scope": "no_sharing"
}
```



# Survey Response

|  | 
:----------- | :----------- 
__Description__         | Submit a survey response.
__Endpoint__         | /submission/  
__Method__         | POST       
__Authentication__         | Token        
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request


Request Object
```
{   

    "time_start": "2015-12-17T18:52:49.963458Z",
    "time_complete": "2015-12-17T18:52:49.963458Z",
    "device_id": "ED2B101F-CC55-46FF-BEE5-60CC32EEC6C9",
    "lat": "40.5895466",
    "long": "-105.0751243",
    "response": {
    	"mood category": "fine",
        "mood scale": "8",
        "mood image": "3"
	}
 
}
```




_If you are feeling adventurous, try running this in [Postman](https://app.getpostman.com/run-collection/6241de2d723c0c4b8780)._



