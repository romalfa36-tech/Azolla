# Azolla - Todo App

A Python-based todo application with user authentication and task management.

## 🚀 Features

- **User Authentication**: Secure user registration and login
- **Todo Management**: Create, read, update, and delete todos
- **Database Integration**: SQLite database for persistent storage
- **RESTful API**: Built with FastAPI for clean API endpoints
- **Responsive Design**: Web interface deployed on Render

## 📋 Project Structure

```
├── main.py              # Application entry point
├── auth.py              # Authentication logic
├── auth_routes.py       # Authentication endpoints
├── todo_routes.py       # Todo CRUD endpoints
├── models.py            # Database models
├── schemas.py           # Pydantic schemas for validation
├── database.py          # Database configuration
├── config.py            # Application configuration
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version specification
└── todoapp-db           # SQLite database file
```

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Authentication**: JWT tokens
- **Validation**: Pydantic
- **Server**: Uvicorn

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/romalfa36-tech/Azolla.git
cd Azolla
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

The application will be available at `http://localhost:8000`

## 🔐 Environment Variables

Create a `.env` file with the following variables:
```
DATABASE_URL=sqlite:///./todoapp-db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📚 API Documentation

Once the application is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🌐 Live Demo

Visit the live application at: [https://azolla-iiqd.onrender.com](https://azolla-iiqd.onrender.com)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Created by [romalfa36-tech](https://github.com/romalfa36-tech)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
