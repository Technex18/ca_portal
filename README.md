# TECHNEX

# Api Documentation
## Registration Api
<br> <br>
Url: http://technex-ca.herokuapp.com/api/register
<br>
Method: POST
<br>
Json object Expected : 			//(all fields required)<br>
								{<br>
									"email" : emailOfUser,<br>
									"first_name" : firstName,<br>
									"last_name" : lastName,<br>
									"password" : password,<br>
									"college" : collegeName,<br>
									"year" : year(1,2,3,4,5)<br>
									"mobile_number" : mobileNumber<br>
								 }<br><br>

Json Response for Successful registration:<br>
								{<br>
								 	"status" : "Profile created successfully"<br>
								}<br><br>

Json Response for Error in Registration(validation Erorr):<br>
								{<br>
									"status" : "Registration in error",<br>
									"field_name": errorInField //field_name is same as above expected<br>
								}<br><br>

Json Response for Invalid Request(requests other than post):<br>
								{<br>
									"Error" : True,<br>
									"status" : "invalid request,Post request Please!"<br>
								}<br><br><br>

## Login Api
<br><br>
Url: http://technex-ca.herokuapp.com/api/login
<br>
Method: POST
<br>
Json object Expected:<br>			{<br>
									"email" : email,<br>
									"password" : password<br>
								}<br><br>

Json Response for successful Login: <br>
								{<br>
									"status" : "logged in"<br>
								}<br><br>

Json Response for wrong Username/password:<br>
								{<br>
									"Error" : True,<br>
									"status" : "Invalid Credentials!"<br>
								}<br>

Json Response for invalid form submission(empty username/password and other validation errors):<br>
								{<br>
									"Error" : True,<br>
									"status" : "Please Fill the form correctly!"<br>
								}<br><br><br>					

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

Json Response for Director detail, student detail, notifications: <br> {<br>
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
                        "directordetail":"Details of the Director"<br>
                        "studentbodydetail":"Details of student body"<br>
                        }<br><br><br>

## LeaderBoardApi
<br><br>

Url: http://technex-ca.herokuapp.com/api/leaderboard/
<br>
Method: POST
<br>
Json object Expected :<br>   {
  <br>"email":"bikram.bharti99@gmail.com"
<br>}

Json Response for Wrong Post Request Method: <br> {<br>
                        "status": 0 <br>
                        }<br><br>

Json Response for points: <br> {<br>
                        "status": 1<br>
                        "points":10<br>
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
                       "creation_time":"2017-10-07 12:12:42.037000+00:00"(String type casted time)<br>
                       "mark_read":boolean(true/false)<br>
                      }<br>
                      {<br>
                       "creation_time":"2017-10-07T12:13:10.756000+00:00"(String type casted time)<br>
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
