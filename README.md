# 🔐 Software Security Lab – Secure Web Application

## 📌 Overview

This project demonstrates a **secure web application with login functionality** implementing modern security practices like **password hashing and salting**. It also covers multiple software security experiments such as SQL Injection, secure authentication, vulnerability scanning, and more.

---

## 🎯 Objectives

* Identify common software vulnerabilities
* Implement secure coding techniques
* Demonstrate attacks like SQL Injection
* Secure authentication using hashing & salting
* Analyze and improve application security

---

## 🧪 Experiments Covered

| Exp | Title                              |
| --- | ---------------------------------- |
| E1  | Vulnerability Identification       |
| E2  | SQL Injection Attack & Prevention  |
| E3  | Password Hashing                   |
| E4  | Secure Code Review                 |
| E5  | Network Traffic Analysis           |
| E6  | Threat Modeling (STRIDE)           |
| E7  | Secure Authentication System       |
| E8  | Vulnerability Scanning (OWASP ZAP) |
| E9  | Browser Artifact Analysis          |
| E10 | Incident Response (Log Analysis)   |

---

## 🔐 Key Feature – Secure Login System

* User Registration & Login
* Passwords stored using **bcrypt hashing**
* Automatic **salting using `password_hash()`**
* Secure verification using `password_verify()`

---

## 🛠 Technologies Used

* PHP
* MySQL (phpMyAdmin)
* XAMPP (Apache Server)
* HTML
* OWASP ZAP
* Wireshark

---

## 📂 Project Structure

```
htdocs/
 └── Labeval/
      └── exp7/
           └── login.php
```

---

## 🚀 How to Run

1. Install XAMPP
2. Start **Apache** and **MySQL**
3. Place project folder inside:

   ```
   C:\xampp\htdocs\Labeval\exp7
   ```
4. Open browser:

   ```
   http://localhost/Labeval/exp7/login.php
   ```
5. Register and login

---

## 🔍 Security Implementation

* ❌ No plain text passwords
* ✔ Password hashing using `password_hash()`
* ✔ Automatic salting
* ✔ Secure password verification
* ✔ Protection against password theft

---

## 🎤 Viva Explanation (Short)

> This project implements a secure authentication system where passwords are hashed using bcrypt and automatically salted. It prevents storing plain-text passwords and improves overall application security.

---

## 📊 Result

* Secure login system successfully implemented
* Passwords stored in hashed format
* Authentication verified securely

---

## 📌 Conclusion

This project demonstrates how secure coding practices like hashing and salting protect user credentials and prevent common attacks such as password leaks and unauthorized access.

---

## 👨‍💻 Author

Uday Veer
B.Tech CSE (Cyber Security)

---
