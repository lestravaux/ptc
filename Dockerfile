# Use an official lightweight Python image.
FROM python:3.10-slim

# Set working directory
WORKDIR /app
# Set PYTHONPATH so Python finds the app package
ENV PYTHONPATH=/app
# Copy dependency files and install them
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
#COPY app/ .
COPY . .
# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
