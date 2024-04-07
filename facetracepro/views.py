from django.shortcuts import render,redirect
from .models import Login,Police,MissingPerson,User
import datetime
import re
from django.contrib.auth.hashers import make_password
import face_recognition
import cv2
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import random
import string
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.db.models import Q
    



# def login(request):
#     if(request.POST):
#         email=request.POST['email']
#         password=request.POST['password']
        
#         # pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
#         # match = pattern.match(email)
#         # if(not bool(match)):
#         #     return(render(request,"login.html",{"error":"Enter Proper Email"}))
#         if (email == 'admin@gmail.com' and password == 'admin'):
#             return (redirect(adminhome))
#         obj=Login.objects.filter(email=email,password=password)
#         if(obj):
#             return(redirect(userhome))

#     return(render (request,"login.html"))

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if the provided email and password match the admin credentials
#         if email == 'admin@gmail.com' and password == 'admin':
#             return redirect(adminhome)

        
#         user = Login.objects.filter(email=email, password=password).first()
#         if user.is_police==True:
#             return redirect(policehome)
#         elif(user.is_police==False):
#             return redirect(userhome)


#         return render(request, 'login.html', {'error': 'Invalid email or password'})

#     return render(request, 'login.html')
# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if the provided email and password match the admin credentials
#         if email == 'admin@gmail.com' and password == 'admin':
#             return redirect('adminhome')

#         user = Login.objects.filter(email=email, password=password).first()
#         if user:
#             request.session['user_id'] = user.id
#             if user.is_police:
#                 return redirect(policehome)
#             else:
#                 return redirect(userhome)

#         return render(request, 'login.html', {'error': 'Invalid email or password'})

#     return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the provided email and password match the admin credentials
        if email == 'admin@gmail.com' and password == 'admin':
            return redirect(adminhome)

        user = Login.objects.filter(email=email, password=password).first()
        if user:
            request.session['user_id'] = user.id
            if user.is_police:
                # Store the police_id in the session
                # police = Police.objects.get(login_id_id=user.id)
                # request.session['police_id'] = police.id
                return redirect(policehome)
            else:
                return redirect(userhome)

        return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')

def logout(request):
    return redirect(eg3)
# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if the provided email and password match the admin credentials
#         if email == 'admin@gmail.com' and password == 'admin':
#             return redirect('adminhome')

#         user = Login.objects.filter(email=email, password=password).first()
#         if user:
#             request.session['user_id'] = user.id
#             if user.is_police:
#                 # Store the police_id in the session
#                 police = Police.objects.get(login_id=user.id)
#                 request.session['police_id'] = police.id
#                 return redirect(policehome)
#             else:
#                 # Clear any existing 'police_id' session variable for regular users
#                 if 'police_id' in request.session:
#                     del request.session['police_id']
#                 return redirect(userhome)

#         return render(request, 'login.html', {'error': 'Invalid email or password'})

#     return render(request, 'login.html')











def mainhome(request):
    return(render(request,"mainhome.html"))
def eg3(request):
    return(render(request,"eg3.html"))
def aboutus(request):
    return(render(request,"aboutus.html"))



def adminhome(request):
    return(render(request,"adminhome.html"))
