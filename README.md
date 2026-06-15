# 📚 Library Book Management API

A beginner-friendly CRUD API built with **FastAPI** and a plain HTML/JS frontend.  
Live demo hosted on GitHub Pages.

🌐 **Live Demo:** [backenddeveloperhub.github.io/Library_book_management-_api](https://backenddeveloperhub.github.io/Library_book_management-_api/)

---

## 🚀 Features

- ✅ Add new books
- 🔍 Find book by ID
- 📖 List all books
- ❌ Delete books
- CORS enabled for frontend-backend communication

---

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| Backend | FastAPI + Pydantic |
| Frontend | HTML + JavaScript |
| Hosting | GitHub Pages |

---

## 📁 Project Structure


├── main.py          # FastAPI backend
├── index.html       # Frontend UI
├── requirements.txt # Dependencies
└── LICENSE



---

## ⚙️ Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/BackendDeveloperHub/Library_book_management-_api.git
cd Library_book_management-_api


2. Install dependencies

pip install -r requirements.txt

3. Run the API

uvicorn main:app --reload
4. Open frontend


index.html → open in browser

⚠️ Make sure API is running at localhost:8000 before using the frontend.

📡 API Endpoints
Method
Endpoint
Description
GET
/books
Get all books
POST
/books
Add a new book
GET
/books/{id}
Get book by ID
DELETE
/books/{id}
Delete a book
🤝 Contributing
Part of BackendDeveloperHub open-source community.
PRs welcome!
---

## Epdi Add Pannanum

```bash
# Repo clone pannu
git clone https://github.com/BackendDeveloperHub/Library_book_management-_api.git
cd Library_book_management-_api

# README create pannu
# (mela irukka content paste pannu)
nano README.md

# Commit & push
git add README.md
git commit -m "docs: add README"
git push




