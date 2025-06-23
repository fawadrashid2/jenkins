# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Create a simple HTTP server script
COPY hello.py .

# Expose port 89
EXPOSE 85

# Run the script
CMD ["python", "hello.py"]
