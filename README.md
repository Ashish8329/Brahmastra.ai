# Brahmastra.ai  

**Brahmastra.ai** is a cutting-edge AI-powered tool designed to streamline your job search by automating the tedious processes involved in finding and applying for jobs. Whether you're targeting specific companies or want to stay ahead of new opportunities, Brahmastra.ai gives you the competitive edge you need to succeed.  

## Features  

### 🚀 Real-Time Job Tracking  
- Monitors career pages of your selected companies automatically.  
- Keeps you updated on new job postings as soon as they go live.  

### 🔔 Instant Notifications  
- Sends real-time alerts when relevant positions are available.  
- Ensures you act quickly on high-demand roles.  

### 🤖 Automated Applications  
- Submits applications for pre-configured roles using your saved details.  
- Saves time and effort by reducing repetitive manual tasks.  

### 🎯 Customizable Job Alerts  
- Filter job postings by keyword, title, location, or other preferences.  
- Receive personalized alerts tailored to your career aspirations.  

### 📊 Application Management Dashboard  
- Track application statuses across multiple companies.  
- View a clear, user-friendly summary of your application progress.  

## Why Brahmastra.ai?  

Finding the right job is challenging, especially when it involves:  

- Constantly monitoring multiple career pages.  
- Applying quickly for high-demand roles.  
- Managing numerous applications across companies.  

**Brahmastra.ai** eliminates these obstacles by automating the job search and application process, enabling you to focus on preparing for interviews and achieving your career goals.  


# Project Installation Guide

This is a guide to set up and run the project locally on your machine.

---

## Prerequisites

Make sure you have the following installed:

- Python (>= 3.8)
- pip (Python package installer)
- Virtualenv (optional but recommended)
- Git
 
---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate the project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

### 5. Run Migrations

Apply database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin User)

Create a superuser for accessing the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser credentials.

### 7. Run the Development Server

Start the local Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to see the project running.

---

## API Documentation (Optional)

If you're using DRF and Swagger for API documentation:

- Navigate to: `http://127.0.0.1:8000/swagger/` to view the API docs.

---
 

## Troubleshooting

- Ensure all dependencies are installed.
- Check `.env` or `settings.py` for correct database configurations.
- Verify that the database server is running.

---

## License

This project is licensed under the [MIT License](LICENSE).
