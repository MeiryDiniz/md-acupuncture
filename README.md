# MD|ACUPUNCTURE

This project is a web application developed using Django and Django Allauth for user management, built for managing acupuncture appointments and user profiles. It includes features such as account registration, user profile management, and custom forms for collecting personal information. 

![M|D ACUPUNCTURE](/workspace/md-acupuncture/static/images/readme-md/Screenshot 2024-11-29 224907.png)

Visit the live version of the web application: [M|D ACUPUNCTURE](https://md-booking-system-e8987ebab81d.herokuapp.com/)

- - -

## CONTENTS

* [PROJECT OVERVIEW](#project-overview)
* [TECHNOLOGIES USED](#technologies-used)
* [FEATURES](#features)  
* [TESTS](#tests)
  * [AUTOMATED TESTS](#automated-tests)  
* [MANUAL TESTS](#manual-tests)
   * [TESTS DONE BY THE DEVELOPER](#test-done-by-developer)
* [BUGS](#bugs)
   * [FIXED BUGS](#fixed-bugs)   
   * [UNFIXED BUGS](#unfixed-bugs)
* [DEPLOYMENT](#deployment) 
* [RESOURCE](#resource)  
* [CONTENT](#content)
* [CREDITS](#credits)  

- - -

## PROJECT OVERVIEW

MD Acupuncture is a web application designed to manage acupuncture clinic appointments and user profiles. The application allows users to sign up, manage their personal information, and book appointments. The primary functionalities of the app include:
 + User authentication and profile management using **Django Allauth**.
 + User registration with custom fields (first name, last name, date of birth, email address, etc.).
 + Custom user profile creation for storing extended user information.
 + Acupuncture appointment management (to be added).

- - -

## TECHNOLOGIES USED

This project uses the following technologies:
 + **Django:** The web framework used for developing the application.
 + **Django Allauth:** Used for user authentication, registration, and account management.
 + **Bootstrap:** Used for styling the frontend and ensuring a responsive layout.
 + **Neon Database**: The cloud-native PostgreSQL database used for storing the app’s data.
 + **SQLite:** The default database for development.
 + **Python 3.x:** The programming language used for backend development.
 + **HTML/CSS:** For structuring and styling the frontend.

- - -

## FEATURES

+ **User Authentication:** Users can sign up, log in, and manage their accounts.
+ **Custom Signup Form:** The signup form collects additional user data such as first name, last name, date of birth and email address.
+ **User Profiles:** Extended user information is stored in the UserProfile model.
+ **Patients Page:** Allows users to view their scheduled appointments and manage them.
+ **Responsive Design:** The app is designed to be mobile-friendly using Bootstrap.
+ **Password Reset:** Users can reset their passwords using the built-in Django Allauth functionality.

## TESTS

###  AUTOMATED TESTS

Django's built-in test framework was used to validate the code, and any error returned: `python3 manage.py runserver`
```
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...F.
======================================================================
FAIL: test_logout_view (booking.tests.AppointmentTests.test_logout_view)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/md-acupuncture/booking/tests.py", line 48, in test_logout_view
    self.assertEqual(response.status_code, 302)
AssertionError: 200 != 302
----------------------------------------------------------------------

Ran 5 tests in 6.546s

FAILED (failures=1)
Destroying test database for alias 'default'...
``` 

- - -

## MANUAL TESTING

### Test done by developer

Have APP features tested.

| Feature | Expected Outcome | Testing Performed | Result | Passed/Failed 
| --- | --- | --- | --- | --- |
| **Register** | Have a new user account set up. | Data was inputted to have a new user account created. | The new user account was set up. | Passed | 
| **Log in** | Log in as an user. | Be able to log in and have access to the app features. | User could log in. | Passed |
| **Book an Appointment** | Have an appointment booked. | Choose a date and time to have an appointment booked. | Appointment was booked. | Passed | 
| **Edit an Appointment** | Have an appointment edited. | Choose an appointment booked already booked and have it edited. | Appointment was updated. | Passed |
| **Delete an Appointment** | Have an deleted. | Choose an appointment booked that need to be deleted. | Appointment was deleted. | Passed |
| **Log out** | Have account loged out. | Be able to log out once the user is logged in. | User could log out. | Passed |
| **Reset Password** | Have password reset. | Click on the `Forgot Password` link to follow the instructions to have password reset. | Password was reset. | Passed |

- - -

## BUGS

### FIXED BUGS

| Bug | Reason | Action |
| --- | --- | --- |
| The ``automated test`` returned that some templates were not rendering correctly . | It happended because in certain scenarios templates names were wrong. | This was resolved by correctly managing the names in the templates views and ensuring proper rendering.|

I had a considerable number of problems with the result of functions in my code and also, how them were running. It happened because I was not using the correct indentation and sequence to write the functions. I revised the course content, did research on google and kept trying until I got the result that I needed. 

### UNFIXED BUGS
There is an issue with the logout functionality during the tests. The test expects a 302 status code (redirect), but it receives a 200 status code instead. This indicates that the logout view is not correctly redirecting to the login page. Despite attempts to resolve this, the issue persists.
- - -

## DEPLOYMENT 

The **M|D ACUPUNCTURE** APP was deployed on Heroku using Code Institute's mock terminal.

- - -

## RESOURCE

In addition to the course content I used [Stack Overflow](http://stackoverflow.com) to do research to develop my APP. 

- - - 

## CONTENT

The content and code of the program were wrote by the developer.

- - - 

## CREDITS

I used the Code Intitute's **Love Sandwiches** milestone project as a base to develop my proram and understand better how to use ``Python`` on its development.

The Favicon used was taken from [Flaticon](https://www.flaticon.com/free-icon/acupuncture_1996928?term=acupuncture&related_id=1996928)


