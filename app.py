#app.py
from flask import Flask
app=Flask(__name__) #__name__ represent current module

@app.route("/") #decorator of function (decorator)
def home():
    return "Hello Flask"
@app.route("/test")#represent the path of website we wanna use
def test():
    return "this is test"

if __name__=="__main__": #if it is executed by main program
    app.run() #execute the server
    
