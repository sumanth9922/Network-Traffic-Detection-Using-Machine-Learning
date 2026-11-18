from django.shortcuts import render,redirect
from .models import UserRegistrationModel
from django.contrib import messages

from .forms import UserRegistrationForm
# Create your views here.
def UserBase(request):
    return render(request,'users/UserBase.html')

def UserHome(request):
    return render(request,'users/UserHome.html')
    



def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistration.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistration.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

from django.shortcuts import render

def overview(request):
    threats = [
        {
            "label": "Good",
            "icon": "✅",
            "name": "Benign / Normal Traffic",
            "category": "Normal / Non-malicious",
            "description": "Represents typical, legitimate user behavior in the network (e.g., browsing, file transfers, etc.). No signs of attack."
        },
        {
            "label": "Brute Force",
            "icon": "🚨",
            "name": "Brute Force Attack",
            "category": "Credential-based Attack",
            "description": "Repeatedly tries different combinations of usernames and passwords to gain unauthorized access to systems (often targets SSH or FTP services).",
            "tools": "Hydra, Medusa, Ncrack"
        },
        {
            "label": "DDoS",
            "icon": "🌐",
            "name": "Distributed Denial-of-Service Attack",
            "category": "Volume-based Network Attack",
            "description": "Multiple machines flood a network or server with excessive traffic to exhaust resources and make it unavailable to legitimate users.",
            "tools": "Variants: SYN Flood, UDP Flood, ICMP Flood"
        },
        {
            "label": "FTP-Patator",
            "icon": "🔐",
            "name": "FTP Brute Force using Patator Tool",
            "category": "Credential Attack (targeting FTP)",
            "description": "Automated tool attack specifically crafted for brute-forcing FTP login credentials.",
            "tools": "Tool used: Patator"
        },
        {
            "label": "PortScan",
            "icon": "🔍",
            "name": "Port Scanning",
            "category": "Reconnaissance",
            "description": "Scans a host/network for open ports to identify services and vulnerabilities before launching an attack.",
            "tools": "Tools used: Nmap, Masscan"
        },
        {
            "label": "SSH-Patator",
            "icon": "🔐",
            "name": "SSH Brute Force using Patator Tool",
            "category": "Credential Attack (targeting SSH)",
            "description": "Uses brute force techniques to guess SSH login credentials (username/password) using the Patator tool."
        },
    ]
    return render(request, 'users/overview.html', {'threats': threats})


from django.shortcuts import render
from .forms import CyberThreatForm
import numpy as np
import joblib

# Load model, scaler, and label encoder (once)
model = joblib.load(r'media\best_random_forest_model (2).pkl')
scaler = joblib.load(r'C:\Users\gsuma\OneDrive\Desktop\18. Improving Intrusion Detection Systems\network traffic\network_traffic\scaler.pkl')
labelen = joblib.load(r'C:\Users\gsuma\OneDrive\Desktop\18. Improving Intrusion Detection Systems\network traffic\network_traffic\label_encoder.pkl')

def prediction(request):
    prediction = None
    label_confidences = {}

    if request.method == 'POST':
        form = CyberThreatForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = np.array([[data['destination_port'], data['flow_duration'],
                                  data['fwd_packet_length_mean'], data['bwd_packet_length_mean'],
                                  data['flow_iat_mean'], data['bwd_packets_per_s'],
                                  data['avg_packet_size']]])
            
            scaled = scaler.transform(features)
            pred_index = model.predict(scaled)[0]
            predicted_label = labelen.inverse_transform([pred_index])[0]

            # Confidence scores
            probs = model.predict_proba(scaled)[0]
            classes = labelen.inverse_transform(np.arange(len(probs)))
            label_confidences = {label: f"{round(prob * 100, 2)}%" for label, prob in zip(classes, probs)}

            prediction = predicted_label
    else:
        form = CyberThreatForm()

    return render(request, 'users/prediction.html', {
        'form': form,
        'predicted_label': prediction,
        'label_confidences': label_confidences
    })
     