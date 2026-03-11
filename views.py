from django.shortcuts import render
from django.http import HttpResponse
from .models import Database
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# ////////////////////////////////////////////////////////////////////////////////
def gallery(request):
    return render(request , 'gallery.html ')
def aboutus(request):
    return render(request , 'aboutus.html ')
def contact(request):
    return render(request , 'contact.html ')
def privacy(request):
    return render(request , 'privacy.html ')

def model_accuracy(request):
    # Load the dataset
    data = pd.read_csv('C:\\Users\\GUNJAN\\Desktop\\healthdjango - Copy - Copy - Copy (2)\\heathproject\\healthapp\\Book2.csv')

    # Select features and target variable
    features = ['Market Prices (INR)', 'Market Demand (tons)', 'Market Supply (tons)',
                'Storage Duration (months)','Price Spike',
                'Crop Quality Rating','Market Trends', 'Harvest Date (Month)','Weather Condition (Month)','Storage Duration (months)','Crop Rotation','Yield Predicted by Farmer','Actual Harvested Yield','Actual Distributed Yield','Crop Type','Historical Yield Data (tons)', 'Consumer Preference','Storage Cost (per ton)','Transport Cost (per km)','Weather Change (Yes/No)','Sowing Date (Month)']
    target = 'Intentional Storage (Yes/No)'

    X = data[features]
    y = data[target]

    # Split the data into training and testing sets
   #  rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load the trained model
    rf_model = joblib.load('C:\\Users\\GUNJAN\\Desktop\\healthdjango - Copy - Copy - Copy (2)\\heathproject\\healthapp\\trained_model.joblib')

    # Calculate training accuracy
    
    
    y_train_pred = rf_model.predict(X_train)
    training_accuracy =accuracy_score(y_train, y_train_pred)
    tr_ac=100*training_accuracy
    

    # Calculate testing accuracy
   #  rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
   #  rf_model = RandomForestClassifier(random_state=42, max_depth=10)

    y_test_pred = rf_model.predict(X_test)
    testing_accuracy = accuracy_score(y_test, y_test_pred)
    te_ac=100*testing_accuracy

    return render(request, 'model_accuracy.html', {'training_accuracy': tr_ac, 'testing_accuracy': te_ac})


#//////////////////////////////////////////////////////////////////////////////


def index(request):
    return render(request , 'landing.html ')
def indexx(request):
    return render(request , 'index.html ')

def next_page(request):
    return render(request, 'next_page.html')

def secondpage(request):
    return render(request, 'second.html')

def anxiety(request):
   return render(request, 'anxiety.html')
def panic(request):
   return render(request, 'panic.html')
def phsycotic(request):
   return render(request, 'phsycotic.html')
def depression(request):
   return render(request, 'depression.html')
def eating(request):
   return render(request, 'eating.html')
def anxietysil(request):
   return render(request, 'anxietysil.html')
def panicsol(request):
   return render(request, 'panicsol.html')
def phsycoticsol(request):
   return render(request, 'phsycoticsol.html')
def depressionsol(request):
   return render(request, 'depressionsol.html')
def eatingsol(request):
   return render(request, 'eatingsol.html')

def take_input(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    user1= request.POST.get("user_name1")
    user2= request.POST.get("user_name2")
    user3= request.POST.get("user_name3")
    user4= request.POST.get("user_name4")
    user5= request.POST.get("user_name5")
    user6= request.POST.get("user_name6")
    user7= request.POST.get("user_name7")
    user8= request.POST.get("user_name8")
    user9= request.POST.get("user_name9")
    user10= request.POST.get("user_name10")
    user11= request.POST.get("user_name11")
    user12= request.POST.get("user_name12")
    user13= request.POST.get("user_name13")
    user14= request.POST.get("user_name14")
    user15= request.POST.get("user_name15")
    user16= request.POST.get("user_name16")
    user17= request.POST.get("user_name17")
    user18= request.POST.get("user_name18")
    user19= request.POST.get("user_name19")
    user20= request.POST.get("user_name20")
    newinput= Database(name1=name,email1= email,username1=user1,username2=user2, username3=user3, username4=user4,username5=user5,username6=user6,username7=user7, username8=user8, username9=user9,username10=user10,username11=user11,username12=user12, username13=user13, username14=user14,username15=user15,username16=user16,username17=user17, username18=user18, username19=user19,username20=user20  )
    
    if user1 == request.POST.get("user_name1") and user2== request.POST.get("user_name2") and user3==request.POST.get("user_name3")  and user4==request.POST.get("user_name4") :
     newinput.save()
     return render(request, 'panic.html')
    elif user5 == request.POST.get("user_name5") and user6== request.POST.get("user_name6") and user7==request.POST.get("user_name7")  and user8==request.POST.get("user_name8")  :
      newinput.save()
      return render(request, 'panic.html')
    elif user9 == request.POST.get("user_name9") and user10== request.POST.get("user_name10") and user11==request.POST.get("user_name11")  and user12==request.POST.get("user_name12"):
       newinput.save()
       return render(request,'phsycotic.html' )
    if user13 == request.POST.get("user_name13") and user14== request.POST.get("user_name14") and user15==request.POST.get("user_name15")  and user16==request.POST.get("user_name16"):
       newinput.save()
       return render(request, 'depression.html')
    if user17 == request.POST.get("user_name17") and user18== request.POST.get("user_name18") and user19==request.POST.get("user_name19")  and user20==request.POST.get("user_name20"):
       newinput.save()
       return render(request, 'eating.html')
    else:
       
       return HttpResponse('Fill Again..!')
       
    
    
   

# Create your views here.
