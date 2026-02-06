w# TODO List for Upgrading Portfolio Project to DRF API + React Frontend (Production Ready)

## 1. Update Dependencies
- [x] Add DRF, django-cors-headers, psycopg2-binary, python-decouple to requirements.txt

## 2. Update Settings
- [x] Configure DRF in INSTALLED_APPS
- [x] Add CORS settings
- [x] Use environment variables for SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB credentials
- [x] Switch database to PostgreSQL
- [x] Add production settings (secure headers, logging)

## 3. Create API Layer
- [x] Create portapp/serializers.py with ModelSerializers for Category, Project, Skill, Experience
- [x] Update portapp/views.py to use DRF ModelViewSets
- [x] Update portapp/urls.py to include API routes

## 4. Update URLs
- [x] Add API namespace in portfolio/urls.py

## 5. Create React Frontend
- [x] Create frontend/ directory with Vite React app
- [x] Create components for Home, About, Portfolio, Contact
- [x] Fetch data from DRF API using Axios or Fetch
- [x] Add routing with React Router

## 6. Integrate Frontend
- [x] Configure Django to serve React build as static files
- [x] Add API proxy in React Vite config for development

## 7. Production Readiness
- [x] Create Dockerfile
- [x] Update Procfile for production
- [x] Create .env.example
- [ ] Add authentication for dashboard if needed

## 8. Testing & Deployment
- [ ] Add API tests
- [x] Update README.md with setup and deployment instructions
- [x] Test locally
- [ ] Deploy to production
