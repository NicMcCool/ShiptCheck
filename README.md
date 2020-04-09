# ShiptCheck 
### a simple web query tool to notify when deliveries are available on Shipt
##### ShiptCheck uses a headless instance of Chrome and an OAuth bypass/migration to access Shipt 

## SETUP 
### Install requirements.txt.
### Update the *config-template.py* file and rename to *config.py*:
* *userID* = Your google login ID
* *userPW* = Your google login Password
* *driverLoc* = This app uses Chrome, so you'll need [Chromedriver](https://chromedriver.chromium.org/downloads). Enter the path where it's saved. 
* *googlePage* = A generic google OAuth landing page. [StackOverflow has one](https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&as=AdbJ-lkEluBIh0zm96n9hQ&destination=https%3A%2F%2Fstackauth.com&approval_state=!ChRKU1lFZGpodEk1SlZYRm1OWF9pMhIfazJ0NDdJNDE2Y2thMEs2dFEwd1Nsa3NsZDRfSUZSYw%E2%88%99AF-3PDcAAAAAXo_KlPcol3aWcsl5fRg6m6Q7R5WbLYOz&oauthgdpr=1&xsrfsig=ChkAeAh8T76hwI-2c_g1CioP8-P3rd2dlTdsEg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow) as an example.  
* *pbAPI* = Your [PushBullett API](https://docs.pushbullet.com/)