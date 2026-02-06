# Portfolio Project - Django REST API + React Frontend

A modern, production-ready portfolio website built with Django REST Framework for the backend API and React for the frontend.

## Features

- **Django REST API**: RESTful API endpoints for projects, skills, experiences, and categories
- **React Frontend**: Modern single-page application with routing
- **Production Ready**: Dockerized, environment variables, security headers, PostgreSQL support
- **Responsive Design**: Mobile-friendly interface
- **Admin Dashboard**: Django admin with Jazzmin theme

## Tech Stack

- **Backend**: Django 5.2, Django REST Framework, PostgreSQL
- **Frontend**: React 18, Vite, Axios, React Router
- **Deployment**: Docker, Gunicorn, Whitenoise

## Setup Instructions

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (for production)
- Docker (optional)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create .env file from .env.example:
   ```bash
   cp .env.example .env
   ```
   Edit .env with your settings.

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

## API Endpoints

- `GET /api/projects/` - List all projects
- `GET /api/skills/` - List all skills
- `GET /api/experiences/` - List all experiences
- `GET /api/categories/` - List all categories

## Deployment

### Using Docker

1. Build the image:
   ```bash
   docker build -t portfolio .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 portfolio
   ```

### Manual Deployment

1. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

2. Use Gunicorn for production:
   ```bash
   gunicorn portfolio.wsgi
   ```

## Environment Variables

See .env.example for required environment variables.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
