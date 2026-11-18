# 🛡️ Network Traffic Detection Using Machine Learning

## 📌 Project Overview

Network Traffic Detection is a web-based cybersecurity application developed using Python, Django, and Machine Learning. The project aims to identify and classify network traffic into different categories, helping users distinguish between normal network activities and potentially malicious traffic.

The system uses a trained **Random Forest Machine Learning Model** to analyze network traffic features and predict possible cyber threats.

The application provides a user-friendly web interface with separate Admin and User functionalities, user registration, login, account activation, and threat prediction.

## 🎯 Objectives

- Detect malicious and suspicious network traffic using Machine Learning.
- Classify network traffic into normal and attack categories.
- Provide probability scores for predicted threat categories.
- Develop a web-based interface for network traffic analysis.
- Provide separate functionalities for administrators and registered users.
- Improve awareness of different types of network-based cyberattacks.

## ✨ Key Features

### 👤 User Module
- User Registration and Login.
- User Account Activation.
- User Dashboard.
- Cyber Threat Overview.
- Network Traffic Prediction.
- Display of Machine Learning Prediction Results.
- Class Probability Visualization.

### 🔐 Admin Module
- Administrator Login.
- Admin Dashboard.
- View Registered Users.
- Activate Registered User Accounts.
- Manage User Access.

### 🤖 Machine Learning Module
- Random Forest Classification Model.
- Network Traffic Feature Processing.
- Feature Scaling using a trained Scaler.
- Label Encoding for Classification.
- Threat Prediction.
- Prediction Probability Scores.

## 🚨 Threat Categories

The trained model supports the following traffic categories:

| Category | Description |
|---|---|
| Good | Normal and legitimate network traffic |
| Brute Force | Repeated attempts to guess login credentials |
| DDoS | Distributed Denial-of-Service attack |
| FTP-Patator | FTP-based brute-force attack |
| PortScan | Network port scanning activity |
| SSH-Patator | SSH-based brute-force attack |

## 🛠️ Technologies Used

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Machine Learning
- Scikit-learn
- NumPy
- Joblib

### Database
- SQLite

### Machine Learning Model
- Random Forest Classifier
- MinMax/Feature Scaling (trained scaler artifact)
- Label Encoder

### Development Environment
- Visual Studio Code
- Python
- Django Development Server

## 📊 Network Traffic Features

The application accepts the following seven network traffic features for prediction:

1. Destination Port
2. Flow Duration (µs)
3. Forward Packet Length Mean
4. Backward Packet Length Mean
5. Flow IAT Mean
6. Backward Packets per Second
7. Average Packet Size

These features are processed using the saved scaler before being passed to the trained Random Forest model.

## 🏗️ Project Architecture

```text
Network Traffic Detection
│
├── admins/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── users/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── network_traffic/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── AdminLogin.html
│   ├── UserLogin.html
│   ├── UserRegistration.html
│   ├── Home.html
│   ├── Base.html
│   │
│   ├── admins/
│   │   ├── AdminBase.html
│   │   ├── AdminHome.html
│   │   └── UserDetails.html
│   │
│   └── users/
│       ├── UserBase.html
│       ├── UserHome.html
│       ├── Prediction.html
│       └── overview.html
│
├── static/
│   └── Images and Static Resources
│
├── media/
│   └── Random Forest Model
│
├── scaler.pkl
├── label_encoder.pkl
├── db.sqlite3
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### Step 2: Navigate to the Project Directory

```bash
cd network_traffic
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Kali Linux:**

```bash
source venv/bin/activate
```

### Step 5: Install Required Dependencies

```bash
pip install django numpy scikit-learn joblib
```

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Run the Django Development Server

```bash
python manage.py runserver
```

### Step 8: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔄 Working Process

1. The user accesses the Network Traffic Detection web application.
2. The user registers and logs into the system.
3. The administrator activates the registered user account.
4. The user accesses the Cyber Threat Overview section.
5. The user enters the required network traffic features.
6. The application processes the input using the trained scaler.
7. The Random Forest model analyzes the processed features.
8. The system predicts the corresponding network traffic category.
9. The application displays the predicted category and class probability scores.

## 🔮 Future Enhancements

- Real-time network packet capture and analysis.
- Integration with Wireshark and other network monitoring tools.
- Live network traffic monitoring.
- Advanced Deep Learning-based threat detection.
- Automated threat alert notifications.
- Network traffic visualization and analytics.
- Integration with Security Operations Center (SOC) dashboards.
- Automated malicious traffic response mechanisms.

## 🎓 Project Information

**Project Name:** Network Traffic Detection Using Machine Learning

**Domain:** Cybersecurity / Network Security

**Project Type:** Machine Learning and Web Application

**Backend:** Python and Django

**Machine Learning Algorithm:** Random Forest Classifier

**Database:** SQLite

## 👨‍💻 Author

**G. Sumanth**

B.Tech – Computer Science and Engineering (Cyber Security)

Interested in Cybersecurity, Ethical Hacking, Network Security, and Machine Learning.

## 📜 Disclaimer

This project is developed for educational and research purposes. The system is intended to demonstrate Machine Learning-based network traffic classification and cybersecurity threat detection.

It should not be considered a replacement for enterprise-grade network intrusion detection and prevention systems.

---

⭐ If you find this project useful, consider giving the repository a star!
