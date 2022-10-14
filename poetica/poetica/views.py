from django.shortcuts import render
import pyrebase
 
config={
    "apiKey": "AIzaSyCaDqoWU6hoe6-UcgkiVzjPKNHbRh4XUcE",
    "authDomain": "poetica-1ff63.firebaseapp.com",
    "databaseURL": "https://poetica-1ff63-default-rtdb.firebaseio.com/",
    "projectId": "poetica-1ff63.appspot.com",
    "storageBucket": "63071574397",
    "messagingSenderId": "1:63071574397:web:f654a30da6e2bfee1fd414",
    "appId": "G-T448X1VV35"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def index(request):
        #accessing our firebase data and storing it in a variable
        name = database.child('Data').child('Name').get().val()
        stack = database.child('Data').child('Stack').get().val()
        framework = database.child('Data').child('Framework').get().val()
    
        context = {
            'name':name,
            'stack':stack,
            'framework':framework
        }
        return render(request, 'index.html', context)