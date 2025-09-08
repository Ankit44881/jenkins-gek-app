FROM python:3.11-slim
WORKDIR /app
COPY requirement.txt .
COPY . .
EXPOSE 8080
CMD ["python","app.py"]
