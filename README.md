# Public Info API

## 📌 Project Overview
This is a simple public API that returns basic information in **JSON format**. It provides:
- A registered email address
- The current UTC datetime in **ISO 8601 format**
- A GitHub repository URL containing the project code
- Additional system metadata

This project is implemented using **Python (Flask)**.

---

## 🚀 Features
- **Lightweight & Fast**: Minimal response time (<500ms)
- **CORS Enabled**: Allows cross-origin requests
- **Public Endpoint**: Accessible to anyone
- **Dynamically Generated DateTime**: Always returns the latest UTC timestamp

---

## 📂 Project Structure
```
basic-public-api/
│── python-api/    # Python implementation
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── .gitignore
│── README.md
```

---

## 🛠️ Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/CynthiaWahome/basic-public-api.git
cd basic-public-api/python-api/app.py
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
```
Activate the virtual environment:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the API Locally**
```sh
python app.py
```
The API will be accessible at:  
➡ **http://127.0.0.1:5000/**

---

## 📡 API Documentation
### **🔹 Endpoint: GET /**
Returns the required JSON response.

#### **Response Format (200 OK)**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo",
  "track": "Backend",
  "message": "Do it alone, do it broke, do it scared...JUST DO IT ✔ 🔥",
  "server_info": {
    "os": "Linux",
    "python_version": "3.10.12",
    "client_ip": "123.45.67.89"
  }
}

```

---

## 🌍 Deployment
The API is deployed to a **publicly accessible endpoint**.

### **Live URL**
```
https://basic-public-api-d1f963692f67.herokuapp.com/
```

---

## 🔗 Additional Resources
- [Python Developers](https://hng.tech/hire/python-developers)

---

## 📜 License
This project is open-source and available under the **MIT License**.

