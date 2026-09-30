# centralized settings for the app, instead of hardcoding values everywhere

class Config:
    SECRET_KEY = "h4r0h4p1" #protects sessions, makes sure the login sessions are secure
    
    DB_HOST = "127.0.0.1" #where the db lives, localhost bc we use phpMyAdmin
    DB_PORT = 3306
    DB_USER = "root" # my mysql username
    DB_PASSWORD = "" #mysql password
    DB_NAME =  "csci213_project" #database to use in sql
