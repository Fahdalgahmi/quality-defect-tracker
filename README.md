# Quality Defect Tracker

## Overview

Quality Defect Tracker is a manufacturing quality management application developed to monitor, track, and analyze production defects. The system allows users to record defects, update statuses, filter records, visualize trends, and export data for reporting and analysis.

This project was inspired by real manufacturing quality processes, where defect tracking, root cause analysis, and production reporting are critical for maintaining product quality and supporting continuous improvement initiatives.

The application combines software development, database management, and data analytics concepts commonly used in manufacturing environments.

---

## Project Highlights

* Developed a full-stack manufacturing quality management application.
* Built REST APIs using FastAPI and PostgreSQL.
* Designed and implemented a PostgreSQL database schema for defect management and reporting.
* Implemented CRUD operations and defect workflow management.
* Created interactive dashboards and severity visualizations using Chart.js.
* Added search, filtering, and CSV export capabilities for operational reporting.
* Applied manufacturing quality concepts to solve a real-world business problem.

---

## Features

* Add New Defects
* View Defect Records
* Update Defect Status
* Delete Defects
* Search by Part Number
* Filter by Severity
* Dashboard KPI Cards
* Defect Severity Visualization
* CSV Export
* PostgreSQL Database Storage

---

## Technologies Used

### Backend

* Python
* FastAPI
* PostgreSQL
* Psycopg2

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Development Tools

* Git
* GitHub
* Visual Studio Code
* OpenAI ChatGPT (development assistance, debugging support, code review, and implementation guidance)


---

## System Architecture

Frontend (HTML/CSS/JavaScript)

↓

FastAPI REST API

↓

PostgreSQL Database

---

## Dashboard Features

### KPI Metrics

* Total Defects
* Open Defects
* Critical Defects

### Analytics

* Defect Severity Distribution Chart
* Search and Filtering Tools
* CSV Data Export

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Defect Table

![Table](screenshots/table.png)

### Add Defect Form

![Form](screenshots/form.png)

### Severity Analytics

![Chart](screenshots/chart.png)

---

## How To Run

### 1. Clone Repository

```bash
git clone https://github.com/Fahdalgahmi/quality-defect-tracker.git
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
DB_NAME=quality_defects
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run FastAPI

```bash
python -m uvicorn api:app --reload
```

### 7. Open the Application

Open the HTML frontend in your browser and ensure the FastAPI server is running.

---

## Future Enhancements

* Monthly Defect Trend Analysis Dashboard
* Power BI Integration for Executive Reporting
* User Authentication and Role Management
* Automated Email Notifications
* Production Shift Performance Analytics
* Defect Root Cause Trend Analysis
* Cloud Deployment

---

## Author

**Fahd Algahmi**

Bachelor of Science in Computer Science

Eastern Michigan University

---

## Project Purpose

This project demonstrates full-stack development, database integration, data visualization, and manufacturing quality analytics. It highlights the ability to design and develop software solutions that support operational decision-making and continuous improvement initiatives in a manufacturing environment.  