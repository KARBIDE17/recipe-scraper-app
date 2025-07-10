Flask + Vue Full Stack Starter Template

Welcome to the Flask + Vue Starter Template, a full-stack project boilerplate that includes a Flask API backend and a Vite-powered Vue 3 frontend, both fully containerized with Docker.

GitHub Repository: https://github.com/KARBIDE17/flask-starting-template

Table of Contents

Project Structure

Cloning & Setup

Docker-Based Development

Backend Details

Frontend Details

Helpful Tips

Project Structure

flask-starting-template/
├── backend/             # Flask app (API)
│   ├── app.py
│   ├── models/
│   ├── resources/
│   ├── database.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/            # Vue 3 + Vite frontend
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml   # Multi-container setup
├── .gitignore
└── README.md            # You're reading this!

Cloning & Setup

git clone https://github.com/KARBIDE17/flask-starting-template.git
cd flask-starting-template

Make sure Docker is installed and running on your system.

Docker-Based Development

To build and run everything:

docker-compose up --build

Frontend: http://localhost:5173

Backend API: http://localhost:5000

To stop everything:

docker-compose down

Backend Details (Flask)

Location:

/backend

Tech Stack:

Flask: Minimal, expressive Python web framework

Flask-Smorest: API blueprint + schema validation (uses Marshmallow)

Peewee: Lightweight ORM (SQLite by default)

Flask-CORS: Enables cross-origin requests from frontend

API Routes:

GET /item: List items

POST /item: Create item

DELETE /item/<id>: Delete item

GET /store: List stores

POST /store: Create store

Local SQLite DB:

Auto-created in backend/ directory

Peewee models: ItemModel, StoreModel

You can inspect the database using the SQLite extension in VS Code or external tools like DB Browser for SQLite.

Frontend Details (Vue 3)

Location:

/frontend

Tech Stack:

Vue 3 with <script setup> syntax

Vite: Lightning-fast dev environment

Axios: API communication

Pug (optional): HTML templating used in components

Main Components:

AddItemForm.vue: Form for creating items

ItemList.vue: Shows items grouped by store

StoreList.vue: Optional display of stores

Axios API Helper:

Located in frontend/src/api.js, defines:

getItems, createItem, deleteItem

getStores, createStore

These use a shared api object that targets the backend.

Helpful Tips

1. Inspect SQLite DB

Install the SQLite extension for VS Code

Open the .sqlite3 file in the backend/ folder

Browse tables, run queries, etc.

2. Clean Docker Build

docker-compose down --volumes --remove-orphans

3. Environment Variables (Optional)

Consider using a .env file in both frontend and backend folders for config like:

# frontend/.env
VITE_API_URL=http://localhost:5000

# backend/.env
DATABASE_URL=sqlite:///data.db

License

MIT (or specify your license here)


Flask + Vue Full Stack Starter Template

Welcome to the Flask + Vue Starter Template, a full-stack project boilerplate that includes a Flask API backend and a Vite-powered Vue 3 frontend, both fully containerized with Docker.

GitHub Repository: https://github.com/KARBIDE17/flask-starting-template

Table of Contents

Project Structure

Cloning & Setup

Docker-Based Development

Backend Details

Frontend Details

Helpful Tips

Project Structure

flask-starting-template/
├── backend/             # Flask app (API)
│   ├── app.py
│   ├── models/
│   ├── resources/
│   ├── database.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/            # Vue 3 + Vite frontend
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml   # Multi-container setup
├── .gitignore
└── README.md            # You're reading this!

Cloning & Setup

git clone https://github.com/KARBIDE17/flask-starting-template.git
cd flask-starting-template

Make sure Docker is installed and running on your system.

Docker-Based Development

To build and run everything:

docker-compose up --build

Frontend: http://localhost:5173

Backend API: http://localhost:5000

To stop everything:

docker-compose down

Backend Details (Flask)

Location:

/backend

Tech Stack:

Flask: Minimal, expressive Python web framework

Flask-Smorest: API blueprint + schema validation (uses Marshmallow)

Peewee: Lightweight ORM (SQLite by default)

Flask-CORS: Enables cross-origin requests from frontend

API Routes:

GET /item: List items

POST /item: Create item

DELETE /item/<id>: Delete item

GET /store: List stores

POST /store: Create store

Local SQLite DB:

Auto-created in backend/ directory

Peewee models: ItemModel, StoreModel

You can inspect the database using the SQLite extension in VS Code or external tools like DB Browser for SQLite.

Frontend Details (Vue 3)

Location:

/frontend

Tech Stack:

Vue 3 with <script setup> syntax

Vite: Lightning-fast dev environment

Axios: API communication

Pug (optional): HTML templating used in components

Main Components:

AddItemForm.vue: Form for creating items

ItemList.vue: Shows items grouped by store

StoreList.vue: Optional display of stores

Axios API Helper:

Located in frontend/src/api.js, defines:

getItems, createItem, deleteItem

getStores, createStore

These use a shared api object that targets the backend.

Helpful Tips

1. Inspect SQLite DB

Install the SQLite extension for VS Code

Open the .sqlite3 file in the backend/ folder

Browse tables, run queries, etc.

2. Clean Docker Build

docker-compose down --volumes --remove-orphans

