# 🎓 Student & Course Management API

A professional, production-ready **backend API** built with **FastAPI** and **MySQL**. This project demonstrates advanced database design, secure API development, and comprehensive documentation. It is designed to be the backend for a modern frontend application.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

*   **Database:**
    *   MySQL schema with One-to-One, One-to-Many, and Many-to-Many relationships.
    *   Full constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`).
    *   Advanced features: Triggers, Views, Stored Procedures, Full-text Search.
*   **API:**
    *   25+ RESTful endpoints for complete CRUD operations.
    *   Automatic, interactive API documentation (Swagger UI & ReDoc).
    *   Robust error handling with appropriate HTTP status codes.
    *   Search and pagination support.
    *   Pydantic validation for all requests and responses.

## 🚀 Live Demo

You can interact with a live, deployed version of this API:

*   **Base URL:** `https://crud-application-xlua.onrender.com`
*   **Interactive API Docs (Swagger UI):** [https://crud-application-xlua.onrender.com/docs](https://crud-application-xlua.onrender.com/docs)
*   **Alternative Docs (ReDoc):** [https://crud-application-xlua.onrender.com/redoc](https://crud-application-xlua.onrender.com/redoc)

> **Note:** This is a demo instance. Data may be reset periodically.

## 🚀 Getting Started (Local Development)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.9+
*   MySQL Server 8.0+
*   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/student-course-api.git
    cd student-course-api
    ```

2.  **Set up a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the project root and populate it with your MySQL credentials. Use the `.env.example` file as a template.
    ```bash
    cp .env.example .env
    # Edit .env with your actual credentials
    ```

5.  **Create the Database:**
    Log in to your MySQL server and create the database specified in your `.env` file (default: `crud_app_db`).
    ```sql
    CREATE DATABASE crud_app_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```

6.  **Create Database Tables & Sample Data:**
    Run the setup script to create all tables and populate sample data.
    ```bash
    python create_tables.py
    ```

7.  **Run the Application:**
    Start the FastAPI server.
    ```bash
    uvicorn main:app --reload
    ```

8.  **Access the API Locally:**
    *   **API Base URL:** `http://localhost:8000`
    *   **Interactive Docs (Swagger UI):** `http://localhost:8000/docs`
    *   **Alternative Docs (ReDoc):** `http://localhost:8000/redoc`

## 📡 API Endpoints

The API provides comprehensive CRUD operations for Students, Courses, Enrollments, and Student Profiles.

### Students

| Method | Endpoint           | Description                  |
| :----- | :----------------- | :--------------------------- |
| `POST` | `/students/`       | Create a new student.        |
| `GET`  | `/students/`       | Get a list of students.      |
| `GET`  | `/students/{id}`   | Get a single student.        |
| `PUT`  | `/students/{id}`   | Update a student.            |
| `DELETE`| `/students/{id}`  | Delete a student.            |

*(Similar tables for `/courses/`, `/enrollments/`, and `/students/{id}/profile`)*

### Advanced Endpoints

*   `GET /students/{id}/courses` - Get all courses for a student.
*   `GET /courses/{id}/students` - Get all students in a course.
*   `GET /students/{id}/gpa` - Get a student's GPA.

## 🌐 Deployment: Where and How

This is a **backend API server**, not a static website. It requires a platform that can run persistent Python processes.

### ❌ Do NOT Deploy Here

*   **Netlify:** Designed for static sites (HTML, CSS, JS) and serverless functions. It will fail to run your long-running FastAPI server.

### ✅ Recommended Deployment Platforms

Deploy your **backend API** to one of these services:

#### 1. 🚀 Render.com (Easiest)
Perfect for Python apps with a generous free tier.
1.  Push your code to GitHub.
2.  Sign up at [Render.com](https://render.com).
3.  Create a new **Web Service**.
4.  Connect your repo.
5.  Set **Build Command:** `pip install -r requirements.txt`
6.  Set **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
7.  Add your MySQL credentials as **Environment Variables** in the Render dashboard.
8.  Deploy! You'll get a URL like: `https://my-student-api.onrender.com`

#### 2. 🛤️ Railway.app (Also Great)
Very user-friendly with a free tier.
1.  Push your code to GitHub.
2.  Sign up at [Railway.app](https://railway.app).
3.  Click "New Project" -> "Deploy from GitHub".
4.  Select your repo. Railway will auto-detect Python.
5.  Add your MySQL credentials in the "Variables" tab.
6.  Deploy! You'll get a URL like: `https://my-student-api.up.railway.app`

#### 3. ☁️ AWS / GCP / Azure (Advanced)
For maximum control and scalability. Deploy using services like AWS Elastic Beanstalk or Google App Engine.

---

## 💻 Connecting a Frontend (Deployable on Netlify!)

You can build a **frontend** application (using React, Vue, Angular, or even plain HTML/JS) that consumes this API. **This frontend *can* and *should* be deployed on Netlify.**

### Architecture

*   **Frontend (Hosted on Netlify):** `https://your-cool-frontend.netlify.app`
    *   This is what users interact with (buttons, forms, lists).
*   **Backend API (Hosted on Render/Railway):** `https://crud-application-xlua.onrender.com`
    *   This is where data is stored and managed. The frontend sends requests here.

### How to Connect Your Frontend to the API

In your frontend code (e.g., JavaScript), use the `fetch` API or a library like `axios` to send HTTP requests to your deployed backend URL.

**Example (JavaScript):**

```javascript
// File: src/api.js (in your frontend project)

// Replace this with your ACTUAL deployed backend URL
const API_BASE_URL = 'https://crud-application-xlua.onrender.com';

// Function to get all students
export async function fetchStudents() {
    const response = await fetch(`${API_BASE_URL}/students/`);
    if (!response.ok) {
        throw new Error('Failed to fetch students');
    }
    return await response.json();
}

// Function to create a new student
export async function createStudent(studentData) {
    const response = await fetch(`${API_BASE_URL}/students/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(studentData),
    });
    if (!response.ok) {
        throw new Error('Failed to create student');
    }
    return await response.json();
}

Deploying Your Frontend to Netlify
Follow these steps:

Build your frontend project:
For a React app, run: npm run build
This creates a build (React) or dist (Vue) folder with the static files.
Push the code to GitHub:
Commit and push your entire project, including the build or dist folder, to a GitHub repository.
bash


1
2
3
git add .
git commit -m "Add built frontend for deployment"
git push origin main
Go to Netlify:
Visit https://app.netlify.com/ and sign up or log in.
Import Your Project:
Click the "Add new site" button.
Select "Import an existing project".
Connect Your Repository:
Choose your Git provider (e.g., GitHub).
Authorize Netlify if prompted.
Select the repository containing your frontend code.
Configure Build Settings:
Netlify will usually auto-detect the framework and suggest settings.
Build command: Confirm it's set correctly (e.g., npm run build).
Publish directory: Confirm it points to your build folder (e.g., build or dist).
Click "Deploy site".
Access Your Live Frontend:
Netlify will build and deploy your site.
Once done, it will provide you with a unique public URL (e.g., https://your-site-name.netlify.app).
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Emanuel Mutua - emanuel.mutua@gmail.com

Project Repository: https://github.com/emutua23/wk-8_database_final_project
Live Demo: https://crud-application-xlua.onrender.com