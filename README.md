🔗 URL Shortener | Flask • Docker • GitHub Actions • AWS EC2

A fully containerized URL Shortener application built with Flask and SQLite, featuring an automated CI/CD pipeline that deploys the latest version to AWS EC2 using GitHub Actions and Docker Hub.

⸻

📌 About The Project

This project demonstrates how a simple web application can be deployed using modern DevOps practices.

Users can generate a short URL from a long URL and access the original website using the generated link. Every change pushed to GitHub is automatically built, published to Docker Hub, and deployed to an AWS EC2 server without any manual steps.

⸻

✨ Features

* 🔗 Generate short URLs
* 🚀 Redirect to original URLs
* 💾 Store URL mappings using SQLite
* 🐳 Dockerized application
* 📦 Docker Compose support
* ⚡ Automated CI/CD with GitHub Actions
* ☁️ Automatic deployment to AWS EC2
* 🔄 Docker Hub integration

⸻

🛠️ Tech Stack

Category	Technologies
Backend	Flask, Python
Database	SQLite
Frontend	HTML, CSS
Containerization	Docker, Docker Compose
Version Control	Git, GitHub
CI/CD	GitHub Actions
Container Registry	Docker Hub
Cloud	AWS EC2
OS	Ubuntu Linux

⸻

📂 Project Structure

url-shortener-devops
│
├── .github/workflows/
│      └── docker.yml
│
├── static/
├── templates/
├── app.py
├── database.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── urls.db
└── README.md

⸻

⚙️ Application Workflow

User
 │
 ▼
Enter Long URL
 │
 ▼
Flask Application
 │
 ▼
Generate Short Code
 │
 ▼
Store in SQLite
 │
 ▼
Return Short URL
 │
 ▼
Open Short URL
 │
 ▼
Redirect to Original Website

⸻

🚀 CI/CD Workflow

Developer
    │
git push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
Build Docker Image
    │
    ▼
Push Image to Docker Hub
    │
    ▼
SSH into AWS EC2
    │
    ▼
Pull Latest Docker Image
    │
    ▼
Restart Container
    │
    ▼
Application Updated Automatically

⸻

🏗️ Architecture

                Internet
                    │
                    ▼
              AWS EC2 Instance
                    │
                    ▼
            Docker Container
                    │
                    ▼
         Flask URL Shortener App
                    │
                    ▼
             SQLite Database

⸻

🚀 Run Locally

Clone Repository

git clone https://github.com/MamtaGupta4/url-shortener-devops.git
cd url-shortener-devops

Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Run Application

python app.py

Open:

http://localhost:5000

⸻

🐳 Run Using Docker

Build Image

docker build -t url-shortener .

Run Container

docker run -d -p 5000:5000 --name url-shortener url-shortener

⸻

🐳 Run Using Docker Compose

docker compose up --build

Stop

docker compose down

⸻

☁️ Deployment

The application is deployed on an AWS EC2 instance using Docker.

Each push to the main branch automatically:

* Builds a Docker image
* Pushes the image to Docker Hub
* Connects to AWS EC2 using SSH
* Pulls the latest Docker image
* Recreates the Docker container
* Deploys the latest application

No manual deployment is required.

⸻

📸 Project Screenshots

Add screenshots here:

* 🖥️ Home Page
  <img width="2324" height="1136" alt="image" src="https://github.com/user-attachments/assets/c30f8b2d-77fd-45f4-aa80-512646054e64" />

* 🔗 URL Generated
  <img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/74985e9a-29c1-4e7f-b787-d74090757d2f" />

* 🐳 Docker Hub Repository
 <img width="1470" height="956" alt="Screenshot 2026-07-14 at 12 09 07" src="https://github.com/user-attachments/assets/ac04980b-a31a-49a1-a69b-2e2db0fdb262" />
  
* ⚡ GitHub Actions Success
  <img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/1dfbd1da-0d86-4625-8ad5-0a6b1abdad35" />

* ☁️ AWS EC2 Running Container
  <img width="1470" height="956" alt="Screenshot 2026-07-14 at 12 30 12" src="https://github.com/user-attachments/assets/9593fa28-758b-4d6a-9ca2-661e873218d3" />

* 🌐 Live Application
  <img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/49c8f35a-142c-4286-bb8f-d93ddae3fc01" />

⸻

📚 What I Learned

* Flask Web Development
* Docker & Docker Compose
* Git & GitHub
* GitHub Actions
* Docker Hub
* AWS EC2
* Continuous Integration (CI)
* Continuous Deployment (CD)
* Linux Commands
* SSH-based Deployment
* End-to-End DevOps Workflow

⸻

🔮 Future Enhancements

* Custom Short URLs
* QR Code Generator
* URL Analytics
* User Authentication
* MySQL Integration
* Kubernetes Deployment
* Terraform Infrastructure
* Prometheus & Grafana Monitoring

⸻

👩‍💻 Author

Mamta Gupta

* GitHub: https://github.com/MamtaGupta4
* LinkedIn: https://www.linkedin.com/in/mamtagupta2

⸻

⭐ If you like this project, don’t forget to give it a Star!