# def userhome(request):
#     return(render(request,"userhome.html"))
# def policehome(request):
#     return(render(request,"policehome.html"))
def userhome(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = User.objects.get(login_id=user_id)
        return render(request, "userhome.html", {'user_id': user_id, 'user': user})
    else:
        return redirect(login)

def policehome(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        police = Police.objects.get(login_id=user_id)
        return render(request, "policehome2.html", {'user_id': user_id, 'police': police})
    else:
        return redirect(login)
def reportpolice(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('dob')
        address = request.POST.get('address')
        aadhar_number = request.POST.get('aadhar_number')
        missing_from = request.POST.get('missing_date')
        image = request.FILES.get('image')
        gender = request.POST.get('gender')
        reported_by= request.session.get('user_id')
        investigating_police= request.session.get('user_id')
        
        # Check if the user is a police officer
        # if 'police_id' in request.session:
        #     # If so, get the investigating police ID from the session
        #     investigating_police_id = request.session.get('police_id')
        # else:
        #     # If not, set investigating_police_id to None
        #     investigating_police_id = None

        # # Check if investigating_police_id is available
        # if investigating_police_id is None:
        #     # Print a message indicating that investigating_police_id is not available
        #     print("Investigating police id is not available")

        #     # Return a response indicating the issue
        #     return render(request, 'report.html', {'error': 'Investigating police id is not available'})

        # Create the MissingPerson object
        person = MissingPerson(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            address=address,
            aadhar_number=aadhar_number,
            missing_from=missing_from,
            image=image,
            gender=gender,
            reported_by=reported_by,
            investigating_police=investigating_police
        )
        print("************")
        print(reported_by)
        person.save()
        return render(request, 'policehome2.html')
        # return render(request, 'report_police.html', {"message": "successful"})

    return render(request, 'report_police.html')






# def reportuser(request):
#     if request.method == 'POST':
#         # Extract form data
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         date_of_birth = request.POST.get('dob')
#         address = request.POST.get('address')
#         aadhar_number = request.POST.get('aadhar_number')
#         missing_from = request.POST.get('missing_date')
#         image = request.FILES.get('image')
#         gender = request.POST.get('gender')

#         # Assuming you have already set 'user_id' in the session
#         reported_by = request.session.get('user_id')

#         # Get the police station based on the provided location
#         # Note: You need to define how you're getting the location from the form
#         # For this example, let's assume you get it from the form directly
#         location = request.POST.get('location')

#         # Check if the location exists
#         police_station = Police.objects.filter(location=location).first()

#         if police_station:
#             # If police station is found, use its id as investigating_police
#             investigating_police = police_station.id

#             # Create the MissingPerson object with the provided data
#             person = MissingPerson.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 date_of_birth=date_of_birth,
#                 address=address,
#                 aadhar_number=aadhar_number,
#                 missing_from=missing_from,
#                 image=image,
#                 gender=gender,
#                 location=location,
#                 reported_by=reported_by,
#                 investigating_police=investigating_police
#             )
#             person.save()
#             print("************")
#             print(reported_by)

#             print(location)

#             return render(request, 'report_user.html', {'location': location})
#         else:
#             # If no police station is found for the provided location, handle the error
#             return render(request, 'report_user.html', {"error": "No police station found for the provided location."})

#     return render(request, 'report_user.html')


# def reportuser(request):
#     if request.method == 'POST':
#         # Extract form data
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         date_of_birth = request.POST.get('dob')
#         address = request.POST.get('address')
#         aadhar_number = request.POST.get('aadhar_number')
#         missing_from = request.POST.get('missing_date')
#         image = request.FILES.get('image')
#         gender = request.POST.get('gender')

#         # Assuming you have already set 'user_id' in the session
#         reported_by = request.session.get('user_id')

#         # Get the police station based on the provided location
#         # Note: You need to define how you're getting the location from the form
#         # For this example, let's assume you get it from the form directly
#         location = request.POST.get('location')

#         # Check if the location exists
#         police_station = Police.objects.filter(location=location).first()

#         if police_station:
#             # If police station is found, use its id as investigating_police
#             investigating_police = police_station.id

#             # Create the MissingPerson object with the provided data
#             person = MissingPerson.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 date_of_birth=date_of_birth,
#                 address=address,
#                 aadhar_number=aadhar_number,
#                 missing_from=missing_from,
#                 image=image,
#                 gender=gender,
#                 location=location,
#                 reported_by=reported_by,
#                 investigating_police=investigating_police
#             )
#             person.save()
#             print("************")
#             print(reported_by)

#             print(location)

#             return render(request, 'report_user.html', {'location': location})
#         else:
#             # If no police station is found for the provided location, handle the error
#             return render(request, 'report_user.html', {"error": "No police station found for the provided location."})

#     # Fetch all police station locations
#     police_stations = Police.objects.values_list('location', flat=True)

#     return render(request, 'report_user.html', {'police_stations': police_stations})

def reportuser(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('dob')
        address = request.POST.get('address')
        aadhar_number = request.POST.get('aadhar_number')
        missing_from = request.POST.get('missing_date')
        image = request.FILES.get('image')
        gender = request.POST.get('gender')

        # Assuming you have already set 'user_id' in the session
        reported_by = request.session.get('user_id')

        # Get the police station based on the provided location
        # Note: You need to define how you're getting the location from the form
        # For this example, let's assume you get it from the form directly
        location = request.POST.get('location')
        if(MissingPerson.objects.filter(aadhar_number=aadhar_number)):
            return render(request, 'report_user.html', {"error": "Case already exist for this Aadhar number"})

        # Check if the location exists
        police_station = Police.objects.filter(location=location).first()

        if police_station:
            # If police station is found, use its id as investigating_police
            investigating_police = police_station.login_id

            # Create the MissingPerson object with the provided data
            person = MissingPerson.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                address=address,
                aadhar_number=aadhar_number,
                missing_from=missing_from,
                image=image,
                gender=gender,
                location=location,
                reported_by=reported_by,
                investigating_police=investigating_police
            )
            person.save()

            # Store investigating_police ID in session
            request.session['investigating_police_id'] = investigating_police

            print("************")
            print(reported_by)
            print(location)

            return render(request, 'report_user.html', {'location': location})
        else:
            # If no police station is found for the provided location, handle the error
            return render(request, 'report_user.html', {"error": "No police station found for the provided location."})

    # Fetch all police station locations
    police_stations = Police.objects.values_list('location', flat=True)

    return render(request, 'report_user.html', {'police_stations': police_stations})









   
    

def surveillance(request):
    return(render(request,"surveillance.html"))
# def detect(request):
    

#     known_images = []
#     for person in MissingPerson.objects.all():
#         known_images.append(face_recognition.load_image_file(person.image.path))

#     # Encode the known faces
#     known_face_encodings = [face_recognition.face_encodings(img)[0] for img in known_images]

#     # Open the default camera (camera index 0)
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # Find face locations and encodings in the current frame
#         face_locations = face_recognition.face_locations(frame)
#         face_encodings = face_recognition.face_encodings(frame, face_locations)

#         for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
#             # Compare detected face with the known faces
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

#             name = "Unknown"
#             for i, match in enumerate(matches):
#                 if match:
#                     name = f"Person {i + 1}"
#                     break

#             # Display a rectangle around the detected face
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             # Display the name on the frame
#             cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

#         # Display the frame
#         cv2.imshow('Camera Feed', frame)

#         # Break the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the camera when everything is done
#     cap.release()
#     cv2.destroyAllWindows()

#     return render(request, "surveillance.html")






def detect(request):
    known_images = []
    for person in MissingPerson.objects.all():
        known_images.append(face_recognition.load_image_file(person.image.path))

    # Encode the known faces
    known_face_encodings = [face_recognition.face_encodings(img)[0] for img in known_images]

    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Find face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        if face_encodings:  # Check if face_encodings is not empty
            for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
                # Compare detected face with the known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"
                for i, match in enumerate(matches):
                    if match:
                        name = f"Person {i + 1}"
                        break

                # Display a rectangle around the detected face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                # Display the name on the frame
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera when everything is done
    cap.release()
    cv2.destroyAllWindows()

    return render(request, "surveillance.html")


def register(request):
    if(request.POST):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pp']
        phone=request.POST['phone']
        obj=Login(email=email,password=password,is_police=0)
        obj.save()
        lg_id=obj.id
        obj2=User(login_id=lg_id,name=name,phn_num=phone)
        obj2.save()
    return redirect(login)




# def addpolice(request):
#     if(request.POST):
#         ps=request.POST['policestation']
#         address=request.POST['address']
#         location=request.POST['location']
#         pn=request.POST['pn']
#         email=request.POST['email']
#         obj=Police(policestation=ps,address=address,location=location,phnnum=pn,email=email)
#         obj.save()
#         return(redirect(viewpolice))
#     return(render(request,"reportpolice.h

def addpolice(request):
    if request.method == 'POST':
        # Extract form data from request.POST
        ps = request.POST.get('policestation')
        address = request.POST.get('address')
        location = request.POST.get('location')
        pn = request.POST.get('pn')
        email = request.POST.get('email')
        password = generate_random_password()
        obj_police=Login(email=email,password=password,is_police=1)
        obj_police.save()
        lg_id=obj_police.id
        obj2_police=Police(login_id=lg_id,policestation=ps, address=address, location=location, phnnum=pn)
        obj2_police.save()

 

        # Generate a random password for the police station
       

        # Send email to the police station with username and password
        send_registration_email(obj_police,obj2_police,password)

        # return redirect(viewpolice)
        return render(request, "addpolice.html")

    return render(request, "addpolice.html")

def generate_random_password():
    """Generate a random password."""
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def send_registration_email(obj_police,obj2_police,password):
    """Send registration email to the police station."""
    username = obj_police.email  # Assuming email is used as username
    subject = 'Registration Confirmation'
    message = f'Hello {obj2_police.policestation},\n\nYour account has been successfully registered with FaceTrace Pro.\n\nUsername: {username}\nPassword: {password}\n\nPlease keep your login credentials secure.\n\nRegards,\nThe FaceTrace Pro Team'
    from_email = 'sreesiva2310@gmail.com'  # Update with your email address or use a dedicated email account
    recipient_list = [obj_police.email]

    # Send email
    send_mail(subject, message, from_email, recipient_list)


def viewpolice(request):
    data=[]

    for d in Police.objects.all():
        obj=Login.objects.get(id=d.login_id)
        d.email=obj.email
        data.append(d)

    return(render(request,"viewpolice.html",{"police_details": data}))
def viewuser(request):
    data=User.objects.all()
    return(render(request,"viewuser.html",{"user_details": data}))


def get_phone_number(login_id, is_police):
    if is_police:
        # Fetch phone number for a police station
        try:
            police = Police.objects.get(login_id=login_id)
            return police.phnnum
        except Police.DoesNotExist:
            return None
    else:
        # Fetch phone number for a user
        try:
            user = User.objects.get(login_id=login_id)
            return user.phn_num
        except User.DoesNotExist:
            return None
        
# def missing(request):
#     persons = MissingPerson.objects.all()
#     personobj=[]
    
#     for person in persons:
#         reported_by_phone = get_phone_number(person.reported_by, is_police=False)
#         police_station_phone = get_phone_number(person.investigating_police, is_police=True)
        
#         personobj.append({
#             'person': person,
#             'reported_by_phone': reported_by_phone,
#             'police_station_phone': police_station_phone
#         })
    
#     return render(request, "missing.html", {"missingperson": personobj})

# def  missing(request):
#     queryset = MissingPerson.objects.all()
#     search_query = request.GET.get('search', '')
#     if search_query:
#         queryset = queryset.filter(aadhar_number__icontains=search_query)
    
#     context = {'missingperson': queryset}
#     return render(request,"missing.html",context)
        
def missing(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        persons = MissingPerson.objects.filter(aadhar_number=search_query)
    else:
        persons = MissingPerson.objects.all()
        
    personobj = []
    for person in persons:
        reported_by_phone = get_phone_number(person.reported_by, is_police=False)
        police_station_phone = get_phone_number(person.investigating_police, is_police=True)
        
        personobj.append({
            'person': person,
            'reported_by_phone': reported_by_phone,
            'police_station_phone': police_station_phone
        })
    
    return render(request, "missing.html", {"missingperson": personobj, "search_query": search_query if 'search' in request.GET else ''})


def missing3(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        persons = MissingPerson.objects.filter(aadhar_number=search_query)
    else:
        persons = MissingPerson.objects.all()
        
    personobj = []
    for person in persons:
        reported_by_phone = get_phone_number(person.reported_by, is_police=False)
        police_station_phone = get_phone_number(person.investigating_police, is_police=True)
        
        personobj.append({
            'person': person,
            'reported_by_phone': reported_by_phone,
            'police_station_phone': police_station_phone
        })
    
    return render(request, "missing3.html", {"missingperson": personobj, "search_query": search_query if 'search' in request.GET else ''})

        

# def missing(request):
#     if 'user_id' in request.session:
#         user_id = request.session['user_id']
#         personobj = MissingPerson.objects.all()
#         if Login.objects.get(id=user_id).is_police:
#             police = Police.objects.get(login_id=user_id)
#             return render(request, "missing.html", {"missingperson": personobj, "police": police})
#         else:
#             user = User.objects.get(login_id=user_id)
#             return render(request, "missing.html", {"missingperson": personobj, "user": user})
#     else:
#         # Redirect to login page if user is not logged in
#         return redirect(login)



# def missing(request):
#     # Retrieve all missing persons
#     missing_persons = MissingPerson.objects.all()
    
#     # Initialize user and phone number variables
#     user = None
#     phone_numbers = {}

#     # Check if the current user is logged in and retrieve user data if available
#     if 'user_id' in request.session:
#         user_id = request.session['user_id']
#         user = User.objects.get(login_id=user_id)
        
#         # Check if the user is a police officer
#         try:
#             police = Police.objects.get(login_id=user_id)
#             for missing_person in missing_persons:
#                 phone_numbers[missing_person.id] = police.phn_num
#         except Police.DoesNotExist:
#             # If the user is not a police officer, then the user is a regular user
#             for missing_person in missing_persons:
#                 phone_numbers[missing_person.id] = user.phn_num

#     # Pass the necessary data to the template
#     return render(request, "missing2.html", {
#         "missing_persons": missing_persons,
#         "user": user,
#         "phone_numbers": phone_numbers,
#     })





# def missing(request):
#     # Retrieve all missing persons
#     person= MissingPerson.objects.all()
    
#     # Initialize user and phone number variables
#     user = None
#     phone_number = None

#     # Check if the current user is logged in and retrieve user data if available
#     if 'user_id' in request.session:
#         user_id = request.session['user_id']
#         user = User.objects.get(login_id=user_id)
        
#         # Check if the user is a police officer
#         try:
#             police = Police.objects.get(login_id=user_id)
#             phone_number = police.phn_num
#         except Police.DoesNotExist:
#             # If the user is not a police officer, then the user is a regular user
#             phone_number = user.phn_num

#     # Pass the necessary data to the template
#     return render(request, "missing2.html", {
#         "missing_persons": person,
#         "user": user,
#         "phone_number": phone_number,
#     })


# def missing2(request):
#     person=MissingPerson.objects.all()
#     return(render(request,"missing2.html",{"missingperson": person}))
# def missing(request):
#     search_query = request.GET.get('search', '')  # Get the search query from the request
#     personobj = MissingPerson.objects.all()

#     if search_query:
#         personobj = personobj.filter(aadhar_number__icontains=search_query)

#     return render(request, "missing.html", {"missingperson": personobj, "search_query": search_query})
# def viewcase(request):
#     person=MissingPerson.objects.all()
#     return(render(request,"viewcase.html",{"missingperson": person}))


# def viewcase(request):
#     if 'user_id' in request.session:
#         user_id = request.session['user_id']
#         person = MissingPerson.objects.filter(reported_by=user_id)
#         return render(request, 'viewcase.html', {'missingperson': person})
#     else:
#         # Redirect to login page if user is not logged in
#         return redirect(login)

def viewcase(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        search_query = request.GET.get('search', '')  # Get the search query from the request

        person = MissingPerson.objects.filter(reported_by=user_id)
        

        if search_query:
            person= person.filter(aadhar_number__icontains=search_query)
        
        return render(request, 'viewcase.html', {'missingperson': person, 'search_query': search_query})
    else:
        # Redirect to login page if user is not logged in
        return redirect(login)
    
# def investigatingcase(request):
#     if 'user_id' in request.session:
#         user_id = request.session['user_id']
#         try:
#             police = Police.objects.get(login_id=user_id)
#             # Retrieve cases reported at the police station by both users and police
#             cases = MissingPerson.objects.filter(investigating_police=user_id) | MissingPerson.objects.filter(reported_by=user_id)
#             return render(request, 'investigatingcase.html', {'cases': cases,'police': police})
#         except Police.DoesNotExist:
#             # Redirect to user or police home page based on the user role
#             if Login.objects.get(id=user_id).is_police:
#                 return redirect(policehome)
#             else:
#                 return redirect(userhome)
#     else:
#         # Redirect to login page if user is not logged in
#         return redirect(login)
    
def investigatingcase(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        print(user_id)
        try:
            police = Police.objects.get(login_id=user_id)
            search_query = request.GET.get('search', '')  # Get the search query from the request
            
            # Retrieve cases reported at the police station by both users and police
            cases = MissingPerson.objects.filter(investigating_police=user_id)

            if search_query:
                cases = cases.filter(aadhar_number__icontains=search_query)

            return render(request, 'investigatingcase.html', {'cases': cases, 'police': police, 'search_query': search_query})
        except Police.DoesNotExist:
            # Redirect to user or police home page based on the user role
            if Login.objects.get(id=user_id).is_police:
                return redirect(policehome)
            else:
                return redirect(userhome)
    else:
        # Redirect to login page if user is not logged in
        return redirect(login)









    
def transfercase(request):
    case_id=request.GET['caseid']
    if request.POST:
        police=request.POST['station']
        obj=MissingPerson.objects.get(id=case_id)
        p=Police.objects.get(location=police)
        obj.investigating_police=p.login_id
        obj.save()
        return redirect(investigatingcase)
    
    police_stations = Police.objects.values_list('location', flat=True)
    return(render(request,"transfercase.html",{"locations":police_stations}))



def deletepolice(request):
    police_id=request.GET['id']
    obj=Police.objects.get(id=police_id)
    obj.delete()
    return(redirect(viewpolice))

def deleteperson(request):
    person_id=request.GET['id']
    obj=MissingPerson.objects.get(id=person_id)
    obj.delete()
    return(redirect(viewcase))
   


def editpolice(request):
    if(request.POST):
        police_id=request.POST['p_id']
        ps=request.POST['policestation']
        address=request.POST['address']
        location=request.POST['location']
        pn=request.POST['pn']
        email=request.POST['email']
        obj=Police.objects.get(id=police_id)
        obj.id=police_id
        obj.policestation=ps
        obj.address=address
        obj.location=location
        obj.phnnum=pn
        obj.email=email
        obj.save()
        return(redirect(viewpolice))
    
    police_id=request.GET['id']
    obj=Police.objects.get(id=police_id)
    return(render(request,"editpolicestation.html",{"police":obj}))   

def editperson(request):
    if(request.POST):
         person_id=request.POST.get('id')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         date_of_birth = request.POST.get('dob')
         address = request.POST.get('address')
         gender = request.POST.get('gender')
         obj=MissingPerson.objects.get(id=person_id)
         obj.id=person_id
         obj.first_name=first_name
         obj.last_name=last_name
         obj.date_of_birth=date_of_birth
         obj.address=address        
         obj.gender=gender
         obj.save()
         return(redirect(missing))
    person_id=request.GET['id']
    obj=MissingPerson.objects.get(id=person_id)
    person={
        "first_name":obj.first_name,
        "last_name":obj.last_name,
        "date_of_birth" :obj.date_of_birth ,
        "address":obj.address,
        "gender":obj.gender
    }
    return(render(request,"editperson.html",{"person":person}))  
    
    
    







def test(request):
    if(request.POST):
        name=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['pass']
        obj=Login(name=name,email=email,password=pwd)
        obj.save()
    return(render(request,"testregister.html"))



