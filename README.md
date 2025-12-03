🚀 Python Distroless Application

This project demonstrates how to containerize a Python application using:

Standard Docker image (Python runtime)

Optimized Distroless image with PyInstaller (binary-only, ultra-light)

The goal is to reduce image size for production workloads while maintaining security and performance.

📌 Project Structure
python-distroless-app/
│── app/
│   ├── main.py
│── requirements.txt
│── Dockerfile.normal
│── Dockerfile.distroless
│── .dockerignore
│── README.md

🔥 What this project solves
Build Type	Image Size	Includes Python?	Recommended For
Dockerfile.normal	~226 MB	Yes	Development
Dockerfile.distroless	~30 MB (can go <15MB with UPX)	No	Production / Edge workloads

The Distroless build ships only the compiled executable — no shell, no package manager → minimal attack surface and small footprint.

🧪 Run the Application Without Docker
pip install -r requirements.txt
python app/main.py

🐳 Build & Run Normal Docker Image
Build
docker build -t python-distroless:normal -f Dockerfile.normal .

Run
docker run -p 8080:8080 python-distroless:normal

🐳 Build & Run Distroless Optimized Image
Build
docker build -t python-distroless:distro-1 -f Dockerfile.distroless .

Run
docker run -p 8080:8080 python-distroless:distro-1


⛔ Note: Distroless does not include a shell.
To override the entrypoint for debugging:

docker run --entrypoint "" python-distroless:distro-1 /app/app

🧹 .dockerignore (Best Practice)
__pycache__
*.pyc
*.log
dist/
build/
.env

📦 Environment Variables (Optional)

If your app requires configuration, create .env:

PORT=8080


Then load inside Python using os.getenv.

🛡 Why Distroless?
Benefit	Explanation
Security	No shell, no package manager → reduced attack surface
Performance	Faster startup due to static binary
Size	~10–30 MB vs 200+ MB
Production-ready	Immutable and minimal
📍 When to Use Which Image?
Use Case	Recommended Image
Development & debugging	python:3.11-slim via Dockerfile.normal
Production deployment	Distroless (Dockerfile.distroless)
IoT / Edge devices	Distroless + UPX compression
 

👨‍💻 Author

Maintained by Kaushal Kishore.