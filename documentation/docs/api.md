

# Token Authenticate

|  | 
:----------- | :----------- 
__Description__         | Obtain a token given a username and password. Subsequently, this token is used to authenticate all requests using the following authorization HTTP header `Authorization: Token [TOKEN_ID]`
__Endpoint__         | /api-token-auth/
__Method__        | POST  
__Authentication__         | None       
__Response Codes__         | 200 - Successful<br/>401 - Unauthorized <br/>400 - Bad Request        

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


# Participant

 |  | 
:----------- | :----------- 
__Description__         | Get study participants.
__Endpoint__         | /participant/       
__Method__         | GET
__Pagination__         | Limit Offset: This pagination style mirrors the syntax used when looking up multiple database records. The client includes both a `limit` and an `offset` query parameter. The limit indicates the maximum number of items to return, and defaults to 20 records. The offset indicates the starting position of the query in relation to the complete set of unpaginated items.  
__Authentication__         | Token  
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request   

Response Object
```
{
  "count": 20,
  "next": null,
  "previous": null,
  "results": [
    {
      "username": "testuser0",
      "first_name": "Chris",
      "last_name": "Smith",
      "email": "fakeemail@rti.org",
      "gender": "Male",
      "dob": "1971-09-04"
    },
    {
      "username": "testuser1",
      "first_name": "Sue",
      "last_name": "Smith",
      "email": "fakeemail@rti.org",
      "gender": "Female",
      "dob": "1983-03-04"
    },
    ...
    ]
}

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


# Participant Consent

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



# Survey Submission

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

|  | 
:----------- | :----------- 
__Description__         | Get survey submissions.
__Endpoint__         | /submission/  
__Method__         | GET       
__Pagination__         | Limit Offset: This pagination style mirrors the syntax used when looking up multiple database records. The client includes both a `limit` and an `offset` query parameter. The limit indicates the maximum number of items to return, and defaults to 20 records. The offset indicates the starting position of the query in relation to the complete set of unpaginated items.  
__Authentication__         | Token        
__Response Codes__         | 200 - Sucessful<br/>401 - Unauthorized <br/>400 - Bad Request

Response Object
```
{
  "count": 105,
  "next": "http://localhost:8000/submission/?limit=20&offset=20",
  "previous": null,
  "results": [
    {
      "id": 23,
      "participant": {
        "username": "testuser0",
        "email": "fakeemail@rti.org",
        "first_name": "Piper",
        "last_name": "Walters",
        "gender": "Male",
        "dob": "1984-05-23"
      },
      "time_start": "2016-03-30T20:54:17.142617Z",
      "time_complete": "2016-03-30T20:54:17.142632Z",
      "timestamp": "2016-03-30T20:54:17.164977Z",
      "device_id": "TEST-49D5-4CAD-AE42-E5CE922A3346",
      "response": {
        "mood image": "6",
        "mood cateogry": "fine",
        "mood scale": "2"
      },
      "lat": 45.5423508,
      "long": -122.7945071,
      "place": "Portland, OR US"
    },
    {
      "id": 24,
      "participant": {
        "username": "testuser0",
        "email": "fakeemail@rti.org",
        "first_name": "Piper",
        "last_name": "Walters",
        "gender": "Male",
        "dob": "1984-05-23"
      },
      "time_start": "2016-03-30T20:54:17.291626Z",
      "time_complete": "2016-03-30T20:54:17.291638Z",
      "timestamp": "2016-03-30T20:54:17.292202Z",
      "device_id": "TEST-49D5-4CAD-AE42-E5CE922A3346",
      "response": {
        "mood image": "9",
        "mood cateogry": "good",
        "mood scale": "7"
      },
      "lat": 39.1490189,
      "long": -107.1444289,
      "place": "Marble, CO US"
    },
    ...
    ]
}

```


_If you are feeling adventurous, try running this in [Postman](https://app.getpostman.com/run-collection/6241de2d723c0c4b8780)._



