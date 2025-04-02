# 📝 Note App Backend

This is the backend API for the Note App, built with **Django** and **Django REST Framework**. It supports creating, retrieving, updating, and deleting notes, with each note tied to a specific user and a status: To Do, In Progress, or Done.

---

## 🚀 Features

- Token-based authentication
- User-specific note access
- CRUD operations on notes
- Filter notes by user automatically
- Retrieve individual notes by ID
- Status management (`1 = To Do`, `2 = In Progress`, `3 = Done`)
- JSON API responses
- CORS support for frontend access

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default) / PostgreSQL (optional)
- REST framework token authentication

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/note-app-backend.git
cd note-app-backend
```
### 2. Create virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py migrate
```
### 5. Create a superuser
```bash
python manage.py createsuperuser
```
### 6. Run the development server
```bash
python manage.py runserver
```

---

## 🔐 Authentication
This app uses Token Authentication.
### Obtain a token:
```http
POST /api-token-auth/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```
### Use the token:
Include the token in the header for all requests:
```http header
Authorization: Token your_token_here
```
## 📋 API Endpoints
| Method | Endpoint | Description |
|--- | --- |--- |
| Get | /note/ | Get all notes for the authenticated user |
| Get | /note/<id>/ | Get a specific note by ID |
| Post | /note/ | Create a new note |
| Put | /note/ | Update an existing note(by note_id) |
| Delete | /note/<id>/ | Delete a note by ID |
> ### 🔒 All endpoints require authentication. Each user can only access their own notes.

---

## 🧾 Note Object Format
```json
{
  "note_id": 1,
  "title": "Finish the README",
  "content": "Write a complete and clear README for the project.",
  "status": 2
}
```

---

## 🗂 Status Values
| Status Code | Meaning |
| --- | --- |
| 1 | To Do |
| 2 | In Progress |
| 3 | Done |

---

## 🧪 Running Tests
```bash
python manage.py test
```

---

## 🔄 CORS (Frontend Access)
If you're connecting this backend to a React (or other) frontend, make sure the frontend domain is allowed in **settings.py**:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

---

## 📁 Optional: .env Configuration
If you're using **django-environ**, create a **.env** file:
```ini
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🧭 Future Improvements
- JWT authentication support
- Pagination and filtering
- Search functionality
- Tags or categories for notes
- WebSocket-based real-time updates

---

## 🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is licensed under the MIT License. See LICENSE for details.
> Let me know if you'd like:
> - A section on how to deploy to Railway / Render / Heroku
> - An OpenAPI or Swagger UI setup
> - A Postman collection export
> 
> I'm happy to help with any of that too!


