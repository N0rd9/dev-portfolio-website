# Dev Portfolio Website

A personal developer portfolio website with a Flask backend and a contact endpoint for storing submitted messages locally. The project presents profile information, featured projects, and a lightweight full-stack workflow.

## Features

- Personal portfolio homepage
- Project showcase sections
- Flask backend server
- Contact endpoint using JSON requests
- Local message storage in `messages.json`
- Simple frontend structure with HTML, CSS, and JavaScript

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- JSON

## Backend Overview

The Flask app serves the homepage and exposes a `/contact` route for POST requests. Submitted messages are normalized into a small object and appended to local JSON storage.

```python
message = {
    "name": data.get("name"),
    "email": data.get("email"),
    "message": data.get("message")
}
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open the local Flask URL shown in the terminal.

## What It Demonstrates

- Flask routing
- Template rendering
- JSON request handling
- Local persistence
- Frontend and backend integration
