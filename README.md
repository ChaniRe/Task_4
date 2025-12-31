# MinIO Object Storage Task

This project demonstrates how to work with Object Storage using **MinIO** and **Python**. It covers the full cycle of infrastructure setup, manual management, and automated CRUD operations.

## Task Overview
The goal of this task was to deploy a local MinIO server using Docker and interact with it programmatically to perform basic storage operations.

### Key Features implemented:
* **Infrastructure:** Running MinIO in a Docker container with persistent data mapping.
* **Random Object Creation:** Automatically generating files with random names and content.
* **List & Read:** Retrieving and displaying stored objects and their data.
* **Object Update:** Demonstrating the "Overwrite" nature of Object Storage.
* **Versioning Concept:** Understanding how versioning protects data during updates.
* **Object Removal:** Cleaning up storage programmatically.

## Tech Stack
* **Server:** [MinIO](https://min.io/) (S3 Compatible Storage)
* **Environment:** Docker & Docker Compose
* **Language:** Python 3.x
* **Library:** `minio` (Official SDK) / `boto3`

## Getting Started

### 1. Run MinIO Server (Docker)
```bash
docker run -p 9000:9000 -p 9001:9001 \
  -v C:/Tasks/task4/minio_data:/data \
  -e "MINIO_ROOT_USER=admin" \
  -e "MINIO_ROOT_PASSWORD=password123" \
  minio/minio server /data --console-address ":9001"
