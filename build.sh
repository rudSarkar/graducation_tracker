docker build -t gub_academic_progress:latest .
docker run -it -d -p 8000:8080 --name gub_academic_progress gub_academic_progress:latest