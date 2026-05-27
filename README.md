# Student Task Manager

A simple and efficient web-based Student Task Manager application built using Django. This project helps students organize, manage, and track their daily academic tasks in one place.

---

## Features

* Add new tasks
* Update existing tasks
* Delete completed/unwanted tasks
* Mark tasks as completed
* User-friendly interface
* Django-powered backend
* SQLite database integration
* Responsive structure for easy customization

---

## Tech Stack

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Django (Python)
* **Database:** SQLite3
* **Version Control:** Git & GitHub

---

## Project Structure

```bash
student-task-manager/
│
├── config/                 # Project configuration files
├── tasks/                  # Main application folder
├── .vscode/                # VS Code settings
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
├── Procfile                # Deployment configuration
├── .gitignore              # Ignored files
└── README.md               # Project documentation
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anjali-562/student-task-manager.git
cd student-task-manager
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Database Migrations

```bash
python manage.py migrate
```

---

### 5. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

---

## Usage

1. Open the application in your browser.
2. Add tasks with required details.
3. Edit tasks whenever needed.
4. Mark tasks as completed after finishing them.
5. Delete tasks that are no longer required.

---

## Future Improvements

* User Authentication
* Task Deadlines & Reminders
* Priority Levels
* Email Notifications
* Dark Mode UI
* Task Categories & Filters
* Deployment on Render/Heroku

---

## Deployment

This project includes a `Procfile`, making it deployment-ready for platforms like:

* Heroku
* Render
* Railway

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## Author

**Anjali Gupta**

* GitHub: [https://github.com/anjali-562](https://github.com/anjali-562)

---

