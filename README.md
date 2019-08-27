py-rec-task-1
=============

## DESCRIPTION
Simple web benchmark that measure page load time and compare it with competitive web pages.

## CONCEPTS THAT I TRIED TO PRESENT
* clean architecture
* event driven architecture
* ddd
* cqrs
* command bus
* python typing :)

## RUN APPLICATION 
Application have simple web interface, everything You need to do to 
run it is execute run.py and visit http://localhost:5000 :)
I think best way to run application is to create virtual env with python 3.6.5 and install requirements from requirements.txt

## RUN TESTS
To run the tests execute

`py.test`

## ADDITIONAL FEATURES
* if You want to receive sms You need to update NOTIFICATION_SMS_PHONE_NUMBER key in configuration module
* if You want to receive emails You need to update NOTIFICATION_EMAIL key in configuration module and provide some smtp configuration in same place

## TODO
* error handling
* validation
* documentation
* async benchmarking
* practice english :P

## COMPATIBILITY:
Compatible with Python 3.6
