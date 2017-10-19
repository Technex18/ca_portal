# Technex CA

# Api Documentation

## Login Api
<br><br>

Url: http://technex-ca.herokuapp.com/api/login/
<br>
Method: POST
<br>
Json object Expected :<br>   {
	<br>"email":"bikram.bharti99@gmail.com",
	<br>"password":"caportal"
<br>}
                                         
Json Response for Wrong Post Request Method: <br>	{<br>
												"status":"4"<br>
												}<br><br>
							
Json Response for wrong user: <br> { <br>
									"status":"3"<br>
									}<br><br>
									
Json Response for inactive user: <br>{ <br>
                                      "status": "2"<br>
                                      }<br><br>
                                      
Json Response if user ca profile is not chosen: <br> { <br>
                                                        "status" : "0"<br>
                                                        }<br><br>
Json Response if user ca profile is chosen: <br> {<br>
                                                      "status": "1"<br>
                                                       "whatsappNumber": 9999999999,<br>
    "first_name": "bikram",<br>
    "last_name": "bharti",<br>
    "pastExp": "test",<br>
    "pinCode": 111111,<br>
    "whyChooseYou": "test",<br>
    "email": "bikram.bharti99@gmail.com",<br>
    "postel_address": "123A XYZ Colony"<br>
    "college": "test",<br>
    "mobileNumber": 9999999999,<br>
    "status": 1,<br>
    "year": 2<br>                                }<br><br><br>
				
				
				
## AccountdetailApi
<br><br>
Url: http://technex-ca.herokuapp.com/api/editprofile/
<br>
Method: POST
<br>
Json object Expected :<br>   {
  <br>
      <br>"email":"bikram.bharti99@gmail.com",
      <br>"first_name":"new firstname",
      <br>"last_name":"new lastname",
      <br>"mobileNumber":1234567898,
      <br>"whatsappNumber":9999999999,
      <br>"pinCode":123456,
      <br>"postal_address":"new address",
      <br>"year": 2
<br>}

Json Response for Wrong Post Request Method: <br> {<br>
                        "status":"Invalid Request"<br>
                        }<br><br>

Json Response for profile edit confirmation: <br> {<br>
                        "status":"OK"<br>
                        }<br><br><br>


## DashboardApi
<br><br>

Url: http://technex-ca.herokuapp.com/api/dashboard/
<br>
Method: POST
<br>
Json object Expected :<br>   {
  <br>"email":"bikram.bharti99@gmail.com"
<br>}

Json Response for Wrong Post Request Method: <br> {<br>
                        "status": 0 <br>
                        }<br><br>

Json Response for No Director Detail: <br>{
<br>
                                  "status":2 <br> }<br><br>

Json Response for No Student Body detail: <br>{
<br>
                                  "status":3 <br> }<br><br> 

Json Response for No Director Detail and No student Body detail : <br>{
<br>
                                  "status":4 <br> }<br><br>                

Json Response for Director detail, student detail: <br> {<br>
                        "status": 1<br>
                        "directordetail":"Details of the Director"<br>
                        "studentbodydetail":"Details of student body"<br>
                        }<br><br><br>

## LeaderApi
<br><br>

Url: http://technex-ca.herokuapp.com/api/leader/
<br>
Method: POST
<br>
Json object Expected :<br>   {
  <br>"email":"bikram.bharti99@gmail.com"
<br>}

Json Response for Wrong Post Request Method: <br> {<br>
                        "status": 0 <br>
                        }<br><br>
			
Json Response for a non choosen CA: <br> {<br>
			"status": 2 <br>
			}<br><br>

Json Response for points: <br> {<br>
                        "status": 1<br>
                        "points": 10<br>
			"rank": 3(Same rank for same points and others as per position in list)<br>
                        }<br><br><br>


## LeaderBoardApi
<br><br>

Url: http://technex-ca.herokuapp.com/api/leaderboard/
<br>
Method: GET
<br>

Json Response for Wrong GET Request Method: <br> {<br>
                        "status": 0 <br>
                        }<br><br>

Json Response for LeaderBoard: <br> {<br>
                        "Leaderboard": [<br>
				{<br>
                        	"rank": 3<br>
				"points": 10(Same rank for same points and others as per position in list)<br>
				"username": "bikram.bharti99@gmail.com"(email id is the username)<br>
				},<br>
				{<br>
				"rank": 3<br>
				"points": 10(Same rank for same points and others as per position in list)<br>
				"username": "kautilyakatiha10@gmail.com"(email id is the username)<br>
				}<br>
				{<br>
				"rank": 5<br>
				"points": 8(Same rank for same points and others as per position in list)<br>
				"username": "something@gmail.com"(email id is the username)<br>
				}<br>
			]<br>
                        }<br><br><br>


## DashboardUpdateApi
<br><br>

Url: http://technex-ca.herokuapp.com/api/update/
<br>
Method: POST
<br>
Json object Expected :<br>   {
  <br>"email":"bikram.bharti99@gmail.com"
  <br>"directordetail":"Updated director details"
  <br>"studentbodydetail":"Updated studentbody details"
  <br>"notification":<br>[<br>
                      {<br>
                       "creation_time":"2017-10-07T12:13:10.756000+00:00"(String type casted time)<br>
                       "mark_read":boolean(true/false)<br>
                      }<br>
                      {<br>
                       "creation_time":"2017-10-07 12:12:42.037000+00:00"(String type casted time)<br>
                       "mark_read":boolean(true/false)<br>
                      }<br>
                     ]<br>
		}                

Json Response no notification for given creation_time: <br> {<br>
							"status":2<br>
							}<br><br>
                        
Json Response for update confirmation: <br> {<br>
                        "status": 1<br>
                        }<br><br><br>

## NotificationApi
<br><br>

Url: http://technex-ca.herokuapp.com/api/notification/
<br>
Method: POST
<br>
Json object Expected :<br>   {
  <br>"email":"bikram.bharti99@gmail.com"
<br>}

Json Response for Wrong Post Request Method: <br> {<br>
                        "status": 0 <br>
                        }<br><br>                

Json Response for notifications: <br> {<br>
                        "status": 1<br>
                        "notification":<br>[<br>
                                        {<br>
                                          "message":"Message of first notification"<br>
                                          "creation_time":"2017-10-07 12:12:54.656000+00:00"(String type casted time)<br>
                                          "mark_read":boolean(true/false)<br>
                                        }<br>
                                        {<br>
                                          "message":"Message of second notification"<br>
                                          "creation_time":"2017-10-07 12:13:10.756000+00:00"(String type casted time)<br>
                                          "mark_read":boolean(true/false)<br>
                                        }<br>
                                      ]<br>
                        }<br><br><br>
