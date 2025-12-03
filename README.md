 

---

# Python Distroless Application

This project demonstrates how to containerize a Python application using:

1. Standard Docker image (Python runtime)
2. Optimized Distroless image with PyInstaller (binary-only)

The goal is to reduce image size for production workloads while maintaining security and performance.

---

## Project Structure

```
python-distroless-app/
│── app/
│   ├── main.py
│── requirements.txt
│── Dockerfile.normal
│── Dockerfile.distroless
│── .dockerignore
│── README.md
```

---

## What this project solves

| Build Type            | Image Size | Includes Python? | Recommended For |
| --------------------- | ---------- | ---------------- | --------------- |
| Dockerfile.normal     | ~226 MB    | Yes              | Development     |
| Dockerfile.distroless | ~30 MB     | No               | Production      |

Distroless build ships only the compiled executable — no shell, no package manager, minimal attack surface and small size.

---

## Run the application without Docker

```
pip install -r requirements.txt
python app/main.py
```

---

## Build & run normal Docker image

Build:

```
docker build -t python-distroless:normal -f Dockerfile.normal .
```

Run:

```
docker run -p 8080:8080 python-distroless:normal
```

---

## Build & run Distroless optimized image

Build:

```
docker build -t python-distroless:distro-1 -f Dockerfile.distroless .
```

Run:

```
docker run -p 8080:8080 python-distroless:distro-1
```

If debugging is required (since distroless has no shell):

```
docker run --entrypoint "" python-distroless:distro-1 /app/app
```

---

## .dockerignore (recommended)

```
__pycache__
*.pyc
*.log
dist/
build/
.env
```

---

## Environment variables (optional)

If needed, create a `.env` file:

```
PORT=8080
```

Load in Python using `os.getenv`.

---

## Why Distroless?

| Benefit          | Explanation                       |
| ---------------- | --------------------------------- |
| Security         | No shell and no package manager   |
| Size             | ~10–30 MB instead of 200+ MB      |
| Fast             | Fast startup due to single binary |
| Production-ready | Immutable and minimal             |

---

## When to use which image

| Use Case                | Recommended Image              |
| ----------------------- | ------------------------------ |
| Development / Debugging | Dockerfile.normal              |
| Production              | Dockerfile.distroless          |
| Edge / IoT devices      | Dockerfile.distroless with UPX |

---

 
## Author

Maintained by Kaushal Kishore.

 
