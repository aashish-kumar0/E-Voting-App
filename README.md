# Secure E-Voting Application 🌍

A secure, modern, state-of-the-art Electronic Voting Web Application built with Python and Django. This project leverages cryptographic hashing algorithms to mathematically guarantee that users can cast their ballots with full anonymity while strictly preventing any possibility of duplicate voting.

## 🚀 Features

- **Robust User Authentication**: Integrated login and registration system. 
- **Cryptographic Security**: Uses SHA-256 hashing combining a voter's hidden ID and the server's secret key. This completely unlinks the user's personal identity from their chosen candidate in the database while mathematically denying secondary voting attempts.
- **Modern User Interface**: Built featuring a responsive, vibrant, and interactive "Glassmorphism" UI design entirely with Vanilla CSS.
- **Admin Dashboard**: Effortlessly monitor overall turnout metrics and live, real-time results via secure dashboard features.
- **Demo Ready**: Includes a script to instantly spawn dummy datasets (candidates, voters, and randomized pre-cast votes) to present an active environment.

## 🛠 Technology Stack

- **Backend**: Python 3, Django 6
- **Database**: SQLite (Default)
- **Frontend**: HTML5, Vanilla CSS

## 📋 Installation & Setup

If you are setting this project up locally, please follow these terminal commands:

1. **Clone or Open the Directory**
   Ensure you are in the main project directory: `e-voting`

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On **Windows**:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Django**
   ```bash
   pip install django
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## 🎲 Running the Demo Setup

To easily test the application's flow, you can populate the database with dummy candidates, users, and preliminary votes.

```bash
python populate_db.py
```
*Note: This script also creates a user named `demo_user` with the password `password123` who has **not** voted yet, allowing you to manually test the final voting flow.*

## 💻 Running the Server

Start the local development server:

```bash
python manage.py runserver
```

Open your browser and navigate to: `http://127.0.0.1:8000/`

## 🔒 Understanding the Code Setup
- `voting/models.py`: Defines the database tables for Candidates and Votes. Notice how `voter_hash` expects a 64-character hash.
- `voting/views.py`: Central location for all logic, including the process in `cast_vote()` where the cryptography check kicks in.
- `populate_db.py`: Centralized Python tool to clear and reset the testing database on the fly.
